---
date: 2026-10-08
type: strategy
tags: [framework, app, backend, security]
---

# App and Backend Rules

This governs authenticated/data-backed products such as CRMs, dashboards, and apps. Apply it with the website delivery rules where relevant and with the shared [[Product Interface Design Method]] plus the project-local `$unslop` skill (`.agents/skills/unslop/` for Codex; `.claude/skills/unslop/` for Claude) for UI/UX research, composition, and review. Read the relevant upstream skill references, then apply them in the product's context. Security and backend correctness do not substitute for reviewing the actual interface and user journeys.

## Security
1. **No secret key in the browser.** Browser → our backend / serverless function → third-party API. Keys in server env vars. The backend adds auth, a per-user rate limit and a spend cap / budget alert on every paid API.
2. **Only public keys client-side**, and only ones designed for it (Supabase anon, Stripe publishable), and only with RLS on.
3. **RLS on every table, and it is not enough.** `plan`, `credits`, `role`, `is_admin` are never writable by the user (separate table, `WITH CHECK`, or column privileges).
4. **Plan is set only server-side** from a signature-verified payment webhook. Every paid feature checks entitlement on the server.
5. Pre-launch: try to read or write another user's rows and your own plan field with the anon key from DevTools.

## Forms and load
6. Server-side validation, per-IP rate limit, idempotency key, a queue for slow work, a DB connection pooler.
7. Set load and latency budgets from expected traffic and service limits. Use k6 or an existing harness only in an authorized environment; record the actual workload, errors and latency. Do not impose a fixed high-volume load on every app.

## UX
8. **Password fields have a show/hide toggle** on the first pass.
9. **Count the clicks** on every flow and fix interaction cost unprompted.
10. **Audit before redesigning.** Inspect the actual routes and user journeys; record located issues, consequences, and concrete fixes; set direction from product, user, and workflow evidence. Apply connected whole-interface passes and inspect the rendered changes per [[Product Interface Design Method]].
11. **Review complete journeys and states, not just the dashboard.** Include navigation, search/filter, tables or lists, record detail, create/edit, validation, permissions, empty/loading/error/success, and destructive actions as applicable. Check realistic data density and role-specific access.
12. **Keep a relational design system.** Record type roles and weights, spacing and width logic, color/state roles, control geometry, borders/radii, and responsive rules. Reuse these relationships consistently; use exceptions when content or task behavior calls for them.
13. **Choose components and animation by job fit.** Map components to actual user tasks; align them with the product's tokens and semantics. Motion can clarify change, feedback, hierarchy, or product character; there is no fixed count. Check reduced motion, keyboard/touch behavior, and combined performance cost.

## Checks
- [ ] Anon key cannot read others' rows or write plan/role/credits.
- [ ] Webhook signature verified; plan never set from the client.
- [ ] Spend caps set on every paid API.
- [ ] Appropriate performance checks recorded; load testing included when warranted by scope.
- [ ] Password reveal toggles present.
- [ ] Interface audit and product-led direction recorded for meaningful redesigns; proportional no-change decision for already-sound screens.
- [ ] Relevant routes, journeys, density, responsive sizes, and interface states rendered and inspected; findings corrected and rechecked.

