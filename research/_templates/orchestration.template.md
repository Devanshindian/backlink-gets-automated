---
slug: <orchestration-slug>
type: orchestration
title: "<Human-readable campaign name>"
aliases: []
difficulty: medium         # low | medium | high
cost: medium               # free | low | medium | high
risk: low                  # low | medium | high
strategies: []             # strategy slugs this campaign sequences, in order
last_updated: YYYY-MM-DD
---

<!-- An orchestration is a RUNBOOK, not a reference article. It holds ORDER + LINKS only.
     Each step = one [[strategy]] link + a one-line gist. No how-to detail — that lives in the
     strategy files. If a strategy's process changes, update the matching gist here (drift rule). -->

## Goal
<One line: what this campaign produces.>

## When to run it
<The trigger / business situation that makes this the right campaign.>

## The sequence
1. **<Phase name>** → [[strategies/<slug>]] — _<one-line gist of what this step does>_
2. ...

## Where the links point
<Reverse-silo note: where the earned links should aim, if relevant.>

## Done when
<The success signal that the campaign worked.>

## Strategies used
- [[strategies/<slug>]] — <role in this campaign>
