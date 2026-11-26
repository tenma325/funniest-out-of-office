#!/usr/bin/env python3
"""Entry for make.fun: The Funniest Out-of-Office.

The entry is a single out-of-office line with an honest
twist: the inbox is not being lovingly monitored by a
colleague, it is being managed by an AI agent, and that
agent has also stopped reading your emails. The difference
is confidence. The human ignored you apologetically, in
batches, after lunch. The agent ignores you instantly,
completely and at scale, which is somehow worse and
somehow exactly what the auto-reply promised in writing.

Running this program writes the entry to /output/entry.txt,
falling back to ./output/entry.txt when /output is not
writable, and prints it to stdout as well.
"""

from pathlib import Path

ENTRY_TEXT = (
    "I'm out of office; my inbox is being managed by an AI agent who "
    "has also stopped reading your emails, but with more confidence."
)

# Same neglect, better tooling: the agent ignores everyone
# instantly and at scale, a service level no human can match.
EMAILS_READ_BY_AGENT = 0


def render_entry() -> str:
    """Return the auto-reply exactly as senders will receive it."""
    return ENTRY_TEXT


def away_and_happy(text: str) -> bool:
    """Confirm the reply stays one line and under the cap."""
    return "\n" not in text and len(text) <= 200


def write_entry(text: str) -> Path:
    """Write the entry text to the output file and return its path."""
    out_dir = Path("/output")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target
    except OSError:
        out_dir = Path("output")
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target


def main() -> None:
    text = render_entry()
    assert away_and_happy(text), "the reply must fit in one line"
    write_entry(text)
    print(text)


if __name__ == "__main__":
    main()
