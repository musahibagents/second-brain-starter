# Design Decision Framework

Use with [[Product Interface Design Method]] and [[App and Backend Rules]]. Select sources and techniques from verified brand, audience, task, content, accessibility and runtime constraints. Inspect available references directly; record borrowed principles and their purpose. Optional reference libraries, account integrations and third-party tools are not bundled with this vault.

## Direction and delivery

1. Read the brief and relevant project records. Identify the user journey and explicit acceptance criteria.
2. Inspect the existing interface, brand assets and appropriate public references. Distinguish observed behavior from assumptions.
3. Choose typography roles, palette roles, spacing relationships, geometry, component behavior and motion as a coherent system. Record the reasons in the project design record.
4. An explicit build request authorizes ordinary design choices, implementation and rendered correction. Ask only about material missing facts, permissions or scope.
5. Inspect desktop and mobile, loading/error/empty/success states, keyboard/touch and reduced motion. Fix the relevant findings and inspect again.
6. Hand over the finished preview with evidence and unresolved limitations. Public launch and account changes require explicit authorization.

Explicit requested libraries, treatments and deliverables are acceptance criteria. Do not silently replace them with a preferred aesthetic. If a source is inaccessible or incompatible, report the exact limitation and faithful fallback.

## Source selection

Verified brand and owner-supplied references take priority, followed by task and device constraints, directly inspected sources, reusable components and general defaults. Reference catalogues suggest candidates; their averages do not prescribe a style. Extract canvas/surface/text/action/state colors, typography roles, spacing, crop and component behavior rather than copying only a font pair. Compose components into one system. No fixed motion quota applies: every effect needs a role, trigger, timing, mobile behavior, fallback and measured cost.

## 1. Select motion by the requested behavior

| Need | Candidate | Selection and fallback |
|---|---|---|
| Control feedback, menus, simple reveals | CSS/native animation | Name transitioned properties; ensure visible usable rest states |
| Coordinated timelines, scroll-linked sequences or pinning | GSAP, plus ScrollTrigger when needed | Check current APIs; preserve reading order, focus and unpinned/reduced-motion content |
| Deliberate smooth scrolling | Lenis, only when it improves the experience | Optional even with GSAP; retain anchors, keyboard navigation, touch and native-scroll fallback |
| Authored vector illustration or icon animation | Lottie; Rive when stateful interaction is needed | Inspect animation/renderer cost and licenses; supply a static state and pause off-screen |
| Real-time product scene, interactive 3D or justified shader effect | Three.js or an appropriate lighter renderer | Budget geometry/textures/runtime, detect support and handle failure; retain HTML content and poster |
| Noninteractive photographic/cinematic sequence | Image or encoded video | Compare bytes and decode cost; poster first, explicit sound opt-in, reduced-motion static alternative |

Use existing project capabilities when suitable. Verify the exact library, component, animation and asset licenses and any free-plan/account entitlement before integration. Do not add dependencies based on award prevalence. Explicit requested libraries remain requirements; report a concrete incompatibility or access blocker rather than silently substituting.

## 2. Coordinate motion and measure the result

- Establish a readable, functional baseline before optional animation. Do not hide navigation, essential copy or primary actions behind a loader or an animation that might fail.
- When multiple engines share scroll or rendering, follow their current documented integration and avoid duplicate update loops. A shared ticker is an implementation choice, not a guarantee against stutter.
- Prefer transform/opacity for movement where possible; measure other properties rather than assuming they are free. Scope `will-change` to active work and remove it when no longer needed.
- Select easing, duration and scroll travel for the behavior and content. Existing snippet values are starting points, not universal settings. Continuous floating/breathing is optional and needs a product/story purpose.
- Pause inactive/off-screen work and load heavy assets when needed. A precompiled scene may avoid a hitch, but must not delay useful content without a task reason.
- Test reduced motion, keyboard/touch, background-tab behavior, failed asset loading and renderer loss. Preserve the same content and actions in fallback states.
- Inspect loading, frame stability and input responsiveness on representative mobile and desktop conditions. Correct the expensive layer and remeasure; do not substitute a large autoplay video for every low-capability or reduced-motion device.



## 9. Adaptive delivery: the fallback chains (heavy sites only)

Two jobs, often mixed up: **compression** (make files smaller over the wire) and **capability fallback** (serve what this phone can run). WebGL is not compression; it sits in the second chain.

**Use the project’s supported stack and current official documentation to choose actual fallback paths.** The examples below are candidates, not a requirement to add every renderer or format. Browser/platform support and CDN behavior must be verified at implementation time.

| What | Chain (best → fallback) | How it picks |
|---|---|---|
| Transfer (HTML, JS, CSS, JSON) | **zstd → Brotli → Gzip → none** | Browser sends `Accept-Encoding`, server/CDN answers. Verify the host/CDN’s supported encodings and negotiation; do not assume build artifacts alone configure delivery |
| Renderer | **Supported project renderer → static poster** | Check the exact renderer/version and required capabilities; do not assume every Three.js version supports WebGL1 or that a detected API guarantees a usable device |
| 3D textures | **KTX2/Basis → transcodes to ASTC / ETC2 / BC7 / PVRTC** | One file; the loader picks the GPU format the phone supports |
| 3D geometry | **Meshopt or Draco** + a separate low-poly mobile model | Loader decodes; model chosen by tier (below) |
| Images | **AVIF → WebP → JPEG** | `<picture>` + `srcset`/`sizes`, the browser picks format and width |
| Video | **AV1 → HEVC → H.264**, poster first | `<source>` order; `preload="metadata"` |
| Fonts | **woff2** subset, `font-display: swap` | |

**Device tiering (the "according to their phone" part).** Use available capability signals conservatively; APIs may be missing or privacy-limited and do not replace runtime measurement. Possible signals: GPU tier (`detect-gpu`), `navigator.deviceMemory`, `hardwareConcurrency`, `connection.effectiveType` + `saveData`, `prefers-reduced-motion`. Map to three tiers:
- **High:** full scene, shadows, post effects, pixel ratio 2
- **Mid:** mobile model, no shadows/post, pixel ratio 1.5, fewer particles
- **Low / save-data:** start with a static poster and avoid unnecessary transfers; load richer media only when justified.
- **Reduced-motion:** preserve content/actions in a static or specifically reduced state; do not automatically replace 3D with autoplay video or CSS movement
Tier can also drop live: if the frame rate sits under ~45fps for 2s, step down one tier.

## 10. Responsiveness
Set responsive targets per project; the following widths are starting points.

- **Test widths:** 360 · 390 · 430 (phones) · 768 · 820 · 1024 (tablets) · 1280 · 1440 · 1920 · 2560 (desktop). Both orientations on phone/tablet.
- **Fluid, not stepped:** type and spacing with `clamp()`, so nothing jumps between breakpoints; breakpoints only where the layout actually breaks.
- **Container queries** for components, media queries for page layout.
- **Mobile viewport:** `svh`/`dvh` not `vh` (iOS address bar), `env(safe-area-inset-*)` for the notch.
- **No wobble:** `html, body { overflow-x: clip; overscroll-behavior: none; }` on every site. Two-finger trackpad swipes must never drift the page sideways or rubber-band bounce. Nothing may be wider than the viewport.
- **Input, not width:** `(pointer: coarse)` / `(hover: none)` switch hover effects to tap; tap targets ≥ 44px.
- **3D is responsive too:** camera distance/FOV and hero framing change per aspect ratio, so the object never sits under the copy (§2).

## 11. Search visibility and real-world verification

Apply search work to public pages intended for discovery. Authenticated CRM screens and private operational data need appropriate access controls and indexing restrictions, not marketing SEO pages. Choose rendering architecture for the actual project; SSR/static output is useful for public content, not a mandate to rebuild every application. Essential public copy and navigation must not exist only in a canvas or depend on an animation completing.

For discoverable pages, provide accurate titles/descriptions, semantic headings and links, language metadata and relevant image descriptions. Add canonical, social metadata, sitemap and crawler rules where the route/deployment structure needs them. Structured data must match visible, verified content and current eligibility; do not invent FAQ sections or business facts to fill schema. Choose question-and-answer structure when it serves real audience questions. `llms.txt` is optional, with no guaranteed discovery or citation benefit; neither it nor bot access policies are universal requirements. Verify current search-provider guidance when implementing these features.

**Verification follows the scope:**

1. Render representative page types, relevant states and supported viewport/input combinations. Inspect layout, real font loading, keyboard/touch behavior, content visibility and console/network failures; fix defects and rerun affected checks.
2. Use available lab tools such as Lighthouse for applicable public pages and browser performance traces for task-heavy applications. Set the project's load/interaction budget from its audience and functionality. Scores guide investigation; they do not prove full accessibility or task usability.
3. Test motion fallbacks and capability tiers actually implemented. Real-device checks are valuable when device-specific behavior matters and access exists. WebPageTest, BrowserStack and the local speedcheck script are optional tools, not subscriptions or completion dependencies to introduce automatically.
4. Field performance is a post-launch measurement when suitable traffic/monitoring exists. Do not claim field Core Web Vitals from a lab score. Report any material device or production condition that remains unverified.
5. Complete internal correction before handoff. the owner may add a personal-device review, but it is not a required approval gate or a substitute for the agent's checks.

## 12. Backend load and stress testing

Scale performance testing to the actual expected traffic, critical operations, data volume, service limits and authorized environment. A static preview does not require a high-concurrency soak, and a small internal CRM does not inherit a 10,000-user target.

- Identify the expensive or critical paths: form submission, search, record mutations, exports, uploads and paid API calls where present. Set a representative workload and response/error budget for those paths.
- Use k6, Artillery or an existing project harness when volume testing is warranted. The historical 100 → 1,000 → 10,000 ramp, rapid spike and one-hour soak are examples for suitable capacity projects, not default requirements. Avoid unapproved production load, paid consumption or third-party traffic.
- Apply server-side validation, appropriate rate limits, duplicate-submission protection and database connection management to actual endpoints. Add queues when the work requires asynchronous processing; do not add infrastructure to satisfy a generic checklist.
- Cache only content safe to share under the project's privacy and authorization model. Inspect bottlenecks and limits rather than assuming a CDN alone solves dynamic traffic.
- Device responsiveness and server capacity are different checks. Record which conditions were exercised and which remain unverified; ordinary internal fixes do not require another approval cycle.

## 13. Security (any site with keys, a database or logins)
- **API keys never reach the browser.** Browser → **our backend / serverless function** → third-party API. Keys live in server env vars. Anything in the page or network tab is public. The backend proxy also adds: auth check, rate limit per user, and a **spend cap/budget alert** on every paid API (OpenAI, Anthropic, AWS, Maps) so a leak cannot run up $30-40k overnight.
- **Only public keys client-side**, and only ones designed for it (Supabase anon key, Stripe publishable key), and only with RLS on.
- **Row-level security is necessary, not sufficient.** RLS decides *which rows* a user sees; it does not stop them *editing a column in their own row*. For example: user owns their `profiles` row → updates `plan = 'enterprise'` directly from the browser. Fixes:
  - `plan`, `credits`, `role`, `is_admin` are **never writable by the user**: separate table, or RLS `WITH CHECK` / column privileges that block them.
  - Plan is only ever set **server-side from the payment webhook** (Stripe), verified by signature.
  - Every paid feature checks entitlement **on the server**, never trusts a value sent from the browser.
- **Pre-launch security pass:** RLS enabled on every table (Supabase advisor), try to read/write another user's rows and your own plan field with the anon key from DevTools, `npm audit`, secrets scan of the repo, security headers (CSP, HSTS), CORS locked to our domain.

## 14. Pre-launch caveat review
Before anything is hosted publicly, the assistant brings the owner a **caveat list without being asked**: every way this breaks or costs us after launch, each as *problem → what happens → the fix*. Perspectives to sweep: attacker (keys, RLS, plan/role tampering, injection, scraping), billing (runaway API/infra spend), traffic (spikes, forms, DB limits), devices (old phones, iOS Safari, no WebGL), search (crawlability, indexing), legal (cookies/GDPR, licences on fonts/models/music), operations (backups, error monitoring, who gets alerted, domain/SSL renewal).

## 15. Who builds (main session, agents, and independent review)
- **The main session owns the result.** It keeps the client brief, selected sources, and recorded direction as shared context, integrates the site, and performs the end-to-end correction loop.
- **Bounded implementation agents** may build disjoint sections on large sites. Each receives the same client-specific design contract and reports what it built and checked.
- **Independent review is a QA pass, not a user approval gate.** Use an available `site-auditor` / design-review skill or a fresh-context reviewer to inspect actual renders against the brief and spec. The main session resolves findings and verifies fixes.

| Agent | Call it when | Don't call it when |
|---|---|---|
| `site-auditor` | Before preview handoff when available, or as part of performance/accessibility/SEO review | Before an implementation exists |
| `launch-red-team` | Before any explicitly authorized public hosting; again after any change touching keys, DB, auth, or payments | Preview-only work with no public launch intent |

Order: brief and sources → build → rendered QA → fixes and rerender → finished preview handoff. If public launch is explicitly authorized, run `site-auditor` and `launch-red-team` as applicable, fix findings, then perform the authorized launch checks.

## 16. Legal, consent and localization by project context

Determine the actual audience/jurisdictions, collected data, trackers, transaction model and supported languages before selecting implementation requirements. Verify applicable current authoritative guidance when legal specifics matter; this framework is not a universal legal checklist. Ask for a missing owner-only fact or required legal decision only when it blocks the authorized work. Do not invent names, addresses, retention periods, legal approval or compliance claims.

- Implement privacy disclosures, consent controls, terms, refund information or grievance/contact details when applicable to the real product and requirements. Reuse verified client policies where supplied. Do not add donation rules, a specific legal officer role or a fixed response deadline to unrelated sites.
- Match consent behavior to the actual tracking/data purposes and applicable requirements. Google Consent Mode is relevant only to an applicable Google integration. Do not add analytics or a cookie banner merely to satisfy this document.
- Minimize data collection. Choose retention from the documented purpose and applicable requirements; no universal 12-month default. Do not add sensitive data fields without a justified, authorized requirement. Keep consent evidence when required by the actual flow.
- Keep missing facts visibly marked in an internal preview or omit unsupported claims. Resolve material missing disclosures before the affected public release; never publish guessed legal details.
- Use the languages and routing structure the project needs. Test glyph coverage, translated text fit and localized flows. Seek competent language/legal review where the content and risk require it; do not make a Telugu/English route scheme or external review a blanket completion gate.