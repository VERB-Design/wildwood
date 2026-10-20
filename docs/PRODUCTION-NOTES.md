# Crestwood Investment Fund — Production Notes

Build: `crestwood/index.html` (+ `Locations Map.html`). Live: https://verb-design.github.io/wildwood/crestwood/
Copy source: *Copy Deck – Crestwood Investment Fund* (Google Doc 147w3OXPXgrG_E35TIuN8C2Ed7v3irGPlTqU7sYUWsw8), integrated 2026-10-20.

## Warnings

### Content accuracy — needs client sign-off
- **Operating locations.** Map and copy show *no* operating Everwild: Fernie, Banff, Harmony under construction (late 2027 – early 2028), four in development. Troy confirmed 2026-10-20. But the Everwild Brand Book and the supplied Canmore lifestyle shoot treat **Everwild Canmore as an open property** — confirm with Basecamp before launch.
- **Copy written by us, not the deck:** Fund ¶1 (built on Selly's "Experience is the asset" line — the BCG Brand Book PDF on Drive could not be read, 220 MB / no text layer); Fund ¶2 and pillar 2 (deck still said "four locations it operates in today"); Story ¶2 sentence and the "Three under construction" milestone; hero line "Capital raised at home, to build at home." (per Selly: Basecamp doesn't invest); all map card descriptions.
- **"Invested" elsewhere.** H2 "Raised in Canada. Invested in Canada." and Fund ¶3 "invested in Canadian communities" still use *invest* — same concern as Selly's hero comment; left as deck has them, flag to client.
- **Investment H2** changed to "Built for Canadian Investors" (Selly: registered accounts only from mid-January).
- **Market Opportunity stats.** Verified against GWI: US$6.8T global wellness economy 2024 (Monitor 2025) and Canada's 7.3% growth 2019–2023, top-ten fastest (GWI Canada release, Mar 2025). **Not verified:** the $9.8T projection's year (deck says 2030; review agent says GWI projects 2029) and US$13.3B Canadian wellness tourism. Deck's "$9.8M" corrected to **$9.8T**; "$6.8T" given "US$" to match stat 3; source line added under the stats (our wording). Client to confirm all three plus the source line. Section came from an *unaccepted suggestion* in the deck; Troy approved it as section two.
- **Minimum C$50,000** — from an unaccepted suggestion; Troy approved. Stat tile and Get in Touch body both updated.
- **Settings "where" lines** follow the deck (Toronto · Calgary · Vancouver, Whistler · Canmore · Rockies, Edmonton · Saskatoon · Winnipeg…) — they name cities with no Everwild site. Confirm they read as *settings*, not locations.
- **Consent text:** deck reads "registered Canadian-exempt market dealer"; page keeps "registered Canadian exempt market dealer" (the regulatory term). Confirm with counsel.
- Fund ¶1 softened from "the ones that hold their value" to "the ones that last" — an unqualified value claim on a securities page.
- Dead copy: the unused prototype layouts (`index`, `split`, `route`, `tabs` behind `marketsLayout`) still say "four operating today". Not rendered; strip them in production.
- Team names/bios, stats, story milestones, email address remain placeholder per README.

### Lead form → HubSpot
- Submits to HubSpot Form 1 "Start your investment journey" (portal 343361068, form ce16b7d7-ed37-46dc-ac9f-398dd1f16a95) via the public Forms API. **Not yet tested with a real submission** — one test lead needed, then delete it in HubSpot.
- HubSpot form only has firstname / lastname / email / phone. **Province and investor type are not sent** — add matching fields in HubSpot, then list them in `HS_EXTRA` in `submitLead()`.
- HubSpot requires phone, so phone is now required on the page.
- HubSpot's own consent copy ("Basecamp Resorts") differs from the deck's; the page sends the deck consent text and maps the opt-in checkbox to subscription type 2973826333. Legal should confirm that mapping.
- Form 2 (bb5df2d0-…, name + email) is unused — likely a newsletter form.

### Licensing / assets
- Hero video is `Element Brand Video.mp4` (Troy's pick, 2026-10-20), full 30.7 s re-encoded to 540p (16 MB). Brand-section video is `Everwild 1920x1080.mp4`, re-encoded to 540p (7.9 MB). Confirm usage rights for web; the folder also holds Travel Alberta and third-party (Juan Pablo Cortes Duenez, JRNY Media) footage — each needs its own clearance. **Now in use:** JRNY Media / Danielle Eagleson stills (Image-75 behind Get in Touch under 80% charcoal, Image-14 swimmer behind Market at 6%, Image-66 under Investment), Photographer credit may be contractually required.
- Map renderings: Fernie (Pacific Render Studio), Harmony (Omega), Banff — credit lines may be required.
- Raw asset library `/assets/` (3.3 GB) is git-ignored. Never commit it.
- Mapbox token is public in source; add URL restrictions in the Mapbox account.

### Performance, unmeasured
- **Hero video is 16 MB and loads immediately** (`preload="auto"`, above the fold). Heaviest thing on the page; untested on mobile data. Options: trim to a 12–15 s loop (~7 MB), or serve the poster only below 760 px.
- Brand video 7.9 MB loads with `preload="metadata"` and plays only while in view; not profiled on mobile data. A 720p HEVC/WebM pair would be lighter — no ffmpeg on this machine.
- Map renderings 330–580 KB each, JPEG only; no WebP/AVIF, no responsive `srcset`.

### Accessibility
- **Settings panels** (2026-10-20, Troy): photo on every card, open or collapsed; panel colours removed; one black gradient, 50% at the bottom to 0 at the top; all type cream with a soft text-shadow. **Contrast is image-dependent and not AA-guaranteed** — weakest on the Coastal fog and the Prairie sky, where cream labels sit on near-white. Body copy in the open card sits in the darker lower half. If a client audit flags it, deepen the gradient's foot or give the copy block its own scrim.
- Hero black gradient: 0.3 at the bottom → 0 at the midpoint (Troy, 2026-10-20). Hero type now sits on near-bare video: over a white frame the intro reads ≈1.3–1.6:1 and the outlined "Learn More" button is faint; the filled "Request Details" button is unaffected. **The H1 sits above it** — 61% up the hero at 1440×900, 67% at 1280×720, 53% on mobile — so the headline is on bare video. Fine over the lake and peak frames; **weak (≈2:1) over the opening glacier frame, which is also the poster**, below the 3:1 large-text minimum. Poster swapped to the lake frame (3 s) on 2026-10-20, so slow loads no longer land on white; the glacier still returns each loop. Text-shadow / longer gradient deferred by Troy ("no worries on the text for now").
- Investment photo sits under 88% charcoal; stat text contrast is effectively unchanged. Market photo is at 10% on beige; charcoal text unaffected.
- Brand overlay deepened (0.86/0.76/0.55) so ivory body text holds ≥5.5:1 over a white frame wherever text sits; corners fall to 3:1 (no text there). Video is `aria-hidden`, muted, starts paused under `prefers-reduced-motion`, and plays only while in view. Pause/play button (44 px, bottom-right, labelled) added for WCAG 2.2.2 — resolved 2026-10-20.
- New Market section: charcoal on beige and forest eyebrow on beige — standard brand pairings; not separately audited.
- **Form field and investor-chip borders at 40% opacity** (Troy, 2026-10-20) — about 1.6:1 against the cream card, below the 3:1 WCAG 1.4.11 minimum for input boundaries. Fields still read as fields (white fill against cream, labels above), and the selected chip is solid forest. Client to accept, or go to ~80% to pass.
- Form error message uses `role="alert"`; colour #8A3B2E on cream not contrast-checked.

### Media requests not actioned
- In-development map galleries and team portraits — no imagery supplied.
- **Settings imagery — Unsplash License** (free commercial use, no attribution required; credit is courteous). Replaced the Everwild renderings/photos 2026-10-20 at Troy's request:
  - Urban — Toronto, ON (sunny, from the islands) — @hamednrg — unsplash.com/photos/noHMMrIbkAE — 2600 px; tower at 41% of frame, object-position 30% centres it in the open card
  - Coastal — Juan de Fuca, BC — @mattdren — unsplash.com/photos/rRwWXI_PeGg
  - Mountain — Banff, AB — @nunzg — unsplash.com/photos/BP0on2uI8bM
  - Forest — Algonquin Park, ON — @arianka — unsplash.com/photos/lJUPztX1SjI — 2300 px, 768 KB (busy texture; heaviest settings image)
  - Prairie — Canada (location unconfirmed) — @sanateddy — unsplash.com/photos/tO0HubKpo70
  Unsplash License bars selling the photos unaltered or using them to build a competing service; fine for this use. Stock, not Everwild properties — no captions imply otherwise.

### Reproducibility
- Renderings: `sips -s format jpeg -s formatOptions 72 -Z 1600`. Video: `avconvert --preset Preset960x540`; posters via `qlmanage -t -s 1280` (hero poster: `avconvert --start 3 --duration 1` from the source, then `qlmanage -t -s 1600`).
- Map coordinates for the three addresses geocoded with Mapbox Geocoding v6 (Lake Simcoe match confidence "medium"); Harmony uses South Harmony Drive, Rocky View County.
