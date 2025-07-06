# Emilien Breton

[613-913-9909](tel:+1-613-913-9909) • [mail@emilien.ca](mailto:mail@emilien.ca) • [github.com/Bricktech2000](https://github.com/Bricktech2000) • [linkedin.com/in/emilien-breton](https://www.linkedin.com/in/emilien-breton/) • [https://emilien.ca/](https://emilien.ca/)

## Experience

### EcoSafeSense

_Firmware Engineer_ `Ottawa | October 2024–Present`

- Writing firmware for ESP32-based air quality sensor and complementary test bench.

### Cohere

_Senior Data Quality Specialist — Advanced Mathematics_ `Freelance | October 2024–April 2025`

- Wrote, audited and corrected LLM prompts and responses with utmost attention to detail to produce **spotless training data** in formal logic, combinatorics, number theory,  graph theory and optimization.

## Projects

### [DFA Regex Engine](https://github.com/Bricktech2000/LTRE)

- Built [regex engine](https://github.com/Bricktech2000/LTRE/blob/master/ltre.c) in C99 that compiles regular expressions down to minimal deterministic finite automata to match input strings in **linear time** without backtracking.
- Wrote [extensive test suite](https://github.com/Bricktech2000/LTRE/blob/master/test.c) of over **400 tests** to ensure end-to-end correctness of engine and catch regressions.
- Developed [grep-like tool](https://github.com/Bricktech2000/LTRE/blob/master/ltrep.c) as real-world stress test for engine, achieving performance on par with GNU grep.

### [Breadboard Microcomputer](https://github.com/Bricktech2000/Atto-8)

- Designed 8-bit microcomputer from from logic gates upward, including [instruction set architecture](https://github.com/Bricktech2000/Atto-8/blob/master/spec/microarchitecture.md), [from-scratch assembler](https://github.com/Bricktech2000/Atto-8/tree/master/asm) and [cross-platform emulator in Rust](https://github.com/Bricktech2000/Atto-8/tree/master/emu), totaling over **20 000 SLOC** and **750 hours** of work.
- Wrote various utilities in Assembly running natively on microcomputer — [Wozmon-inspired memory monitor](https://github.com/Bricktech2000/Atto-8/blob/master/test/utils/attomon.asm) • [16×16 sprite editor](https://github.com/Bricktech2000/Atto-8/blob/master/test/utils/pixedit.asm) • [Tetris clone](https://github.com/Bricktech2000/Atto-8/blob/master/test/games/tetris.asm) • [native assembler](https://github.com/Bricktech2000/Atto-8/blob/master/test/utils/min-asm.asm) • [postfix notation calculator](https://github.com/Bricktech2000/Atto-8/blob/master/test/utils/calc.asm).
- Built microcomputer in hardware by hand-wiring discrete 74HC-series logic chips on breadboards.

### [Rudimentary C Compiler](https://github.com/Bricktech2000/Atto-8/blob/master/cc)

- Building C99 compiler from scratch in Rust targeting breadboard microcomputer’s instruction set.
- Implemented dead code elimination, constant folding and strength reduction, resulting in **20% increase** in generated code performance and **10% reduction** in binary size across test suite. 
- Developed extensive C standard library, including [heap allocator](https://github.com/Bricktech2000/Atto-8/blob/master/lib/stdlib.asm) supporting **malloc and free**, [string handling functions](https://github.com/Bricktech2000/Atto-8/blob/master/lib/string.asm) such as **strlen and memcpy** and [input/output routines](https://github.com/Bricktech2000/Atto-8/blob/master/lib/stdio.asm) including **getline and printf**. 

### [Multilayer Perceptron](https://github.com/Bricktech2000/Autodiff)

- Wrote [static reverse-mode automatic differentiation library](https://github.com/Bricktech2000/Autodiff/blob/master/lib/autodiff.c) in C99 for use in deep learning.
- Designed [multilayer perceptron model](https://github.com/Bricktech2000/Autodiff/blob/master/mlp-gen.c) and implemented [stochastic gradient descent](https://github.com/Bricktech2000/Autodiff/blob/master/mlp-fit.c), momentum and L2 regularization, achieving **97% accuracy** on MNIST database after 3 minutes training on 16 threads. 

## Volunteering

### [Computer Science Club](https://uocsclub.ca/)

_Club Executive_ `University of Ottawa | June 2022–Present`

- Running growing community of **over 1500** computer science students at the University of Ottawa.
- Collaborating with executive board to brainstorm, plan, fund and market monthly events and meetups, such as workshop on Vim bindings and mini-course on the λ-calculus.

### [Hack the Hill Hackathon](http://hackthehill.com/)

_Development Manager — Development Team_ `Ottawa | November 2022–October 2024`

- Led development of [open-source event management system](https://github.com/HacktheHill/track-the-hack) based on Next.js and Prisma and used by over **1000 hackers** and **50 organizers** throughout hackathon.
- Built and maintained internal payment portal powered by Stripe and React.js in collaboration with sponsorship team, enabling processing of over **20 000$**.

## Awards

- **uOCTF 2025** — 1st place `March 2025` 
- **uOttaHack 6** — 1st place, QNX challenge `January 2025` 
- **CS Games 2024** — 1st place, IOT challenge `March 2024` 
- **uOCTF 2024** — 1st place `November 2023` 
- **DeFi The Conventional** — 1st place, DeFi challenge `March 2022` 

## Skills

- **Languages** — C • Rust • Python • C++ • JavaScript • HTML/CSS • JSON • YAML • Markdown • LaTeX • Lua
- **Developer Tools** — GNU/Linux • Vim • Bash • Fish Shell • Git • GDB • GNU Make • Docker
- **Other Technologies** — React • Node.js • Express • Figma • Notion • Cloudflare • GitHub

`cd204e3c • Jul 2025`
