---
name: decodo-scraper
description: Search Google or scrape web pages using the Decodo Scraper OpenClaw Skill.
homepage: https://decodo.com
credentials:
  - DECODO_AUTH_TOKEN
env:
  required:
    - DECODO_AUTH_TOKEN
---

# Decodo Scraper OpenClaw Skill

Use this skill to search Google or scrape any URL via the [Decodo Web Scraping API](https://help.decodo.com/docs/web-scraping-api-google-search). **Search** outputs a JSON array of results; **Scrape URL** outputs plain markdown (page content).

**Authentication:** Set `DECODO_AUTH_TOKEN` (Basic auth token from Decodo Dashboard → Scraping APIs) in your environment or in a `.env` file in the repo root.

**Errors:** On failure the script writes a JSON error to stderr and exits with code 1.

---

## Tools

### 1. Search Google

Use this to find URLs, answers, or structured search results (organic results, AI overviews, related questions, etc.).

**Command:**
```bash
python tools/scrape.py --target google_search --query "your search query"
```

**Examples:**
```bash
python tools/scrape.py --target google_search --query "best laptops 2025"
python tools/scrape.py --target google_search --query "python requests tutorial"
```

Optional: `--geo us` or `--locale en` for location/language.

---

### 2. Scrape URL

Use this to get the content of a specific web page. By default the API returns content as **Markdown** (cleaner for LLMs and lower token usage).

**Command:**
```bash
python tools/scrape.py --target universal --url "https://example.com"
```

**Examples:**
```bash
python tools/scrape.py --target universal --url "https://example.com"
python tools/scrape.py --target universal --url "https://news.ycombinator.com/"
```

---

## Summary

| Action       | Target         | Argument   | Example command |
|-------------|----------------|------------|-----------------|
| Search      | `google_search`| `--query`  | `python tools/scrape.py --target google_search --query "laptop"` |
| Scrape page | `universal`    | `--url`    | `python tools/scrape.py --target universal --url "https://example.com"` |

**Output:** Search → JSON array to stdout. Scrape URL → markdown text to stdout.
