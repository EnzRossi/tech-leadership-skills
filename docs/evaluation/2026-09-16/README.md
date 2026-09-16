# Retained evaluation artifacts

These are unedited model-generated test responses, **including failures**. They are not endorsed advice or example answers to copy. Fixtures are fictional. The authoritative interpretation and limitations are in [evaluation results](../../eval-results.md).

- [Comparison prompts](cases.json) and [additional prompts](remaining-cases.json): resolve fixture paths from repository root.
- [Revised outputs](with_skill/), [original-skill outputs](old_skill/), [baseline outputs](without_skill/), and [targeted reruns](rerun/).
- [Comparison grading](comparison-grading.json), [AI/health additional grading](additional-grading.json), and [sourcing/rerun grading](sourcing-additional-grading.json) contain assertion-level evidence and concerns.
- [Frozen comparison rubric](comparison-rubric.json) and [rubric review](rubric-review.md) distinguish the original measurement contract from subsequent corrections.
- [Revision inputs](revision-inputs.json) preserve the instruction content used in the first revised batch; original files are identified by Git revision and hashes.

The comparison was blinded by copying outputs to random filenames. [The mapping](blind-map.json) is disclosed for audit; it was withheld from the grader. Additional-case grading is not blinded. The generated local HTML review viewer is a convenience, not an additional measurement.

## Held-out and provenance records

- [Held-out cases and frozen assertions](heldout-cases.json), [revised outputs](heldout_with/), [baseline outputs](heldout_without/) and [blinded grading](heldout-grading.json).
- [Held-out blind mapping](heldout-blind-map.json), [final instruction hashes](final-instruction-hashes.json), and [run manifest with output hashes](run-manifest.json).

No changes to the skills followed the held-out run. Related worked examples were visible in the earlier development comparison; they were not part of the independent held-out author's context. Read both batches before drawing conclusions.
