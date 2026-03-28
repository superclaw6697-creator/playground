# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository layout

```
playground/          ← Python backtest scripts + data
grade_1/             ← Kids' spelling games (static HTML)
research/            ← Company research reports (Markdown)
README.md            ← Project index with live links
```

## Deployment

All static files are served via **GitHub Pages** at:
`https://superclaw6697-creator.github.io/playground/`

No build step — push to `main` and GitHub Actions deploys automatically (~1 min).

---

## grade_1 — Kids' spelling games

### Scramble Word Game
**Files:** `scramble_word_game.html`, `word_lists.js`
**Stage file:** `scramble_word_game.stage.html` (test new features here first, then copy to production and remove the 🚧 badge)

Word lists live exclusively in `word_lists.js` as `WORD_LISTS` array. Each entry:
```js
{ id: "unique_id", name: "Display Name", emoji: "🎯",
  words: [{ word: "apple", emoji: "🍎" }] }
```
The HTML loads `word_lists.js` via `<script src="word_lists.js">` — no other changes needed to add a list.

To add words, user says: `新增 scramble word 名稱 [名稱] list: [word1 word2 ...]`

### Phonic Spelling Game
**Files:** `phonic_spelling_game.html`, `phonic_word_list.js`

Separate from the scramble game — word lists are in `phonic_word_list.js` as `PHONIC_WORD_LISTS` array (same shape as `WORD_LISTS`).

Current flow: TTS plays the word → kid writes the whole word on a canvas → Tesseract.js (PSM 8, single-word OCR) recognises the handwriting → letter-by-letter comparison shown (green = correct, red strikethrough = wrong, yellow ? = not recognised) → Next Word regardless of result.

Uses `tesseract.js@5` from CDN. First load takes a few seconds to download the language pack.

### Coin Counter Game
**File:** `coin_counting_game.html` — standalone, no external JS dependencies.

---

## research — Company reports

Markdown files. Naming convention: `公司名稱_EnglishName_StockCode.md`

To generate visual assets, use `generate_sige_poster.py` (requires matplotlib, numpy, and the macOS font paths for HanziPen/Hannotate are hardcoded — macOS only).

---

## playground — Python backtest

`fetch_data.py` fetches Taiwan 三大法人 + QQQ data into `data/`.
`backtest.py` runs analysis and writes charts to `output/`.

---

## ETF tracking cron job

Cron: `30 19 * * 1-5` runs `/Users/superclaw/etf_tracking/trigger_workflow.sh`
Triggers GitHub Actions workflow "ETF Holdings Tracker" in repo `superclaw6697-creator/etfatracking`.

---

## Telegram integration

Claude Code is reachable via Telegram bot. Incoming messages arrive as `<channel source="plugin:telegram:telegram" ...>` blocks. Always reply using the `mcp__plugin_telegram_telegram__reply` tool — text output is not visible in Telegram.
