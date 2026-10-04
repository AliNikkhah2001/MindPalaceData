---
title: "Relation Extraction"
summary: "§II Annotating Linguistic Structure › Information Extraction:: CHAPTER 20 • INFORMATION EXTRACTION: RELATIONS, EVENTS, AND TIME ARTIFACT GENERAL AFFILIATION ORG AFFILIATION PARTWHOLE PERSON- SOCIAL PHYSICAL Located Near Business Family Lasting Personal CitizenResident- Ethnicity-"
level: "research"
series: "Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)"
read: false
last_read: null
last_refreshed: 2026-09-19
course: ML Research
tags: [nlp, llm, book, speech, section]
pages: "464-465"
---

# Relation Extraction

§II Annotating Linguistic Structure › Information Extraction: Relations, Events, and Time › Relation Extraction · pp. 464–465 · Speech and Language Processing (Jurafsky & Martin, 3rd ed. draft)

## Extrait
CHAPTER 20 • INFORMATION EXTRACTION: RELATIONS, EVENTS, AND TIME ARTIFACT GENERAL AFFILIATION ORG AFFILIATION PARTWHOLE PERSON- SOCIAL PHYSICAL Located Near Business Family Lasting Personal CitizenResident- Ethnicity- Religion Org-Location- Origin Founder Employment Membership Ownership Student-Alum Investor User-Owner-Inventor- Manufacturer Geographical Subsidiary Sports-Affiliation Figure 20.1 The 17 relations used in the ACE relation extraction task. text presents such a stereotypical situation since airlines often raise fares and then wait to see if competitors follow along. Here we can identify United as a lead airline that initially raised its fares, $6 as the amount, Thursday as the increase date, and American as an airline that followed along, leading to a filled template like the following: FARE-RAISE ATTEMPT:   LEAD AIRLINE: UNITED AIRLINES AMOUNT: $6 EFFECTIVE DATE: 2006-10-26 FOLLOWER: AMERICAN AIRLINES   Let’s assume that we have detected the named entities in our sample text (perhaps using the techniques of Chapter 17), and would like to discern the relationships that exist among the detected entities: Citing high fuel prices, [ORG United Airlines] said [TIME Friday] it has increased fares by [MONEY $6] per round trip on flights to some cities also served by lower-cost carriers.

## Key terms
- **relation** — 29 mentions
- **airline** — 10 mentions
- **text** — 6 mentions
- **united** — 6 mentions
- **is-a** — 6 mentions
- **american** — 5 mentions
- **entity** — 5 mentions
- **wikipedia** — 5 mentions

## Practice — open in app
- [[pdf:Speech and Language Processing.pdf#page=464|Speech and Language Processing.pdf p. 464]]

## Liens
- Up: [[research/slp/information-extraction-relations-events-and-time]]
- Next: [[research/slp/relation-extraction-algorithms]] →
- Document: [[research/slp-book]]

#nlp #llm #book #speech #research #section
