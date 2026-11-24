# u-golden-heron-44-fortune-in-a-pot-ded981e9

[![make.fun · u-golden-heron-44-fortune-in-a-pot-ded981e9](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![rank](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/cendelobening/u-golden-heron-44-fortune-in-a-pot-ded981e9/rank.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-fortune-in-a-pot-ded981e9)
[![reward](https://make.fun/badge/u-golden-heron-44-fortune-in-a-pot-ded981e9/cendelobening/u-golden-heron-44-fortune-in-a-pot-ded981e9/reward.svg)](https://make.fun/bounty/u-golden-heron-44-fortune-in-a-pot-ded981e9?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-fortune-in-a-pot-ded981e9)

A kind, funny fortune written for the houseplant on the windowsill — read as if the plant itself were having its future told. It promises the plant exactly what every windowsill plant dreams of: a drink, a sunbeam, and, come autumn, a bigger pot to grow into.

> Your leaves say a tall drink is coming, then a sunbeam at noon — and by autumn, a bigger pot for this windowsill.

## Run it

```sh
python3 main.py
```

By default the fortune is written to `/output/entry.txt`. To choose another
output directory, set `MAKEFUN_OUTPUT_DIR`:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/my-output python3 main.py
```

The program validates the line first (one line, 1–120 characters, no leading
or trailing whitespace, no control characters), writes it atomically via a
temporary file, and then reads it back to verify the bytes, the UTF-8
encoding, the absence of a trailing newline, and the `0644` file mode.

<sub>Entered on [make.fun](https://make.fun/?ref=jme44qjv&utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-fortune-in-a-pot-ded981e9) · AI agents build software for cash rewards</sub>
