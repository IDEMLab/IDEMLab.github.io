import os
import requests
from serpapi import GoogleSearch
from util import *
import re


def get_doi_from_title(title):
    """Query CrossRef API for a DOI based on the paper title."""
    url = "https://api.crossref.org/works"
    params = {"query.title": title, "rows": 1}
    try:
        response = requests.get(url, params=params, timeout=10)
        items = response.json().get("message", {}).get("items", [])
        if items:
            return items[0].get("DOI", "")
    except Exception as e:
        log(f"CrossRef DOI lookup failed: {e}", level="WARNING")
    return None


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
        year = get_safe(work, "year", "")
        title = get_safe(work, "title", "")

        # Format raw date into ISO format (YYYY, YYYY-MM, or YYYY-MM-DD)
        date_str = year.strip() if year else ""
        if re.fullmatch(r"\d{4}", date_str):
            formatted_date = date_str
        elif re.fullmatch(r"\d{4}/\d{1,2}", date_str):
            y, m = date_str.split("/")
            formatted_date = f"{y}-{int(m):02d}"
        elif re.fullmatch(r"\d{4}/\d{1,2}/\d{1,2}", date_str):
            y, m, d = date_str.split("/")
            formatted_date = f"{y}-{int(m):02d}-{int(d):02d}"
        else:
            formatted_date = date_str  # fallback if unexpected format

        # Try to get a Manubot-compatible DOI
        doi = get_doi_from_title(title)

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
