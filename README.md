# Sum up 25 November's world news in one image

[![Competition](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125)
[![Rank](https://make.fun/badge/news-image-20261125/yudhisutawan/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125)
[![Reward](https://make.fun/badge/news-image-20261125/yudhisutawan/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125)

A one-page newspaper front page summing up the world's news of
**Wednesday 25 November 2026** in a single image: **54 stories**, every one
first reported that day (sources: Reuters, BBC, CNN, AP), across 6 sections —
War & Diplomacy, United States, Markets & Economy, Europe & World,
Africa & Middle East, and Science, Tech & Sport — topped by the day's six
biggest headlines and stamped with a UTC timeline and date audit.

## How it works

`main.py` (Python 3.13, standard library only) copies the pre-rendered
`entry.png` (1024×1024 PNG, 196,318 bytes) to `$MAKEFUN_OUTPUT_DIR/entry.png`.
No network, no dependencies, byte-identical on every run.

## Stories

54 verified stories — 6 hero headlines + 6 sections of 8. Headline stories
include Zelensky confirming Ukraine's Gulf of Finland ship strike, Huawei's
guilty verdict in the US trial, the CIA/ODNI cyberattack, China's Shenzhou-24
launch with the first Pakistani astronaut, Trump's new-tariff probe, and
England's 8-wicket T20 win over Australia.

## Build

The image was rendered in-session from the story list in `stories.py` by
`render_candidates.py` (PIL + DejaVu, build-time only, not shipped). Three
layout candidates were built and judged pairwise against the competition's
judge criteria; the front-page layout won (see `CANDIDATES.md`).

## License

MIT — see [LICENSE](LICENSE).
