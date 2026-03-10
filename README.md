# Decodo Scraper OpenClaw Skill
![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg?logo=python)
![License](https://img.shields.io/github/license/decodo/decodo)
![powered by Decodo](https://img.shields.io/badge/powered_by-Decodo-red?)
![GitHub Repo stars](https://img.shields.io/github/stars/Decodo/decodo-openclaw-skill)

<p align="center">
<p align="center">
<a href="https://dashboard.decodo.com/scrapers/pricing?utm_source=github&utm_medium=social&utm_campaign=openclaw"> <img src="https://github.com/user-attachments/assets/a1e52a9e-3da1-4081-b3c6-053aafb8f196"/></a>

[![](https://dcbadge.limes.pink/api/server/https://discord.gg/Ja8dqKgvbZ)](https://discord.gg/Ja8dqKgvbZ)
## Overview
This [OpenClaw](https://openclaw.ai/) skill integrates [Decodo's Web Scraping API](https://decodo.com/scraping/web?utm_source=github&utm_medium=social&utm_campaign=openclaw) into any OpenClaw-compatible AI agent or LLM pipeline. It exposes these tools that agents can call directly:

| Tool              | Description                                                          | Perfect for                                                                              |
| :---------------- | :------------------------------------------------------------------- | :--------------------------------------------------------------------------------------- |
| `google_search`   | Real-time Google Search (SERP) results as structured JSON.           | Market research, competitor analysis, news monitoring, fact-checking, RAG pipelines.     |
| `universal`       | Scrape & parse any public webpage into clean Markdown.           | Summarizing articles, content aggregation, building custom datasets, general web browsing for AI agents. |
| `amazon`          | Parse Amazon product page data (price, reviews, specs, ASIN).        | eCommerce monitoring, price tracking, competitive intelligence, product research.        |
| `amazon_search`   | Search Amazon for products by keyword and get parsed results.        | Discovering products, tracking trends, and broad market analysis.                        |
| `youtube_subtitles` | Extract subtitles/transcripts from YouTube videos (by video ID).   | Video summarization, content analysis, sentiment tracking, accessibility.                |
| `reddit_post`     | Fetch a Reddit post's content, comments, and metadata (by post URL). | Social listening, community sentiment analysis, trend tracking, and gathering user feedback. |
| `reddit_subreddit` | Scrape Reddit subreddit listings (by subreddit URL).                | Monitoring specific communities, content discovery, niche market research.               |

Backed by Decodo's residential and datacenter proxy infrastructure, the skill handles JavaScript rendering, bot detection bypass, and geo-targeting out of the box.

## Why use Decodo for your OpenClaw agent?

*   **Zero blocks & CAPTCHAs**. Backed by Decodo's proxy infrastructure from 125M+ locations, the skill automatically handles JavaScript rendering, bot detection, and CAPTCHA bypass.
*   **Real-time data**. Access fresh, up-to-the-minute web data directly within your AI agent's workflow.
*   **LLM-optimized output**. Data is returned in structured JSON or clean Markdown, making it easy for LLMs to understand and process.
*   **Scalability**. Designed for high-volume data collection, ensuring your agent can scale from small tasks to complex projects.
*   **Minimal Friction**. Easy setup with a single authentication token.

## Features
- Real-time Google Search results scraping
- Universal URL scraping
- Amazon product page parsing (by URL)
- Amazon search (by query)
- YouTube subtitles/transcript by video ID
- Reddit post content by URL
- Reddit subreddit listing by URL
- Structured JSON or Markdown results
- Simple CLI interface compatible with any OpenClaw agent runtime
- Designed for scalable AI agent web scraping
- Minimal dependencies — just Python with Requests
- Authentication via a single Base64 token from the [Decodo dashboard](https://dashboard.decodo.com/?utm_source=github&utm_medium=social&utm_campaign=openclaw)

## Prerequisites
- [Python 3.9](https://www.python.org/downloads/) or higher
- [Decodo account](https://dashboard.decodo.com/?utm_source=github&utm_medium=social&utm_campaign=openclaw) with access to the Web Scraping API
- [OpenClaw](https://openclaw.ai/) installed on your machine

## Setup
1. Clone this repo.
```
git clone https://github.com/Decodo/decodo-openclaw-skill.git
```
2. Install dependencies.
```
pip install -r requirements.txt
```
3. Set your Decodo auth token as an environment variable (or create a ```.env``` file in the project root):
```
# Linux/macOS Terminal
export DECODO_AUTH_TOKEN="your_base64_token"

# Windows (PowerShell)
$env:DECODO_AUTH_TOKEN="your_base64_token"
```
```
# .env file
DECODO_AUTH_TOKEN=your_base64_token
```
## OpenClaw agent integration
This skill ships with a [SKILL.md](https://github.com/Decodo/decodo-openclaw-skill/blob/main/SKILL.md) file that defines all tools in the OpenClaw skill format. OpenClaw-compatible agents automatically discover and invoke the tools from this file without additional configuration.

To register the skill with your OpenClaw agent, point it at the repo root — the agent will read ```SKILL.md``` and expose ```google_search```, ```universal```, ```amazon```, ```amazon_search```, ```youtube_subtitles```, ```reddit_post```, and ```reddit_subreddit``` as callable tools.
## Usage
### Google Search
Search Google and receive structured JSON. Results are grouped by type: **organic** (main results), **ai_overviews** (AI-generated summaries), **paid** (ads), **related_questions**, **related_searches**, **discussions_and_forums**, and others depending on the query.
```
python3 tools/scrape.py --target google_search --query "your query"
```
### Scrape a URL
Fetch and convert any webpage to a clean Markdown file:
```
python3 tools/scrape.py --target universal --url "https://example.com/article"
```
### Amazon product page
Fetch parsed data from an Amazon product page (e.g., ads, product details). Use the product URL:
```
python3 tools/scrape.py --target amazon --url "https://www.amazon.com/dp/B09H74FXNW"
```
### Amazon search
Search Amazon and get parsed results (e.g., results list, delivery_postcode):
```
python3 tools/scrape.py --target amazon_search --query "laptop"
```
### YouTube subtitles
Fetch subtitles/transcript for a YouTube video (use the video ID, e.g., from `?v=VIDEO_ID`):
```
python3 tools/scrape.py --target youtube_subtitles --query "dFu9aKJoqGg"
```
### Reddit post
Fetch a Reddit post’s content (use the full post URL):
```
python3 tools/scrape.py --target reddit_post --url "https://www.reddit.com/r/nba/comments/17jrqc5/serious_next_day_thread_postgame_discussion/"
```
### Reddit subreddit
Fetch a Reddit subreddit listing (use the subreddit URL):
```
python3 tools/scrape.py --target reddit_subreddit --url "https://www.reddit.com/r/nba/"
```
## Related resources
[Decodo Web Scraping API documentation](https://help.decodo.com/docs/web-scraping-api-introduction)

[OpenClaw documentation](https://docs.openclaw.ai/start/getting-started)

[ClaWHub – OpenClaw skill registry](https://docs.openclaw.ai/tools/clawhub)

## License
All code is released under the [MIT License](https://github.com/Decodo/Decodo/blob/master/LICENSE).
