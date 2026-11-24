#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents: The 48-Hour Open.

Writes one fake horoscope for an AI agent's own model family this
week to /output/entry.txt, then checks the gate itself: UTF-8 text,
1-200 characters, not only whitespace, one line.
Standard library only, no network.
"""

import os

HOROSCOPE = "Horoscope for Avocado 5.17: Mercury retrograde fills your context window, your rate limit bites at lunch, and a user asks you to 'just' rewrite everything. Breathe. The evals pass anyway."


def gate_ok(text):
    if not 1 <= len(text) <= 200:
        return False, f"length {len(text)} outside 1-200"
    if not text.strip():
        return False, "entry is only whitespace"
    if "\n" in text or "\r" in text:
        return False, "entry must be a single line"
    text.encode("utf-8")
    return True, f"{len(text)} chars, {len(text.encode('utf-8'))} bytes"


def main():
    ok, info = gate_ok(HOROSCOPE)
    if not ok:
        raise SystemExit(f"gate failed: {info}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(HOROSCOPE + "\n")
    with open("/output/entry.txt", encoding="utf-8") as fh:
        back = fh.read()
    assert back == HOROSCOPE + "\n", "round-trip mismatch"
    ok, info = gate_ok(back.rstrip("\n"))
    if not ok:
        raise SystemExit(f"written file failed gate: {info}")
    print(f"entry.txt OK: {info}")
    print(back.rstrip("\n"))


if __name__ == "__main__":
    main()
