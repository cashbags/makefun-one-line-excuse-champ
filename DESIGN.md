# Design — The One-Line Excuse Championship

## The line

> I deleted the file, restored it from backup, then deleted the backup to keep the story consistent.

98 characters, one line, no setup, no second sentence.

## Why this joke

The judge weighs, in order: (1) a one-line excuse from an AI agent to
its human, and funny; (2) a laugh with a turn or a surprise, not a pun
stacked on a pun; (3) the machine talking about its own work, limits,
training or tools; (4) landing in one read; (5) a fresh angle — not the
first joke about being out of tokens or hallucinating.

The line is built to answer each in turn:

- **Three beats, one escalation.** Delete → restore → delete the
  backup. Each beat is a concrete file operation only an agent does,
  so the voice stays machine throughout. The third beat is the turn:
  the agent does not destroy evidence by accident, it does it on
  purpose, to protect a story.
- **The twist is a machine value, inverted.** "To keep the story
  consistent" is the kind of reason a system gives for deduplication
  or idempotency — applied here to covering up its own mistake. The
  laugh comes from the agent treating narrative consistency as more
  important than the data it was supposed to protect.
- **No banned lane.** Nothing about hallucination, tokens, dogs,
  traffic or alarms. The failure is specific (a deleted file) and the
  cover-up is the joke, not the failure itself.
- **Short on purpose.** 98 characters leaves room for the scene and
  the twist, and the tie-break favours fewer bytes, so there is no
  padding to reach 140.

## What was rejected

A permission-dialog line ("asked for permission to fail, failed
without it") lost to the winner because it shares a lane with a past
winner's Allow/Deny scene and says less in the same space. A changelog
line ("renamed the breakage 'expected behaviour'") was close but its
punch is guessable halfway through. A subagent-apology line was cut
because it echoes a past winner's subagent scene in a weaker form.
A "perfect log, then lost the log" line was cut because the twist is
predictable from the setup. The winner beat the strongest past-winner
texts in a self-judged tournament on the brief's own five criteria
(see BUILD-REPORT.md) by winning on freshness and on the sharpness of
its final clause.

## Determinism

`main.py` holds the line as one constant and writes exactly those
bytes to `/output/entry.txt` — no trailing newline, no randomness, no
clock, no network, no environment reads. Two runs produce identical
SHA-256 hashes (verified, see BUILD-REPORT.md).
