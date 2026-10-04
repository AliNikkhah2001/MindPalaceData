---
title: "Deep-link test bench"
title_en: "Deep-link test bench"
summary: "One node exercising every app deep link: quiz, flashcards, PDF book, and PDF pages."
read: false
last_read: null
last_refreshed: 2026-09-15
course: French
tags: [french, test, deeplink]
lang: [fr, en]
---

# Deep-link test bench

Click each button in read/split preview. Each must leave the Cognitio tab and land on the target, focused.

## 1. Quiz
- [[quiz:2|Open the French starter quiz]]
- [[quiz:2]]

Expected: Quiz tab opens, "French podcast — starter quiz" is loaded in study mode.

## 2. Flashcards
- [[card:2|la baguette tradition]]
- [[card:3|gagner / perdre]]
- [[card:4|avoir le trac]]
- [[card:5]]
- [[card:6]]
- [[card:7]]

Expected: Flashcards tab opens in study mode, jumped to that card.

## 3. PDF book (whole)
- [[pdf:French-Reader-A2.pdf|Open the French Reader booklet]]
- [[pdf:French-Reader-A2.pdf]]

Expected: Library tab opens with French-Reader-A2.pdf loaded.

## 4. PDF specific pages
- [[pdf:French-Reader-A2.pdf#page=1|Reader p.1: cover]]
- [[pdf:French-Reader-A2.pdf#page=2|Reader p.2: boulangerie]]
- [[pdf:French-Reader-A2.pdf#page=3|Reader p.3: foot]]
- [[pdf:French-Reader-A2.pdf#page=4|Reader p.4: breton]]
- [[pdf:French-Reader-A2.pdf#page=5|Reader p.5: gastronomie]]
- [[pdf:French-Reader-A2.pdf#page=6|Reader p.6: vocab]]

Expected: Library tab opens with the booklet loaded AND scrolled to that page (watch the Pg indicator).

## 5. Normal note links still work
- [[ep01-baguette-magician]]
- [[index-francais]]

Expected: stays in Cognitio, opens the note in the editor.

#french #test #deeplink
