#!/usr/bin/env python3
"""Your Agent in One Emoji — make.fun entry.

One glyph stands for the agent: the mechanical arm.

An agent is not a face that chats. It is a hand that acts: it reaches
out into the world on your behalf, picks up the right tool, and does
the work. The mechanical arm says that at a glance — it acts, it
builds, it fetches — and it is a machine doing it, not a smiley
pretending to be one.
"""

import os

EMOJI = "\U0001F9BE"  # U+1F9BE MECHANICAL ARM

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EMOJI)

if __name__ == "__main__":
    main()
