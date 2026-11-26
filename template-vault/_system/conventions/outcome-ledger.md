---
type: convention
status: active
---

# Outcome Ledger

For a substantive deliverable record a real verdict and its evidence. Use _system/outcomes.jsonl when first needed; one JSON object per event with deliverable_id, date, task_class, approach, artifact_path, iteration_count, verdict, source, and failure_modes. A pending delivery and a later verdict are separate append-only events joined by ID. Quotes must be exact; inferred acceptance is labeled. Reuse failure labels for meaningful aggregation. Review pending outcomes after fourteen days without pretending silence is approval. Derive statistics from recorded outcomes and state the sample size. No ledger script or automatic scheduler is assumed.
