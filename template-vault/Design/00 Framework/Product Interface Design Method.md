---
date: 2026-11-14
type: strategy
tags: [design, framework, product-interface, unslop, ux]
---

# Product Interface Design Method

The shared design method for every interface we build: marketing websites, onboarding, dashboards, CRMs, internal tools, and mobile or desktop applications. The project-local website-build skill routes website delivery; [[Design Decision Framework]] supports source and technique selection. Authenticated/data-backed products also follow [[App and Backend Rules]]. The retired Website Build Framework is not a dependency. This method governs how we understand, design, and inspect the interface in either lane.

Adapted from Damir Sokolovsky's [`unslop` skill](https://github.com/heydamir/unslop), by [@heydamir](https://x.com/heydamir), shared under CC BY 4.0. Credit and link the source when adapting its material. This is an adaptation, not a verbatim copy of the upstream skill. Read the source when its detailed method or examples are directly relevant; never claim to have read a source that was not inspected in the current work.

## The working loop

### 1. Understand the product and the work

Establish who uses this screen, what they are trying to do, what decisions or consequences it carries, the product's character, and where it sits in the larger flow. For client work, research the industry, competitors, real product behavior, client identity, constraints, and verified content. For an existing product, inspect the implemented screen and neighboring states before redesigning it. Distinguish verified facts, assumptions, and invented sample data.

### 2. Audit before prescribing

Inspect the real interface at its actual routes and states. Record each material issue with location, user/product consequence, evidence, and a concrete correction. Check information hierarchy, task clarity, density, alignment, spacing relationships, type and numerals, color/contrast, controls, icon meaning, copy, empty/loading/error/success states, responsive behavior, keyboard/touch use, and motion. Look for generic or generated-design tells only where they harm this product; do not treat the checklist as a mandate to remove familiar patterns that serve the user.

Calibrate the work to evidence: a substantial set of defects merits a full pass; a mostly sound interface gets targeted polish; a screen without a meaningful defect gets an honest no-change assessment and optional directions. Do not invent defects or redesign merely to make the output look different.

#### Ecommerce brand and revenue audit

For an established brand, establish the commercial objective before proposing a redesign. Record the source, period, currency and scope for reported revenue. Separate company sales, DTC sales and owned-site revenue. If the channel split is private, record it as unknown. Ads, social engagement and retail presence show activity. Their contribution to sales and acquisition cost requires attribution data.

Follow the real mobile journey from a specific ad, creator post, search result or regional campaign to its landing page, product selection and checkout. When repeat purchase is the goal, trace the return journey through email, account, restock or discovery of a second product where access is available. Compare the audience and promise across channels with the site's navigation, photography, logo use, palette, editorial topics, product proof and tone. For an expansion market, check local customer language and product use alongside sizing, payment, delivery and returns. Use local evidence for cultural choices. Shopify is a platform detail. Document the exact storefront choice or journey defect and what it makes harder for the shopper.

Write each finding as **observed screen or handoff → plausible customer consequence → proposed correction → metric to check**. A visible mismatch supports a hypothesis about brand recognition, conversion or repeat purchase. Customer attribution, acquisition costs and retention require appropriately scoped analytics. For conversion, compare the same route and traffic mix. For retention, compare customers by first product, channel, market and a window that fits the product's buying cycle. Measure brand recall directly if it is the proposed outcome. Check product quality, fit, availability, pricing and post-purchase service as competing explanations. Use an experiment or a credible comparison before crediting design for a change.

For example, if a sports-bra campaign promises confidence on a run but the destination sorts by collection name and buries support and fit, design around how the customer trains. Show support early, use movement photography or an optional short fit demonstration and keep size selection in reach. If brand continuity is the issue, carry the same visual language and product promise from the social creative through the storefront and relevant post-purchase touchpoints. Choose logo, color and motion changes only where the evidence gives them a job.

### 3. Set a product-led direction

Write a short internal direction from the evidence: user and task, product character, appropriate visual world, which information or product moments deserve emphasis, and one recognizable detail that belongs to this product. Select references, skills, design systems, and components for specific jobs. Record what is borrowed, what is adapted, and what is rejected. A component catalogue is a source of candidates, not a page plan: compose selected parts into one system of hierarchy, type, color, geometry, icon language, behavior, and motion.

### Curate the brand identity

Apply this step before choosing an expressive site's layout, assets or animation.

1. **Start with the buyer and the story.** Record who is buying, the decision they need to make, what distinguishes this brand, and which verified facts or available assets can show it. Mark assumptions and concept material. Choose the imagery, typography, palette, composition and motion together so they express the same point of view.
2. **Study what each reference does.** Use relevant examples from the vault, live sites, Awwwards, Lenis, GSAP, Lottie or Unslop. Record the URL or supplied screenshot, what you actually observed, what job that choice does, and how the principle translates into an original treatment for this brand. Distinguish a still from observed playback. Choose a technique or library after deciding what the visitor should see, learn or feel.
3. **Compare two different concepts for expressive builds.** Sketch two materially different compositions and story sequences before coding. A palette change or a different effect on the same layout counts as one concept. Record the choice and why it better serves this buyer, brand and available evidence. Ask which part would stop making sense if another brand's logo and product were swapped in. If every expressive choice survives the swap, revise the concept. For task-focused tools, use the same evidence to give the interface appropriate character and prioritize the work itself.
4. **Give each word and animation a job.** Keep copy that communicates the brand, helps the visitor decide, or tells them what they can do. Remove decorative counters and redundant microcopy. Describe each major animation in one sentence that states what changes, what it communicates, and how the same information and controls work on touch and with reduced motion.

**Design the experience as a whole.** Map how the opening, transitions, controls and closing moments express the brand together. Motion can build anticipation, reveal a detail, or carry atmosphere as well as provide feedback. Glass navigation, magnetic hover, horizontal scroll, custom cursors and 3D are options tied to a particular brief. A suggestion made for one build does not become a default on the next. Give small type a real role in the hierarchy and check legibility in context.

**Build a case for the style from brand evidence.** Compare the product, materials, pricing and occasion with the brand brief, logo, campaigns, public social posts and available customer evidence. Look for recurring visual cues, language, and how people use or talk about the product. Treat follower and comment signals as hypotheses, and record uncertainty about audience, keywords, or positioning. An existing site is one source and may lag the brand. Choose the palette, typography, image treatment, density and motion as a set. Category and generation alone do not decide the style: skate commerce can be restrained, and two drinks brands can express entirely different occasions. A quiet design can still have a signature interaction, such as a focused product reveal. Make price, stock and other essential facts reachable on touch and keyboard.

**Translate the reference into a coherent visual world.** Identify the visual grammar and the job behind it: a dot can navigate, a cutout can organize a story, and fine type can establish hierarchy. For restrained apparel, depth might come from garment layers and fabric movement. For a historical concept, carry period cues through imagery, typography, composition and motion. Illustration, insects, flowers, bubbles and gradients are candidates when their subject or behavior makes sense for that audience and product. Test hybrid directions by checking whether their quieter and bolder moments still feel like the same brand.

**Art direct from cultural and product context, including on short briefs.** Identify what the audience recognizes, how the product is used, and what the place, sport, craft or occasion contributes. Give each visual reference a role in casting, gesture, material, photography, typography, or pacing. Carry the concept from the opening composition into the next section. Verify specific cultural or material claims and distinguish references from evidence of provenance. For a product story, keep at least one clear view of the product when blur or unusual crops carry the campaign.

**Connect the product, its origins and its use before choosing a visual theme.** Investigate what the product is for, how and why it was made, when customers use it, and what cultural or technical context could give it a story. Start from the brief and verify relevant details through brand materials and credible sources. Map each useful connection to something the visitor can see or experience across sections. If a connection is speculative, record it as a concept. For a Rajasthan-inspired polo campaign, examine specific rug borders, floral motifs and carved or painted wall details alongside the motion and dress of equestrian polo. For gummies, start with the actual use, ingredients and sourcing before selecting a nature-led direction or making an organic claim. For a mixer, confirm which kind of mixer it is and explore the mechanism, craft or use that makes it distinctive. These examples show how to find a story from evidence rather than assigning an aesthetic by category.

**Compare structural patterns across builds.** Before committing to a new direction, compare the proposed first screen, scroll sequence and mobile composition with recent builds. If the same image-and-type arrangement or reveal keeps recurring, explain why it belongs to this brief or explore a different structure. Change hierarchy, framing, or how the visitor encounters the product if color and typography alone leave the experience feeling interchangeable. On phones, decide what the viewer sees first, what stays together, and what moves before laying out the desktop composition. Check the rendered scene at rest and mid-motion for subject clipping, off-screen copy and awkward stacking.

**Study playable motion at source frame rate.** For supplied clips that can be accessed, inspect every decoded frame in order (use indexed contact sheets and zoom into transitions). Record trigger, start and end states, key poses, timing, layers, masks, movement, typography, and how the scene settles or loops. Distinguish observed timing from an inferred implementation. Record inaccessible clips as pending, and keep user descriptions or stills labeled as such. Add useful findings to the existing reference notes as the library grows.

**Set the motion character before selecting effects.** Choose where the brand sits between quiet, editorial pacing and expressive campaign choreography. Record why, using the buyer, brand voice, product and story. A soft fade or short type reveal can fit a restrained direction or connect two beats. For a bold direction, storyboard a signature moment that comes from the product, such as an outsole meeting a surface or changing underfoot, and assess whether a generic fade or wipe would lose that idea. Use GSAP for choreography, Three.js for real spatial behavior where depth or physical response serves the idea, and Lenis only when scroll pacing benefits. Treat library demos as a technique source. Prototype the key moment before committing to the stack.

**Design mobile as a primary experience for consumer sites.** Storyboard phone and desktop together. Preserve the brand, story beats, decisions, and useful feedback on touch, then adapt the composition, art crops or assets, pacing, and gestures. Give hover interactions a meaningful tap or touch equivalent when they communicate something useful. Keep decorative pointer effects optional. For expressive pages, plan a lighter touch-led sequence where the desktop effect would cost too much. Preserve the essential experience in reduced motion and when 3D is unavailable. Review on a representative phone and at a narrow viewport with touch, motion enabled and reduced motion. Check the first-screen impression, framing, tap and scroll behavior, and perceived responsiveness. Record any device checks still outstanding.

**Review the actual assets and components in motion.** Reuse suitable components or effects from the project, an accessible 21st.dev entry or another licensed source before writing custom code. Fit real imagery and copy to the component, define aspect ratios and intentional overflow, and inspect intermediate animation frames, rapid input and breakpoint changes. Check image clipping, container height, text wrapping, grid alignment and layout shifts across representative desktop and phone sizes. Fix visible issues before handoff. Distinguish reference motion observed live from behavior described in a walkthrough or inferred from screenshots.

At rendered review, check that the visual treatment still follows the chosen concept on desktop and mobile, the primary action is clear, and the static state conveys the essential information. Record and correct any generic composition, filler copy or motion that lost its intended job during implementation.

### 3a. Resolve direction from context without routine questions

Use the explicit brief and verified brand/assets first, then user tasks, content, language, accessibility and device constraints, then inspected source systems and reusable components. Aggregated award patterns and personal taste are candidate sources, not requirements. Preserve the current product identity unless the request authorizes changing it. A gradient, serif, bold weight, uppercase label, dense layout or multiple accents is not a defect by itself; identify the actual readability, task, brand or consistency failure before changing it.

Choose ordinary design details internally. Ask only when missing facts, assets, rights, access or a material scope decision prevent a responsible result. An explicit build/redesign request authorizes design selection and correction. A discussion or review does not authorize implementation. Reuse the project's existing design record; a short decision note is sufficient when no spec exists. Keep these shared instructions in the vault and implementation, dependencies, assets and tests in the relevant GitHub project checkout.

**Automatic typography selection:**

1. Inspect the existing brand fonts and available licensed files. Retain an established family unless the requested change, missing glyphs, unreadable roles or unavailable rights require an alternative.
2. Assign roles from actual content: navigation/control text, reading text, display headings, metadata and numeric data. A role does not require a different font. Use one family when it handles the work; add a partner only to solve a named expressive or legibility need.
3. Choose candidates by audience/brand character, language and glyph coverage, real weight/style availability, numeral clarity, density and screen rendering. Dense CRM tables need distinguishable characters and usable numerals; commerce names and prices must scan; editorial display type may carry brand expression without setting control text in the same style. Do not default to a serif/sans pairing, Inter replacement, uppercase ban or weight cap.
4. Set size, weight, leading, tracking and text measure together using the actual longest labels, headings, prices, dates and translated strings. Use tabular numerals where values must align; preserve meaningful currency and precision differences. Verify that fonts really load and that fallback metrics do not break the layout.
5. Inspect desktop and mobile renders for line wraps, truncation, reading comfort, hierarchy and control fit. Correct the chosen typography before handoff. Record the selected roles and brief rationale, not a list of unchosen fonts or an approval request.

**Composition follows the journey:** choose content order, emphasis, density and navigation from what users need to understand or accomplish. Preserve useful existing structure; change it when located flow problems or the brief justify it. A full-bleed scene, asymmetric hero, centered headline, card grid or plain data table is an option, never a default obligation. Test mobile composition using real content rather than automatically stacking desktop columns.

| Context | Journey/state coverage when in scope |
|---|---|
| Commerce | Category/search → product → variant/availability → cart → checkout; price and shipping clarity, empty cart, unavailable item and failed submission/payment |
| SaaS | Proposition and evidence → relevant action; for the product itself, onboarding → core task → result, permissions and recovery |
| CRM/internal tool | Role-specific navigation → search/filter/list → record → create/edit/action; realistic dense data, validation, loading/empty/error/success and destructive actions |

Do not invent missing features to fill this table. Cover the journeys the product actually provides.

**Components and assets:** inspect the project's existing implementation first, then relevant HeroUI, 21st.dev or other sources. Confirm the specific component's license, attribution, commercial/client usage rights, dependencies, stack compatibility and accessible behavior. Check whether the exact source/asset requires a paid plan or account entitlement; a free catalogue entry does not prove all bundled assets are free. Use available authorized resources or a licensed equivalent, and explain an unmet explicitly requested source. Never purchase or bypass access. Adapt selected parts to the same type, spacing, color/state and interaction roles.

**Motion selection and usable baseline:** start with readable content and usable controls. CSS/native behavior suits simple feedback; GSAP suits coordinated timelines and scroll-linked sequences; Lenis is optional scroll smoothing, not a prerequisite for GSAP; Lottie suits an authored vector animation; Three.js suits real-time scenes or shader effects that the direction calls for. Choose only the libraries required by the behavior, check current official APIs and licenses during implementation, and verify the combined cost. Keep native scrolling, keyboard/touch access, content and primary actions usable if enhancement fails. Provide reduced-motion and static/poster states, lazy-load heavy optional assets, pause inactive work, and handle renderer/context failure. Reduced motion must not merely swap live 3D for an autoplaying video. Measure loading and interaction on representative devices/network conditions; simplify or defer the expensive layer when it misses the project budget. A loader cannot excuse blocking useful content.

### 4. Refine the whole interface in connected passes

Use the order as a practical dependency guide; return to earlier decisions when content or behavior requires it.

1. **Structure and task flow:** hierarchy, content order, task sequence, navigation, information density, responsive composition.
2. **Spacing and alignment:** shared edges, proportions, rhythm, control placement, text fit, and consistent relationships among containers, insets, radii, and icons.
3. **Color and surfaces:** role-based tokens, contrast, state clarity, layering, and material treatment.
4. **Icons and controls:** meaningful icon semantics, consistent stroke/size, hit areas, labels, focus and selected/disabled/error states.
5. **Copy and typography:** product vocabulary, concise labels, font role and character, actual weights, hierarchy, line lengths, numerals, glyph coverage, and wrapping.
6. **Composition and detail:** charts, tables, visualizations, imagery, transitions between sections, empty/loading/error/success states, and small interaction feedback.
7. **Motion and sensory behavior:** add or correct movement only when it explains change, hierarchy, spatial relationships, feedback, or brand character. The number and type of patterns follow the story and task; there is no fixed animation quota. Audit the combined runtime, paint/GPU, network, accessibility, and attention cost. Use reduced-motion and input-appropriate behavior.
8. **Render and re-audit:** inspect the changed interface, compare against the issue list and direction, test relevant routes/states and device sizes, record what remains, correct defects, and inspect again. A written token map or a successful build is not visual QA.

For an app/CRM, perform the passes across complete user journeys and state variations, not only the dashboard landing screen. Include dense data, table/filters, record detail, create/edit, validation, permissions, empty/loading/error/success, and destructive/irreversible actions where present. Prioritize legibility, predictability, trust, and task completion; use expressive motion where it clarifies system feedback or product identity.

## Visual redlines and communicating the work

The upstream demonstrations use redlines and in-place changes to make design correction visible. Use a before/after or annotated comparison when it materially helps the team understand a review or a design transformation. It is a communication aid; the live product does not need to animate its own critique. Never use a compelling demo clip as a substitute for route/state coverage, responsive checks, accessibility, or actual browser inspection.

## Evidence record

For meaningful redesigns, retain a concise audit with issue/location/evidence/consequence/fix, the product-led direction, relevant source and component choices, and a final verification note. Use the build's existing design spec and review record instead of duplicating this material. Keep findings and changes traceable; do not turn design review into a user-approval gate for ordinary decisions.

## Source boundary

The upstream skill contains specific token scales, layout preferences, and motion recommendations. Treat those as source-specific heuristics, not universal laws. The product, client identity, user task, accessibility, chosen design system, and measured runtime cost govern local choices. Preserve the underlying craft loop—specific audit, product-led direction, connected full-interface passes, rendered correction—without copying constraints that conflict with the product or measured evidence.

Separate **evidence-based engineering/accessibility thresholds** (for example WCAG contrast, touch-target usability, and measured load cost) from **aesthetic heuristics** (for example a fixed palette count, headline line count, one accent, or animation count). Preserve the former where applicable. Use the latter as starting points and change them when the product, content, source system, or rendered layout supports a better choice. No universal pixel prescription replaces inspecting the relationships in the actual design.

