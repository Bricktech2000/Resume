# Emilien&nbsp;**Breton**

<!--          WARNING          -->
<!-- don't spam call me thanks -->
<!--        END WARNING        -->

[613-913-9909](tel:+1-613-913-9909)&nbsp;&bull; [mail@emilien.ca](mailto:mail@emilien.ca)&nbsp;&bull; [github.com/Bricktech2000](https://github.com/Bricktech2000)&nbsp;&bull; [linkedin.com/in/emilien-breton](https://www.linkedin.com/in/emilien-breton/)&nbsp;&bull; [https://emilien.ca/](https://emilien.ca/)

<!-- https://www.engineering.cornell.edu/sites/default/files/users/user240/Action%20Words%20for%20ENG%20(website).pdf -->

## Projects

### [Atto-8 Microcomputer](https://github.com/Bricktech2000/Atto-8)

_A minimalist 8-bit microcomputer with stack-based microprocessor_ `Rust&nbsp;&bull; C&nbsp;&bull; Assembly`

<!-- according to Toggl Track as of 2024-05-12 -->

<!-- according to https://codetabs.com/count-loc/count-loc-online.html -->

- Designed ecosystem of hardware and software from logic gates upward, including [instruction set architecture](https://github.com/Bricktech2000/Atto-8/blob/master/spec/microarchitecture.md), [from-scratch assembler](https://github.com/Bricktech2000/Atto-8/tree/master/asm) and [cross-platform emulator](https://github.com/Bricktech2000/Atto-8/tree/master/emu), totaling over **20&nbsp;000 SLOC** and **750 hours** of work.
- Wrote various demos in Assembly running natively on microcomputer &mdash; [Wozmon-inspired memory monitor](https://github.com/Bricktech2000/Atto-8/blob/master/test/utils/attomon.asm)&nbsp;&bull; [16&times;16 sprite editor](https://github.com/Bricktech2000/Atto-8/blob/master/test/utils/pixedit.asm)&nbsp;&bull; [Tetris clone](https://github.com/Bricktech2000/Atto-8/blob/master/test/games/tetris.asm)&nbsp;&bull; [native assembler](https://github.com/Bricktech2000/Atto-8/blob/master/test/utils/min-asm.asm)&nbsp;&bull; [postfix notation calculator](https://github.com/Bricktech2000/Atto-8/blob/master/test/utils/calc.asm).
- Built microcomputer in hardware by hand-wiring discrete 74HC-series logic chips on breadboards.

### Atto-8 C Compiler

_A rudimentary C99 compiler for the Atto-8 microarchitecture_ `Rust&nbsp;&bull; C&nbsp;&bull; Assembly`

- Building C99 compiler from sctatch in Rust targeting Atto-8 Assembly language, consisting of [preprocessor](https://github.com/Bricktech2000/Atto-8/blob/master/cc/preprocess.rs), [parser](https://github.com/Bricktech2000/Atto-8/blob/master/cc/parse.rs), [typechecker](https://github.com/Bricktech2000/Atto-8/blob/master/cc/typecheck.rs), [optimizer](https://github.com/Bricktech2000/Atto-8/blob/master/cc/optimize.rs) and [code generator](https://github.com/Bricktech2000/Atto-8/blob/master/cc/codegen.rs).
- Implemented dead code elimination, constant folding and strength reduction resulting in average of **20% increase** in generated code performance and **10% reduction** in binary size.
- Developed extensive C standard library, including [heap allocator](https://github.com/Bricktech2000/Atto-8/blob/master/lib/stdlib.asm) supporting **malloc and free**, [string handling functions](https://github.com/Bricktech2000/Atto-8/blob/master/lib/string.asm) such as **strlen and memcpy** and [input/output routines](https://github.com/Bricktech2000/Atto-8/blob/master/lib/stdio.asm) including **printf** supporting conversion specifiers %d, %u, %x, %c, %s and %p.

### [LTRE Regex Engine](https://github.com/Bricktech2000/LTRE)

_A fast regular expression library written in C99_ `C`

- Built [regex engine](https://github.com/Bricktech2000/LTRE/blob/master/ltre.c) in C99 which compiles regular expressions down to deterministic finite automata to match input strings in **linear time** without backtracking.
- Wrote [extensive test suite](https://github.com/Bricktech2000/LTRE/blob/master/test.c) of over **100 tests** to ensure end-to-end correctness of engine and catch regressions.
- Developed [grep-like tool](https://github.com/Bricktech2000/LTRE/blob/master/ltrep.c) supporting flags -v, -x, -i, -n and -c as real-world stress test for engine.

### [DBLess Password Manager](https://github.com/Bricktech2000/DBLess)

_A hash-based, database-less password manager_ `C&nbsp;&bull; Python`

- Devised [custom hash procedure](https://github.com/Bricktech2000/DBLess/blob/master/src/dbless.py) based on SHA-256 in Python which deterministically generates passwords on demand without requiring encryption or password storage.
- Reimplemented password generation algorithm in C along with [SHA-256 routines](https://github.com/Bricktech2000/DBLess/blob/master/src/sha256.c) as per FIPS PUB 180-4 for use as [interactive CLI tool](https://github.com/Bricktech2000/DBLess/blob/master/src/dbless.c).

<!-- - Built cross-platform PWA with Next.js used by over **50 accounts** <!-- 50 of which are mine that loads 2FA tokens, generates passwords and copies them to user's clipboard for convenience. -->

<!--
### [Personal Website](https://emilien.ca/)

_A portfolio for sharing various projects_ `Markdown&nbsp;&bull; Next.js`

- Designed and implemented appealing UI and optimized UX using Google Search Console resulting in over **15&nbsp;000 unique visitors** to portfolio website a month.
- Leveraged Cloudflare caching system and optimized site-wide accessibility resulting in Lighthouse score consistently over **95%**.
-->

<!--
### IB Personal Project

_Design and build of a racing drone_ `May 2020 &mdash; February 2021`

- Strategically put in place a dozen deadlines for the year-long project allowing for submission of [final report](https://docs.google.com/document/d/1IacnKTF84T8h3rhnu_9Y1yqm5nK6_kY3pc5PWw-RIvo/edit?usp=sharing) several days early.
- Designed project roadmap based on thorough understanding of possible complications resulting in only one major setback caused by defective parts.
-->

<!--
### [Legacy Protocol](https://devpost.com/software/legacy-protocol)

<!-- March 18th 2022 &mdash; March 20th 2022

_Submission for DeFi The Conventional 2022_ `React&nbsp;&bull; Rust`

- Won **first place** in Finance category of Canada's largest DeFi hackathon along with **2500&dollar; prize** as part of 3-member team.
- Engineered [MVP smart contract backend and API](https://github.com/Bricktech2000/crypto_will) from scratch in Rust with no prior experience in Web3, all within limited **36-hour timeframe**.
- Worked in collaboration with Terraform Labs post-hackathon to officialize our protocol and secure additional funding prior to Terra Luna collapse.
-->

<!--
### AI Image Compressor

_A neural network that learns to compress images_ `Python&nbsp;&bull; Tensorflow&nbsp;&bull; Keras`

- Implemented web scraper and image preprocessor optimized with numpy to generate millions of training samples in less than 5 minutes.
- Created and implemented custom algorithm within autoencoder structure to allow for variable compression ratio with no overhead.
- Supervised training process and tweaked settings leading to results of superior quality than JPEG compression when in favorable circumstances.
-->

## Volunteering

### [Hack the Hill Hackathon](http://hackthehill.com/)

<!-- according to Code, Coffee & Cram collab on 2022-10-30 -->

<!-- Development Coordinator was updated to Development Manager around 2023-05-01 -->

<!--
_Development Manager &mdash; Development Team_ `Ottawa&ensp;|&ensp;May 2023 &mdash; Present`
_Development Coordinator &mdash; Development Team_ `Ottawa&ensp;|&ensp;November 2022 &mdash; May 2023`
-->

_Development Manager &mdash; Development Team_ `Ottawa&ensp;|&ensp;November 2022 &mdash; Present`

<!-- according to https://prisma.hackthehill.com/ -->

<!-- according to "Hack the Hill I Budget" spreadsheet (actual number is 21699.32$) -->

- Leading development of [open-source participant tracker](https://github.com/HacktheHill/track-the-hack) built with Next.js and Prisma, used by over **1000 hackers** and **50 organizers** throughout hackathon.
- Built and maintained internal sporsorship payment portal powered by Stripe and React.js in collaboration with sponsorship team, enabling processing of over **20 000&dollar;**.

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

### [uOttawa Computer Science Club](https://uocsclub.ca/)

<!-- May 29 2022 20:57 according to CS Discord Jedi -->

<!--
- got Manaal involved to take care of social media and photography
- updated outdated information on website
- ported logo from raster to vector
- refreshed Discord server with clearer roles and introduction
- Designed internal Notion workspace, improving short-term planning by providing single central platform to capture meeting minutes and track task progress.
- Reorganized Discord server of over **1000 members** by creating clearer roles and introduction channels, improving user experience and onboarding.
-->

<!-- 1147 members on Discord server as of 2023-11-10 19:08 -->

_Club Executive_ `University of Ottawa&ensp;|&ensp;June 2022 &mdash; Present`

- Building community of **over 1000** computer science students at the University of Ottawa.
- Collaborated with executive board to brainstorm, organize and schedule a dozen events by designing marketing material with Figma and hosting workshops for <!-- generous cumulative estimation --> over **100 students**.

<!--
### Group Chat Moderator

_Course-specific Discord server creator, owner and moderator_ `University of Ottawa`

161 (ITI1121 A, 2022-04-11) + 424 (ITI1100 A/B, 2022-04-11) + 111 (MAT1320, 2022-12-22) = 696
222 (SEG2105, 2022-10-30) + 230 (CSI2110, 2022-12-22) + 179 (CEG2136, 2022-12-22) = 631
696 + 631 = 1327 in total

- Built and promoted six Discord servers allowing total of over **1000 students** to communicate with their peers and share course resources easily.
- Improved moderation experience by creating [Discord bot](https://github.com/Bricktech2000/Turing-Complete-Mentions) to address groups of students based on specific criteria, extending flexibility of Discord mentions.
-->

## Experience

### Zeptile Software

<!-- start date according to Discord conversations. end date estimated -->

_Software Engineer &mdash; Web3_ `Remote&ensp;|&ensp;October 2022 &mdash; October 2023`

- Implemented various smart contracts in Solidity and ensured **100% test coverage** through Chai and Hardhat.

## Education

### University of Ottawa

_BSc with Honours in Computer Science_ `September 2021 &mdash; Present`

- Admission scholarship &mdash; 95%+ average. `November 2020`

<!--
### Polyvalente Saint-Francois

_IB Middle Years Programme, Secondary School Diploma_ `September 2016 &mdash; June 2021`
-->

## Skills

- **Languages** &ensp; C&nbsp;&bull; Rust&nbsp;&bull; Python&nbsp;&bull; JavaScript&nbsp;&bull; HTML/CSS&nbsp;&bull; JSON&nbsp;&bull; YAML&nbsp;&bull; Markdown&nbsp;&bull; LaTeX&nbsp;&bull; Lua&nbsp;&bull; C++
- **Developer Tools** &ensp; GNU/Linux&nbsp;&bull; Vim&nbsp;&bull; Bash&nbsp;&bull; Fish Shell&nbsp;&bull; Git&nbsp;&bull; GDB&nbsp;&bull; GNU Make&nbsp;&bull; Docker
- **Other Technologies** &ensp; React&nbsp;&bull; Node.js&nbsp;&bull; Express&nbsp;&bull; Figma&nbsp;&bull; Notion&nbsp;&bull; Cloudflare&nbsp;&bull; GitHub

<!--
### Spoken Languages

<!-- https://csb.uncw.edu/cen/docs/determining%20language%20proficiency.pdf
<!-- https://corporatefinanceinstitute.com/resources/careers/resume/language-proficiency-levels/

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

<!-- _[Bricktech2000/Resume](https://github.com/Bricktech2000/Resume/)_ `Commit [COMMIT_HASH]&nbsp;&bull; [MONTH] [YEAR]` -->
