# Emilien **Breton**

---

## Projects

### [Atto-8 Microcomputer](https://github.com/Bricktech2000/Atto-8)

_A minimalist 8-bit microcomputer with stack-based microprocessor_ `Rust • C • Assembly`

- Designed ecosystem of hardware and software from logic gates upward, including [instruction set architecture](https://github.com/Bricktech2000/Atto-8/blob/master/spec/microarchitecture.md), [from-scratch assembler](https://github.com/Bricktech2000/Atto-8/tree/master/asm) and [cross-platform emulator](https://github.com/Bricktech2000/Atto-8/tree/master/emu), totaling over **20 000 SLOC** and **750 hours** of work.
- Wrote various demos in Assembly running natively on microcomputer — [memory monitor](https://github.com/Bricktech2000/Atto-8/blob/master/test/utils/attomon.asm) • [sprite editor](https://github.com/Bricktech2000/Atto-8/blob/master/test/utils/pixedit.asm) • [Tetris clone](https://github.com/Bricktech2000/Atto-8/blob/master/test/games/tetris.asm) • [native assembler](https://github.com/Bricktech2000/Atto-8/blob/master/test/utils/min-asm.asm) • [postfix notation calculator](https://github.com/Bricktech2000/Atto-8/blob/master/test/utils/calc.asm).
- Built microcomputer in hardware using discrete 74HC-series logic chips on breadboards.

### Atto-8 C Compiler

_A rudimentary C99 compiler for the Atto-8 microarchitecture_ `Rust • C • Assembly`

- Building C99 compiler from sctatch in Rust targeting Atto-8 Assembly language, consisting of [preprocessor](https://github.com/Bricktech2000/Atto-8/blob/master/cc/preprocess.rs), [parser](https://github.com/Bricktech2000/Atto-8/blob/master/cc/parse.rs), [typechecker](https://github.com/Bricktech2000/Atto-8/blob/master/cc/typecheck.rs), [optimizer](https://github.com/Bricktech2000/Atto-8/blob/master/cc/optimize.rs) and [code generator](https://github.com/Bricktech2000/Atto-8/blob/master/cc/codegen.rs).
- Implemented dead code elimination, constant folding and strength reduction resulting in average of **20% increase** in execution speed and **10% reduction** in binary size.
- Developed extensive C standard library, including [heap allocator](https://github.com/Bricktech2000/Atto-8/blob/master/lib/stdlib.asm) supporting **malloc and free**, [string handling functions](https://github.com/Bricktech2000/Atto-8/blob/master/lib/string.asm) such as **strlen and memcpy** and [input/output routines](https://github.com/Bricktech2000/Atto-8/blob/master/lib/stdio.asm) including **printf** supporting conversion specifiers %d, %u, %x, %c, %s and %p.

### [LTRE Regex Engine](https://github.com/Bricktech2000/LTRE)

_A fast regular expression library written in C99_ `C`

- Built [regex engine](https://github.com/Bricktech2000/LTRE/blob/master/ltre.c) in C99 which compiles regular expressions down to deterministic finite automata to match input strings in **linear time** without backtracking.
- Wrote [extensive test suite](https://github.com/Bricktech2000/LTRE/blob/master/test.c) of over **100 tests** to ensure end-to-end correctness of engine.
- Developed [grep-like tool](https://github.com/Bricktech2000/LTRE/blob/master/ltrep.c) supporting flags -v, -x, -i, -n and -c as real-world stress test for engine.

### [DBLess Password Manager](https://github.com/Bricktech2000/DBLess)

_A hash-based, database-less password manager_ `C • Python`

- Devised [custom hash procedure](https://github.com/Bricktech2000/DBLess/blob/master/src/dbless.py) based on SHA-256 in Python which deterministically generates passwords on demand without requiring encryption or password storage.
- Reimplemented password generation algorithm in C along with [SHA-256 routines](https://github.com/Bricktech2000/DBLess/blob/master/src/sha256.c) as per FIPS PUB 180-4 for use as [interactive CLI tool](https://github.com/Bricktech2000/DBLess/blob/master/src/dbless.c).

## Volunteering

### [Hack the Hill Hackathon](http://hackthehill.com/)

_Development Manager — Development Team_ `Ottawa  |  November 2022 — Present`

- Leading development of [open-source participant tracker](https://github.com/HacktheHill/track-the-hack) built with Next.js and Prisma, used by over **1000 hackers** and **50 organizers** throughout hackathon.
- Built and maintained internal sporsorship payment portal powered by Stripe and React.js in collaboration with sponsorship team, enabling processing of over **20 000$**.

### [uOttawa Computer Science Club](https://uocsclub.ca/)

_Club Executive_ `University of Ottawa  |  June 2022 — Present`

- Building community of **over 1000** computer science students at the University of Ottawa.
- Collaborated with executive board to brainstorm, organize and schedule a dozen events by designing marketing material with Figma and hosting workshops for  over **100 students**.

## Experience

### Zeptile Software

_Software Engineer — Web3_ `Remote  |  October 2022 — October 2023`

- Implemented various smart contracts in Solidity as per specification and ensured **100% test coverage** through Chai and Hardhat.

## Education

### University of Ottawa

_BSc with Honours in Computer Science_ `September 2021 — Present`

- Admission scholarship — 95%+ average. `November 2020`

---

## Skills

### Languages

Rust • C • Python • JavaScript

### Development Tools

NixOS • Neovim • Fish Shell • Git

### Other Technologies

React • Node.js • HTML • CSS • JSON • YAML • Markdown • LaTeX • Lua • x86 Assembly • C++ • Bash • GDB • Linux • Arduino • VS Code • Figma • Notion • Docker • Cloudflare • GitHub

### Spoken Languages


- French `Native`
- English `Native`
- Spanish `Intermediate`
- Russian `Elementary`

### Other Interests

Electronics • Robotics • CAD • 3D Printing • Finance • Mathematics • Drone Building • Music • Bouldering

## Contact

[Ottawa, Ontario](https://google.com/maps/place/Ottawa,+ON)



[613-913-9909](tel:+1-613-913-9909)

[mail@emilien.ca](mailto:mail@emilien.ca)

[https://emilien.ca/](https://emilien.ca/)

[**github/** Bricktech2000](https://github.com/Bricktech2000)

[**linkedin/** emilien-breton](https://www.linkedin.com/in/emilien-breton/)

---

_[Bricktech2000/Resume](https://github.com/Bricktech2000/Resume/)_ `Commit 3ea7e0d • Jun 2024`
