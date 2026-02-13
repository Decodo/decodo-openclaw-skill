#!/usr/bin/env python3
"""Decodo Scraper OpenClaw Skill: search Google or scrape a URL."""

import argparse
import json
import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env"))

SCRAPE_URL = "https://scraper-api.decodo.com/v2/scrape"


def scrape(args):
    token = os.environ.get("DECODO_AUTH_TOKEN")
    if not token:
        print("Error: Set DECODO_AUTH_TOKEN.", file=sys.stderr)
        sys.exit(1)

    headers = {"Content-Type": "application/json", "Authorization": f"Basic {token}"}

    if args.target == "google_search":
        payload = {"target": "google_search", "query": args.query, "headless": "html", "parse": True}
        if args.geo:
            payload["geo"] = args.geo
        if args.locale:
            payload["locale"] = args.locale
    else:
        payload = {"target": "universal", "url": args.url, "markdown": True}

    try:
        resp = requests.post(SCRAPE_URL, json=payload, headers=headers, timeout=120)
        resp.raise_for_status()
    except requests.RequestException as e:
        err = {"error": str(e), "status_code": getattr(e.response, "status_code", None)}
        print(json.dumps(err), file=sys.stderr)
        sys.exit(1)

    try:
        data = resp.json()
    except json.JSONDecodeError:
        print(json.dumps({"error": "Invalid JSON in response"}), file=sys.stderr)
        sys.exit(1)

    if args.target == "google_search":
        results = data.get("results") or []
        if not results:
            print(json.dumps({"error": "Empty or unexpected response structure", "hint": "API may have changed"}), file=sys.stderr)
            print(resp.text)
            sys.exit(1)
        content = results[0].get("content") if isinstance(results[0], dict) else None
        inner = (content or {}).get("results", {}).get("results") if isinstance(content, dict) else None
        if inner is not None:
            print(json.dumps(inner, ensure_ascii=False))
        else:
            print(json.dumps({"error": "Could not extract search results", "hint": "API structure may have changed"}), file=sys.stderr)
            print(resp.text)
    else:
        results = data.get("results") or []
        if not results:
            print(json.dumps({"error": "Empty or unexpected response structure"}), file=sys.stderr)
            print(resp.text)
            sys.exit(1)
        content = results[0].get("content") if isinstance(results[0], dict) else None
        if isinstance(content, str):
            print(content)
        elif content is not None:
            print(json.dumps(content, ensure_ascii=False))
        else:
            print(json.dumps({"error": "Could not extract page content"}), file=sys.stderr)
            print(resp.text)


def main():
    parser = argparse.ArgumentParser(description="Decodo Scraper OpenClaw Skill: search Google or scrape a URL.")
    parser.add_argument("--target", required=True, choices=["google_search", "universal"])
    parser.add_argument("--query", help="Required for google_search.")
    parser.add_argument("--url", help="Required for universal.")
    parser.add_argument("--geo", help="Google search geo (e.g. us, gb).")
    parser.add_argument("--locale", help="Google search locale (e.g. en, de).")
    args = parser.parse_args()

    if args.target == "google_search" and not args.query:
        parser.error("--query required for google_search")
    if args.target == "universal" and not args.url:
        parser.error("--url required for universal")

    scrape(args)


if __name__ == "__main__":
    main()
