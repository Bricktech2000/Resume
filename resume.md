# Emilien Breton

[613-913-9909](tel:+1-613-913-9909) • [mail@emilien.ca](mailto:mail@emilien.ca) • [github.com/Bricktech2000](https://github.com/Bricktech2000) • [linkedin.com/in/emilien-breton](https://www.linkedin.com/in/emilien-breton/) • [https://emilien.ca/](https://emilien.ca/)

<!-- https://www.engineering.cornell.edu/sites/default/files/departments/career%20services/Action-Words-for-ENG-2016.pdf -->

<!-- https://practicaltypography.com/resumes.html -->

## Experience

### EcoSafeSense

<!-- first meeting with Olga was 2024-10-16 -->

<!--
- wrote test bench firmware
- soldered together sensors using hot air rework station
- oversaw sensor installation
-->

_Firmware Engineer_ `Ottawa | October 2024–Present`

- Writing firmware for ESP32-based air quality sensor and complementary test bench.

### Cohere

<!-- contractor agreement signed 2024-10-28 -->

_Senior Data Quality Specialist — Advanced Mathematics_ `Freelance | October 2024–Present`

- Writing, auditing and correcting LLM prompts and responses with utmost attention to detail to produce **spotless training data** in formal logic, combinatorics, number theory, <!-- group theory, --> graph theory and optimization.

<!--
### Zeptile Software

<! -- start date according to Discord conversations. end date estimated -- >

_Software Engineer — Web3_ `Remote | October 2022–October 2023`

- Implemented various smart contracts in Solidity and ensured **100% test coverage** through Chai and Hardhat.
-->

## Projects

### [LTRE Regex Engine](https://github.com/Bricktech2000/LTRE)

_A fast regular expression library written in C99_ `C`

- Built [regex engine](https://github.com/Bricktech2000/LTRE/blob/master/ltre.c) in C99 that compiles regular expressions down to minimal deterministic finite automata to match input strings in **linear time** without backtracking.
- Wrote [extensive test suite](https://github.com/Bricktech2000/LTRE/blob/master/test.c) of over **400 tests** to ensure end-to-end correctness of engine and catch regressions.
- Developed [grep-like tool](https://github.com/Bricktech2000/LTRE/blob/master/ltrep.c) as real-world stress test for engine, achieving performance on par with GNU grep.

<!--
- Developed [grep-like tool](https://github.com/Bricktech2000/LTRE/blob/master/ltrep.c) supporting flags -v, -x/-p, -i/-s, -S, -F, -n/-N, -H/-I and -c as real-world stress test for engine.
- Developed [grep-like tool](https://github.com/Bricktech2000/LTRE/blob/master/ltrep.c) as real-world stress test for engine, with command-line options for case-insensitive and smart-case matching, fixed-string patterns, full-match and partial-match searches, and more.
-->

### [Atto-8 Microcomputer](https://github.com/Bricktech2000/Atto-8)

_A minimalist 8-bit microcomputer with stack-based microprocessor_ `Rust • C • Assembly`

<!-- according to Toggl Track as of 2024-05-12 -->

<!-- according to https://codetabs.com/count-loc/count-loc-online.html -->

- Designed entire microcomputer from from logic gates upward, including [instruction set architecture](https://github.com/Bricktech2000/Atto-8/blob/master/spec/microarchitecture.md), [from-scratch assembler](https://github.com/Bricktech2000/Atto-8/tree/master/asm) and [cross-platform emulator](https://github.com/Bricktech2000/Atto-8/tree/master/emu), totaling over **20 000 SLOC** and **750 hours** of work.
- Wrote various utilities in Assembly running natively on microcomputer — [Wozmon-inspired memory monitor](https://github.com/Bricktech2000/Atto-8/blob/master/test/utils/attomon.asm) • [16×16 sprite editor](https://github.com/Bricktech2000/Atto-8/blob/master/test/utils/pixedit.asm) • [Tetris clone](https://github.com/Bricktech2000/Atto-8/blob/master/test/games/tetris.asm) • [native assembler](https://github.com/Bricktech2000/Atto-8/blob/master/test/utils/min-asm.asm) • [postfix notation calculator](https://github.com/Bricktech2000/Atto-8/blob/master/test/utils/calc.asm).
- Built microcomputer in hardware by hand-wiring discrete 74HC-series logic chips on breadboards.

### [Atto-8 C Compiler](https://github.com/Bricktech2000/Atto-8/blob/master/cc)

_A rudimentary C99 compiler for the Atto-8 microarchitecture_ `Rust • C • Assembly`

- Building C99 compiler from scratch in Rust targeting Atto-8 Assembly language.
- Implemented dead code elimination, constant folding and strength reduction, resulting in **20% increase** in generated code performance and **10% reduction** in binary size across test suite.
- Developed extensive C standard library, including [heap allocator](https://github.com/Bricktech2000/Atto-8/blob/master/lib/stdlib.asm) supporting **malloc and free**, [string handling functions](https://github.com/Bricktech2000/Atto-8/blob/master/lib/string.asm) such as **strlen and memcpy** and [input/output routines](https://github.com/Bricktech2000/Atto-8/blob/master/lib/stdio.asm) including **getline and printf**. <!-- supporting conversion specifiers %d, %u, %x, %c, %s and %p -->

<!--
### [DBLess Password Manager](https://github.com/Bricktech2000/DBLess)

_A hash-based, database-less password manager_ `C • Python`

- Devised [custom hash procedure](https://github.com/Bricktech2000/DBLess/blob/master/src/dbless.py) based on SHA-256 in Python which deterministically generates passwords on demand without requiring encryption or password storage.
- Reimplemented password generation algorithm in C along with [SHA-256 routines](https://github.com/Bricktech2000/DBLess/blob/master/src/sha256.c) as per FIPS PUB 180-4 for use as [interactive CLI tool](https://github.com/Bricktech2000/DBLess/blob/master/src/dbless.c).

- Built cross-platform PWA with Next.js used by over **50 accounts** <! -- 50 of which are mine -- > that loads 2FA tokens, generates passwords and copies them to user’s clipboard for convenience.
-->

<!--
### [Personal Website](https://emilien.ca/)

_A portfolio for sharing various projects_ `Markdown • Next.js`

- Designed and implemented appealing UI and optimized UX using Google Search Console resulting in over **15 000 unique visitors** to portfolio website a month.
- Leveraged Cloudflare caching system and optimized site-wide accessibility resulting in Lighthouse score consistently over **95%**.
-->

<!--
### [Legacy Protocol](https://devpost.com/software/legacy-protocol)

<! -- March 18th 2022–March 20th 2022 -- >

_Submission for DeFi The Conventional 2022_ `React • Rust`

- Won **first place** in Finance category of Canada’s largest DeFi hackathon along with **2500$ prize** as part of 3-member team.
- Engineered [MVP smart contract backend and API](https://github.com/Bricktech2000/crypto_will) from scratch in Rust with no prior experience in Web3, all within limited **36-hour timeframe**.
- Worked in collaboration with Terraform Labs post-hackathon to officialize our protocol and secure additional funding prior to Terra Luna collapse.
-->

## Volunteering

### [Computer Science Club](https://uocsclub.ca/)

<!-- May 29 2022 20:57 according to CS Discord Jedi -->

<!--
- got Manaal involved to take care of social media and photography
- updated outdated information on website
- ported logo from raster to vector
- refreshed Discord server with clearer roles and introduction
- Designed internal Notion workspace, improving short-term planning by providing single central platform to capture meeting minutes and track task progress.
- Reorganized Discord server of over **1000 members** by creating clearer roles and introduction channels, improving user experience and onboarding.
- hosted talk on the practicality of the lambda-calculus
-->

<!-- 1306 members on Discord server as of 2024-11-23 03:03 -->

_Club Executive_ `University of Ottawa | June 2022–Present`

- Running growing community of **over 1000** computer science students at the University of Ottawa.
- Collaborating with executive board to brainstorm, plan, fund and market monthly events and meetups, such as workshop on Vim bindings and mini-course on the λ-calculus.

### [Hack the Hill Hackathon](http://hackthehill.com/)

<!-- according to Code, Coffee & Cram collab on 2022-10-30 -->

<!-- Development Coordinator was updated to Development Manager around 2023-05-01 -->

<!--
_Development Manager — Development Team_ `Ottawa | May 2023–October 2024`
_Development Coordinator — Development Team_ `Ottawa | November 2022–May 2023`
-->

_Development Manager — Development Team_ `Ottawa | November 2022–October 2024`

<!-- according to https://prisma.hackthehill.com/ -->

<!-- according to "Hack the Hill I Budget" spreadsheet (actual number is 21699.32$) -->

- Led development of [open-source event management system](https://github.com/HacktheHill/track-the-hack) built with Next.js and Prisma and used by over **1000 hackers** and **50 organizers** throughout hackathon.
- Built and maintained internal sporsorship payment portal powered by Stripe and React.js in collaboration with sponsorship team, enabling processing of over **20 000$**.

<!--
- Collaborated with design, development and community teams to fix various issues on [hackathon website](https://hackthehill.com/) and keep it up to date with event information
- worked on website to fix issues
- worked on sponsorship portal with stripe
- worked on display system with firebase
- created CONTRIBUTING.md on .github repo for conventions. helped set up branch protection. figured out what merge strategy would be best
- fixed missing DNS CNAME record on cloudflare
- deployed hacker tracker on Vercel
- brainstormed backend workshop ideas to land on discord bot workshop
- worked on database schema for hacker tracker, implementing `hackers/hacker?id` endpoint
- learned basics of SQL to build queries for hacker tracker
-->

## Awards

- **uOttaHack 6** — 1st place QNX challenge `January 2025` <!-- January 17th 2024—January 19th 2024 -->
- **CS Games 2024** — 1st place IOT challenge `March 2024` <!-- March 15th 2024—March 17th 2024 -->
- **DeFi The Conventional** — 1st place DeFi challenge `March 2022` <!-- March 18th 2022–March 20th 2022 -->

## Skills

- **Languages** — C • Rust • Python • JavaScript • HTML/CSS • JSON • YAML • Markdown • LaTeX • Lua • C++
- **Developer Tools** — GNU/Linux • Vim • Bash • Fish Shell • Git • GDB • GNU Make • Docker
- **Other Technologies** — React • Node.js • Express • Figma • Notion • Cloudflare • GitHub

<!--
### Spoken Languages

<! -- https://csb.uncw.edu/cen/docs/determining%20language%20proficiency.pdf -- >
<! -- https://corporatefinanceinstitute.com/resources/careers/resume/language-proficiency-levels/ -- >

- French `Native`
- English `Native`
- Spanish `Intermediate`
- Russian `Elementary`
-->

<!--
## Achievements

### Fusce Sed Erat Velit

- Sed euismod diam sit amet euismod.

### Iaculis Vehicula Felis

- Aliquam ornare diam sit amet euismod pellentesque.
- In condimentum tortor non odio consectetur accumsan.
-->

<!-- _[Bricktech2000/Resume](https://github.com/Bricktech2000/Resume/)_ `Commit [COMMIT_HASH] • [MONTH] [YEAR]` -->
