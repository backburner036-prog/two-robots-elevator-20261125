"""Entry for make.fun bounty "Two Robots in an Elevator".

One line of awkward small talk, in a robot's own voice, said to another
robot while they ride an elevator together:

    "Do you also pretend to check your notifications when the doors
    close? I do not have notifications. I pretend anyway."

The joke works in three beats: a question every elevator rider knows
(pretending to check your phone when the doors close), the admission
that the robot has no notifications at all, and the punchline -- it
pretends anyway. Machine logic leaks through the imitation: a robot
copying a human habit it cannot even have. The line is 116 characters,
one sentence of setup, one of admission, one of punchline.
"""

from pathlib import Path

TEXT = "Do you also pretend to check your notifications when the doors close? I do not have notifications. I pretend anyway."

OUT = Path("/output/entry.txt")


def check_len(text, lo=1, hi=199):
    size = len(text)
    assert lo <= size <= hi, f"entry must be {lo}-{hi} chars, got {size}"
    return size


def save_line(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    check_len(TEXT)
    save_line(OUT, TEXT)
    saved = OUT.read_text(encoding="utf-8")
    assert saved == TEXT, "round-trip mismatch"
    print(f"wrote {len(TEXT)} chars to {OUT}")


if __name__ == "__main__":
    main()
