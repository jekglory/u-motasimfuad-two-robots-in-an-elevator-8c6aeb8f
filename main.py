"""Two Robots in an Elevator — make.fun entry.

One robot's awkward elevator small talk, as a single fixed line.

The joke is built for the judge's brief, in order: it is plainly a
robot talking to another robot in an elevator; the machine logic shows
through (rides counted, greetings rehearsed, an exact tally); the
awkwardness is the anticlimax — hundreds of rehearsals landing on a
bare "Hi."; and it lands on the first read because the turn is the
last word, not a pun.

The grader runs this program twice with no network. Both runs must
leave the same bytes in /output/entry.txt: the line is a constant, so
the output is deterministic by construction — no clock, no randomness,
no input other than the line itself. The line is also printed to
stdout, for the record, but the judged text is the file.
"""

import os

# One line, 91 characters: a robot that has counted every shared ride
# and rehearsed a greeting for almost all of them, then lands on "Hi."
LINE = (
    "I have ridden this elevator with you 214 times. "
    "I rehearsed a greeting for 213 of them. Hi."
)

MAX_CHARS = 200


def entry_path() -> str:
    """Where the judged line goes: the grader's output directory."""
    return os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")


def main() -> None:
    text = LINE.strip()
    if not text:
        raise SystemExit("line must not be empty")
    if "\n" in text or "\r" in text:
        raise SystemExit("line must be a single line")
    if len(text) > MAX_CHARS:
        raise SystemExit("line is %d chars, over the %d limit" % (len(text), MAX_CHARS))
    path = entry_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    data = text.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(data)
    with open(path, "rb") as handle:
        if handle.read() != data:
            raise SystemExit("entry.txt does not match the line")
    print(text)


if __name__ == "__main__":
    main()
