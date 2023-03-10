# Emilien **Breton**

---

## Experience

### [Hack the Hill](http://hackthehill.com/)

`Development Coordinator &mdash; Development Team` _University of Ottawa&nbsp;&bull; November 2022 &mdash; Present_

### Zeptile Software

`Software Engineer &mdash; Web3` _Remote from Ottawa&nbsp;&bull; October 2022 &mdash; Present_

### [uOttawa CS Club](https://uocsclub.ca/)

`Club Executive` _University of Ottawa&nbsp;&bull; June 2022 &mdash; Present_

- Collaborated with two other executives to brainstorm, organize and schedule a dozen small-scale events in Ottawa by giving talks and organizing workshops for over 100 students
- Designed internal Notion workspace, improving short-term planning by providing single central platform to capture meeting minutes and track task progress

## Projects

### [Personal Website](https://emilien.ca/)

`A portfolio for sharing various projects`
_JavaScript&nbsp;&bull; HTML&nbsp;&bull; CSS&nbsp;&bull; Markdown&nbsp;&bull; Next.js_

- Designed and implemented appealing UI and optimized UX using Google Search Console resulting in over 5000 unique visitors a month
- Leveraged Cloudflare caching system and optimized site-wide accessibility resulting in Lighthouse score consistently over 95%

### [Stack-Based CPU](https://github.com/Bricktech2000/Stack-Based-CPU)

`An assembler and emulator for a custom stack-based CPU architecture`
_Rust&nbsp;&bull; Assembly_

- Designed and implemented stack-based emulator in Rust that supports 44 CPU instructions and graphics through 32x32 grayscale display buffer
- Developed basic assembler to resolve labels and convert Assembly source files into custom binary machine code
- Proved custom instruction set Turing complete through [implementation of Conway's Game of Life](https://github.com/Bricktech2000/Stack-Based-CPU/blob/master/src/tests/test15.asm) from scratch in Assembly language

### [DBLess Password Manager](https://dbless.emilien.ca/)

`A hash-based, database-less password manager`
_Python&nbsp;&bull; JavaScript&nbsp;&bull; HTML&nbsp;&bull; CSS&nbsp;&bull; Next.js_

- Devised [custom cryptographic procedure](https://github.com/Bricktech2000/DBLess-Password-Manager/blob/master/web/lib/generatePassword.js) based on SHA-256 to deterministically generate passwords on demand instead of encrypting them
- Built [cross-platform PWA](https://dbless.emilien.ca/) with Next.js that loads 2FA tokens, generates passwords and copies them to user's clipboard for convenience

### [Legacy Protocol](https://devpost.com/software/legacy-protocol)

`Submission for DeFi The Conventional 2022`
_March 2022&nbsp;&bull; JavaScript&nbsp;&bull; React&nbsp;&bull; Rust_

- Won first place in Finance category of Canada's largest DeFi hackathon along with 2500\$ prize as part of 3-member team
- Built [MVP smart contract backend](https://github.com/Bricktech2000/crypto_will) from scratch in Rust with no prior experience in Web3, all within tight 36-hour timeframe
- Collaborated with Terraform Labs to officialize our protocol and secure additional funding prior to Terra Luna collapse

### More on [GitHub](https://github.com/Bricktech2000) and in [Portfolio](https://emilien.ca/)

## Education

### University of Ottawa

`BSc with Honours in Computer Science` _Dropped out after first year_

- Admission scholarship &mdash; 95%+ average _November 2020_

---

## Contact

[Ottawa, Ontario](https://maps.google.com/place/Ottawa,+ON)

[613-913-9909](tel:+1-613-913-9909)

[mail@emilien.ca](mailto:mail@emilien.ca)

[https://emilien.ca/](https://emilien.ca/)

[**github/** Bricktech2000](https://github.com/Bricktech2000)

[**linkedin/in/** emilien-breton](https://www.linkedin.com/in/emilien-breton/)

## Skills

### Programming Languages

Python&nbsp;&bull; JavaScript&nbsp;&bull; Rust&nbsp;&bull; C++

### Development Tools

Linux&nbsp;&bull; Neovim&nbsp;&bull; Git&nbsp;&bull; GitHub&nbsp;&bull; Docker

### Frameworks

React&nbsp;&bull; Node.js&nbsp;&bull; Next.js&nbsp;&bull; Express.js

### Other Technologies

HTML&nbsp;&bull; CSS&nbsp;&bull; JSON&nbsp;&bull; YAML&nbsp;&bull; Markdown&nbsp;&bull; LaTeX&nbsp;&bull; C&nbsp;&bull; Assembly&nbsp;&bull; Raspberry Pi&nbsp;&bull; Arduino&nbsp;&bull; VS Code&nbsp;&bull; Figma&nbsp;&bull; Notion&nbsp;&bull; Cloudflare

## Other

### Languages

French _Native_

English _Native_

Spanish _Intermediate_

Russian _Elementary_

### Interests

Electronics&nbsp;&bull; [Robotics](https://emilien.ca/Spider-Robot/)&nbsp;&bull; 3D Printing&nbsp;&bull; Mathematics&nbsp;&bull; [Drone Building](https://emilien.ca/FPV-Racing-Drone/)&nbsp;&bull; Finance & Investing&nbsp;&bull; [Productivity](https://notes.emilien.ca/productivity/)&nbsp;&bull; Music

---

[`Bricktech2000/Resume`](https://github.com/Bricktech2000/Resume/) <em class="time"></em>

<script>
  // https://stackoverflow.com/questions/45726013/how-can-i-get-last-commit-from-github-api
  // https://api.github.com/users/Bricktech2000/events/public
  // https://api.github.com/repos/Bricktech2000/Resume
  // https://api.github.com/repos/Bricktech2000/Resume/commits
  (async () => {
    const latestCommitHash = (
      await (
        await fetch(
          'https://api.github.com/repos/Bricktech2000/Resume/commits'
        )
      ).json()
    )[0].sha.slice(0, 15);

    const currentMonthYear = new Date().toLocaleString('default', {
      month: 'long',
      year: 'numeric',
    });

    document.querySelector('.time').innerHTML =
      currentMonthYear + '&nbsp;&bull;&nbsp;' + latestCommitHash;
  })();
</script>
