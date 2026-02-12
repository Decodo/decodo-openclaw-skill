#!/usr/bin/env python3
"""Decodo Scraper OpenClaw Skill: search Google or scrape a URL."""

import argparse
import json
import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv()
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
        try:
            out = data["results"][0]["content"]["results"]["results"]
            print(json.dumps(out, ensure_ascii=False))
        except (KeyError, IndexError, TypeError):
            print(resp.text)
    else:
        try:
            content = data["results"][0]["content"]
            print(content if isinstance(content, str) else json.dumps(content, ensure_ascii=False))
        except (KeyError, IndexError, TypeError):
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
