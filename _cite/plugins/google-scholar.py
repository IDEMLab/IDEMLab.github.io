import os
import re
import requests
from serpapi import GoogleSearch
from util import *


def get_doi_and_date_from_title(title):
    """Query CrossRef API for DOI and best-available ISO date from a title."""
    url = "https://api.crossref.org/works"
    params = {"query.title": title, "rows": 1}
    try:
        response = requests.get(url, params=params, timeout=10)
        items = response.json().get("message", {}).get("items", [])
        if items:
            item = items[0]
            doi = item.get("DOI", "")

            # Prefer print date, fall back to online date
            date_parts = (
                item.get("published-print", {}).get("date-parts")
                or item.get("published-online", {}).get("date-parts")
                or []
            )

            if date_parts and len(date_parts[0]) >= 1:
                parts = date_parts[0]
                year = str(parts[0])
                month = f"{parts[1]:02d}" if len(parts) > 1 else None
                day = f"{parts[2]:02d}" if len(parts) > 2 else None

                if month and day:
                    pub_date = f"{year}-{month}-{day}"
                elif month:
                    pub_date = f"{year}-{month}"
                else:
                    pub_date = year
            else:
                pub_date = ""

            return doi, pub_date
    except Exception as e:
        log(f"CrossRef DOI/date lookup failed: {e}", level="WARNING")

    return None, ""


def main(entry):
    """
    Receives single list entry from google-scholar data file
    Returns list of sources to cite
    """

    api_key = os.environ.get("GOOGLE_SCHOLAR_API_KEY", "")
    if not api_key:
        raise Exception('No "GOOGLE_SCHOLAR_API_KEY" env var')

    params = {
        "engine": "google_scholar_author",
        "api_key": api_key,
        "num": 100,
    }

    _id = get_safe(entry, "gsid", "")
    if not _id:
        raise Exception('No "gsid" key')

    @log_cache
    @cache.memoize(name=__file__, expire=60 * 60 * 24)
    def query(_id):
        params["author_id"] = _id
        return get_safe(GoogleSearch(params).get_dict(), "articles", [])

    response = query(_id)

    sources = []

    for work in response:
        title = get_safe(work, "title", "")
        gs_raw_date = get_safe(work, "year", "").strip().replace(" ", "")

        # Get DOI and structured publication date from CrossRef
        doi, cr_date = get_doi_and_date_from_title(title)

        # Fallback: parse GS year string if CrossRef returned no usable date
        if cr_date:
            formatted_date = cr_date
        else:
            match = re.match(r"^(\d{4})(?:/(\d{1,2}))?(?:/(\d{1,2}))?$", gs_raw_date)
            if match:
                y, m, d = match.groups()
                if d:
                    formatted_date = f"{y}-{int(m):02d}-{int(d):02d}"
                elif m:
                    formatted_date = f"{y}-{int(m):02d}"
                else:
                    formatted_date = y
            else:
                formatted_date = gs_raw_date if gs_raw_date else ""

        source = {
            "id": f"doi:{doi}" if doi else get_safe(work, "citation_id", ""),
            "title": title,
            "authors": list(map(str.strip, get_safe(work, "authors", "").split(","))),
            "publisher": get_safe(work, "publication", ""),
            "date": formatted_date,
            "link": get_safe(work, "link", ""),
        }

        source.update(entry)
        sources.append(source)

    return sources
