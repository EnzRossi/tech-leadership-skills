---
name: skill-template
description: >-
  Replace this with what the skill does and when to use it, written from the
  user's point of view. List the situations, phrases, and adjacent requests
  that should activate it, and name near-miss situations that should not.
  Keep it under 1024 characters. This template itself should never activate.
license: Apache-2.0
metadata:
  author: EnzRossi
  version: "0.1.0"
---

# Skill name

One paragraph: the decision this skill supports, who makes it, and what artifact the skill produces.

## When not to use this skill

Name the adjacent situations that look similar but need something else, and say what to do instead.

## Inputs

List the artifacts to ask for. State what to do when they are missing. A skill that works only with complete inputs is not useful to leaders.

## Workflow

1. **Intake.** The questions that must be answered before analysis starts, and the maximum number to ask before proceeding with stated assumptions.
2. **Evidence.** How to read the inputs. Which signals matter, and which common signals mislead.
3. **Analysis.** The decision structure. Point to `references/methodology.md` for the detailed method and say exactly when to read it.
4. **Recommendation.** How to express the recommendation so it is specific and falsifiable.
5. **Output.** Fill `assets/output-template.md`.

## Evidence rules

State how to label facts, inferences, assumptions, and unknowns, and what the skill must never invent.

## Human decision boundaries

Only the boundaries that change this workflow. Do not add generic disclaimers.

## Gotchas

The mistakes a capable model makes on this task without the skill. This section is often the most valuable part of the file.
