# Decodo Scraper OpenClaw Skill

Decodo Scraper OpenClaw skill for the [Decodo Web Scraping API](https://help.decodo.com/docs/web-scraping-api-google-search). **Search Google** or **scrape any URL**; output is JSON (search) or markdown (scrape).

## Setup

1. Clone this repo and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set your auth token (Basic auth from [Decodo Dashboard](https://dashboard.decodo.com/) → Scraping APIs):
   ```bash
   export DECODO_AUTH_TOKEN="your_base64_token"
   ```
   Or put `DECODO_AUTH_TOKEN=...` in a `.env` file in the repo root.

## Usage

- **Search Google:**  
  `python tools/scrape.py --target google_search --query "your query"`

- **Scrape a URL:**  
  `python tools/scrape.py --target universal --url "https://example.com"`

**Output:** Google search → JSON array of results to stdout. Universal → plain markdown (page content) to stdout.

**[SKILL.md](SKILL.md)** defines the two tools (Search, Scrape URL) and commands for agent use.
