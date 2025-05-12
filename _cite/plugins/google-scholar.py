import os
import re
from serpapi import GoogleSearch
from util import *


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

        # Parse Google Scholar's YYYY/M or YYYY/M/D into ISO
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
            "id": get_safe(work, "citation_id", ""),
            "title": title,
            "authors": list(map(str.strip, get_safe(work, "authors", "").split(","))),
            "publisher": get_safe(work, "publication", ""),
            "date": formatted_date,
            "link": get_safe(work, "link", ""),
        }

        source.update(entry)
        sources.append(source)

    return sources
