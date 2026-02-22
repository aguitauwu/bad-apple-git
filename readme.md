# Bad Apple!! in git commit history

Every frame of Bad Apple!! is stored as a git commit.
The repository has 2,170 commits — one per frame.
The video lives in the commit history, not in the files.

## Watch it

### Version 1 — git only (no dependencies)

```bash
git clone https://github.com/aguitauwu/bad-apple-git
cd bad-apple-git
git log --reverse --pretty=format:"%H" > ~/hashes.txt
while read h; do clear; git --no-pager show "${h}:frame.txt"; sleep 0.1; done < ~/hashes.txt
```

### Version 2 — with colors (requires Python)

Red = dark pixels. Green = light pixels. Exactly like a git diff.

```bash
git clone https://github.com/aguitauwu/bad-apple-git
cd bad-apple-git
git log --reverse --pretty=format:"%H" > ~/hashes.txt
while read h; do clear; git --no-pager show "${h}:frame.txt" | python3 render.py; sleep 0.1; done < ~/hashes.txt
```

## How it works

Each commit modifies a single file `frame.txt` with the next frame of the video.
The ASCII art was sourced from [Chion82/ASCII_bad_apple](https://github.com/Chion82/ASCII_bad_apple).

## License

MIT — aguitauwu
