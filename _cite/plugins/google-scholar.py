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
        year = get_safe(work, "year", "").strip()

        # Get DOI and structured publication date from CrossRef
        doi, crossref_date = get_doi_and_date_from_title(title)
        gs_date_raw = get_safe(work, "year", "").strip().replace(" ", "")
        
        # Convert Google Scholar date (e.g., "2020/9/1") into ISO
        match = re.match(r"^(\d{4})(?:/(\d{1,2}))?(?:/(\d{1,2}))?$", gs_date_raw)
        if match:
            y, m, d = match.groups()
            if d:
                gs_date = f"{y}-{int(m):02d}-{int(d):02d}"
            elif m:
                gs_date = f"{y}-{int(m):02d}"
            else:
                gs_date = y
        else:
            gs_date = gs_date_raw
        
        # Use the date with more specificity
        def date_specificity(date_str):
            return date_str.count("-")  # 0: year, 1: year-month, 2: full date
        
        if gs_date and (date_specificity(gs_date) > date_specificity(crossref_date)):
            formatted_date = gs_date
        else:
            formatted_date = crossref_date or gs_date

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
