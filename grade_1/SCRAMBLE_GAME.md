# Scramble Word Game

**File:** `grade_1/scramble_word_game.html`
**Stage:** `grade_1/scramble_word_game.stage.html`
**Word lists:** `grade_1/word_lists.js`

## What it does

A letter spelling game for Grade 1 kids. Letters are scrambled and the child taps or drags them into the correct order. Speaks the word aloud on completion.

## Game flow

1. **Choose word list** — cards shown for each list in `word_lists.js`
2. **Choose word count** — buttons at steps of 5 (e.g. 5 / 10 / 15 / All 19 🌟)
3. **Play** — spell all selected words in random order, then see results

## Gameplay mechanics

- **Tap a letter** (< 200ms touch) → flies to the next empty slot, left to right like typing
- **Drag a letter** → drop on any specific slot
- **Correct** → slot turns green, letter stays
- **Wrong** → slot flashes red + shakes, letter returns to bank
- **3 wrong attempts** → first letter auto-revealed (yellow slot)
- **💡 Hint button** → reveals 2 random unfilled letters (yellow)
- ❤️❤️❤️ hearts show remaining attempts per word
- **🔊 Replay button** → appears next to the word emoji after completion; tapping speaks the word again (pulses 🔉 while playing)

## End screen

After all words, a celebration screen splits results into:
- ⭐ **Perfect!** — 0 wrong, 0 hints (green cards)
- 💪 **Practice more!** — any wrong or hint used (yellow cards)

Each word card shows: word text + remaining hearts + hint count badge.

## Adding a new word list

Edit `grade_1/word_lists.js` and add an entry to the `WORD_LISTS` array. Each word is an object with `word` and `emoji`:

```js
{
  id: "unique_id",
  name: "Display Name",
  emoji: "🎯",          // list card emoji
  words: [
    { word: "apple", emoji: "🍎" },
    { word: "banana", emoji: "🍌" },
  ]
}
```

Emoji falls back to 📝 if not provided. The `word_lists.js` file is the single source of truth for both words and emojis — no changes needed in the HTML.

**Command shortcut:** tell Claude:
> 新增 scramble word 名稱 [名稱] list: [word1 word2 word3 ...]

## Existing word lists

| ID | Name | Words |
|----|------|-------|
| `march26` | March 26 | shorts 🩳, books, baby, birthday, boy, brother, child, children, daddy, father, friend, girl, grandfather, grandmother, man, men, mother, mummy, sister |
| `week12` | Week 12 | difficult, different, hockey, unicycle, rocket, basketball, bounce, insect, baseball, paint |

## Development workflow

- New features go to `.stage.html` first for testing
- Once confirmed working, copy to `scramble_word_game.html` and remove the 🚧 STAGE title/badge
