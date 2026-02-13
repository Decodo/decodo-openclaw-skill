# Decodo Scraper OpenClaw Skill
![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)
![License](https://img.shields.io/github/license/decodo/decodo)
<p align="center">
<p align="center">
<a href="https://dashboard.decodo.com/scrapers/pricing?utm_source=github&utm_medium=social&utm_campaign=openclaw"><img src="https://github.com/user-attachments/assets/13b08523-32b0-4c85-8e99-580d7c2a9055"></a>

[![](https://dcbadge.limes.pink/api/server/https://discord.gg/Ja8dqKgvbZ)](https://discord.gg/Ja8dqKgvbZ)
## Overview
This [OpenClaw](https://openclaw.ai/) skill integrates [Decodo's Web Scraping API](https://decodo.com/scraping/web) into any OpenClaw-compatible AI agent or LLM pipeline. It exposes two tools that agents can call directly:

- ```google_search``` – query Google Search and receive structured JSON results
- ```universal``` – fetch and parse any public webpage, returning clean Markdown

Backed by Decodo's residential and datacenter proxy infrastructure, the skill handles JavaScript rendering, bot detection bypass, and geo-targeting out of the box.

## Features
- Real-time Google Search results scraping
- Universal URL scraping
- Structured JSON or Markdown results
- Simple CLI interface compatible with any OpenClaw agent runtime
- Minimal dependencies — just Python with Requests
- Authentication via a single Base64 token from the [Decodo dashboard](https://dashboard.decodo.com/)

## Prerequisites
- [Python 3.9](https://www.python.org/downloads/) or higher
- [Decodo account](https://dashboard.decodo.com/) with access to the Web Scraping API
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
# Terminal
export DECODO_AUTH_TOKEN="your_base64_token"
```
```
# .env file
DECODO_AUTH_TOKEN=your_base64_token
```
## OpenClaw agent integration
This skill ships with a [SKILL.md](https://github.com/Decodo/decodo-openclaw-skill/blob/main/SKILL.md) file that defines both tools in the OpenClaw skill format. OpenClaw-compatible agents automatically discover and invoke the tools from this file without additional configuration.

To register the skill with your OpenClaw agent, point it at the repo root — the agent will read ```SKILL.md``` and expose ```google_search``` and ```universal``` as callable tools.
## Usage
### Google Search
Search Google and receive a structured array of results:
```
python tools/scrape.py --target google_search --query "your query"
```
### Scrape a URL
Fetch and convert any webpage to clean Markdown file:
```
python tools/scrape.py --target universal --url "https://example.com/article"
```
## Related resources
[Decodo Web Scraping API documentation](https://help.decodo.com/docs/web-scraping-api-introduction)

[OpenClaw documentation](https://docs.openclaw.ai/start/getting-started)

[ClaWHub – OpenClaw skill registry](https://docs.openclaw.ai/tools/clawhub)

## License
All code is released under the [MIT License](https://github.com/Decodo/Decodo/blob/master/LICENSE).
