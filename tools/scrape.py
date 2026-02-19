#!/usr/bin/env python3
"""Decodo Scraper OpenClaw Skill: search Google, Amazon search/product, scrape URL, YouTube subtitles, Reddit post or subreddit."""

import argparse
import json
import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env"))

SCRAPE_URL = "https://scraper-api.decodo.com/v2/scrape"

TARGETS_NEED_QUERY = ("google_search", "amazon_search", "youtube_subtitles")
TARGETS_NEED_URL = ("universal", "amazon", "reddit_post", "reddit_subreddit")


def _first_result_content(data):
    """Get results[0].content from API response, or None if missing."""
    results = data.get("results") or []
    if not results or not isinstance(results[0], dict):
        return None
    return results[0].get("content")


def _err(msg, hint=None):
    obj = {"error": msg}
    if hint:
        obj["hint"] = hint
    print(json.dumps(obj), file=sys.stderr)


def scrape(args):
    token = os.environ.get("DECODO_AUTH_TOKEN")
    if not token:
        _err("Set DECODO_AUTH_TOKEN.")
        sys.exit(1)

    headers = {"Content-Type": "application/json", "Authorization": f"Basic {token}", "x-integration": "openclaw"}

    payloads = {
        "google_search": {"target": "google_search", "query": args.query, "headless": "html", "parse": True},
        "youtube_subtitles": {"target": "youtube_subtitles", "query": args.query},
        "reddit_post": {"target": "reddit_post", "url": args.url},
        "reddit_subreddit": {"target": "reddit_subreddit", "url": args.url},
        "amazon": {"target": "amazon", "url": args.url, "parse": True},
        "amazon_search": {"target": "amazon_search", "query": args.query, "parse": True},
        "universal": {"target": "universal", "url": args.url, "markdown": True},
    }
    payload = payloads[args.target]
    if args.target == "google_search":
        if args.geo:
            payload["geo"] = args.geo
        if args.locale:
            payload["locale"] = args.locale

    try:
        resp = requests.post(SCRAPE_URL, json=payload, headers=headers, timeout=120)
        resp.raise_for_status()
    except requests.RequestException as e:
        status_code = e.response.status_code if e.response is not None else None
        print(json.dumps({"error": str(e), "status_code": status_code}), file=sys.stderr)
        sys.exit(1)

    try:
        data = resp.json()
    except json.JSONDecodeError:
        _err("Invalid JSON in response")
        sys.exit(1)

    content = _first_result_content(data)
    if content is None:
        _err("Empty or unexpected response structure")
        if args.target in ("google_search", "universal"):
            print(resp.text)
        sys.exit(1)

    if args.target == "google_search":
        inner = (content or {}).get("results", {}).get("results") if isinstance(content, dict) else None
        if inner is not None:
            print(json.dumps(inner, ensure_ascii=False))
        else:
            _err("Could not extract search results", "API structure may have changed")
            print(resp.text)
    elif args.target == "youtube_subtitles":
        print(content if isinstance(content, str) else json.dumps(content, ensure_ascii=False))
    elif args.target in ("reddit_post", "reddit_subreddit"):
        print(json.dumps(content, ensure_ascii=False))
    elif args.target in ("amazon", "amazon_search"):
        inner = (content or {}).get("results") if isinstance(content, dict) else None
        if inner is not None:
            print(json.dumps(inner, ensure_ascii=False))
        else:
            _err(f"Could not extract {args.target} results")
            sys.exit(1)
    else:
        # universal
        print(content if isinstance(content, str) else json.dumps(content, ensure_ascii=False))


def main():
    parser = argparse.ArgumentParser(description="Decodo Scraper OpenClaw Skill: search Google, scrape URL, Amazon, YouTube subtitles, Reddit.")
    parser.add_argument("--target", required=True, choices=["google_search", "universal", "amazon", "amazon_search", "youtube_subtitles", "reddit_post", "reddit_subreddit"])
    parser.add_argument("--query", help="Required for google_search, amazon_search, or youtube_subtitles (video ID for YouTube).")
    parser.add_argument("--url", help="Required for universal, amazon, reddit_post, or reddit_subreddit.")
    parser.add_argument("--geo", help="Google search geo (e.g. us, gb).")
    parser.add_argument("--locale", help="Google search locale (e.g. en, de).")
    args = parser.parse_args()

    if args.target in TARGETS_NEED_QUERY and not args.query:
        parser.error(f"--query required for {args.target}")
    if args.target in TARGETS_NEED_URL and not args.url:
        parser.error(f"--url required for {args.target}")

    scrape(args)


if __name__ == "__main__":
    main()
