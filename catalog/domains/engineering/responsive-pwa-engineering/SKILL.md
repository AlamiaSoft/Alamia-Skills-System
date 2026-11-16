---
name: responsive-pwa-engineering
description: >-
  Engineer, audit and verify responsive web and PWA experiences across mobile phones,
  tablets, desktops, orientations and real browser viewport conditions.
license: MIT
metadata:
  type: specialist-capability
  category: engineering
  version: "1.0.0"
---

# Responsive PWA Engineering

## Purpose

Make web applications and Progressive Web Apps genuinely usable across supported screen sizes and device classes. This skill is for implementation and remediation, not merely writing a responsive-design checklist. It applies to content sites, dashboards, forms, ecommerce flows, interactive tools, canvas interfaces and games.

A page is not responsive just because it has a viewport meta tag or a few media queries. The actual layouts, controls, content, navigation and primary workflows must work at narrow phone widths, large phones, tablets, landscape orientations and desktop sizes.

## Activation

Use when:
- building a new responsive web app, PWA, game or interactive experience;
- auditing or fixing layouts that break on phones or tablets;
- implementing a screen from a desktop-first design or design mockup;
- fixing clipped controls, horizontal overflow, tiny game tiles, unusable landscape layouts, keyboard/viewport issues or touch interactions;
- adding a new page or feature that must follow the project's responsive behavior.

## Inputs

- Repository instructions and existing UX/UI/frontend skills.
- Product requirements, primary user journeys and supported browsers.
- Existing design tokens, component library, CSS strategy and layout conventions.
- Available device/browser test tooling and known target devices.
- For games: board dimensions, interaction model, minimum playable tile/control size and game-state constraints.

If target devices are not specified, establish a sensible baseline matrix and document assumptions rather than silently testing only the developer's desktop.

## Non-negotiable principles

1. **Mobile-first, fluid by default.** Start with the narrowest supported layout and progressively enhance. Use content-driven breakpoints; do not design only for named device models.
2. **Test real viewport dimensions.** CSS viewport width, height, orientation, browser chrome, safe areas and on-screen keyboards matter more than device labels.
3. **No accidental horizontal scrolling.** Every supported viewport must be checked for document-level overflow. Intentional horizontal scrollers must be obvious, contained and operable.
4. **No fixed desktop assumptions.** Avoid hard-coded page widths, fixed-position controls that cover content, rigid multi-column layouts and fixed heights that clip text or controls.
5. **Touch is a first-class input.** Primary actions must work without hover, tiny hit areas or precise pointer movement.
6. **Responsive behavior must preserve function.** Do not hide essential actions, truncate critical information or remove game controls just to make a screenshot fit.
7. **Measure and verify.** A CSS change is not complete until the affected routes and interactions have been checked at representative phone and tablet sizes.

## Procedure

### 1. Reconnaissance before editing

- Read repository agent instructions, design tokens, routing, shared components and current responsive conventions.
- Identify every affected route, reusable component and critical user journey.
- Inspect existing media queries and detect conflicting/duplicated breakpoint rules.
- Run the current app and capture baseline screenshots at narrow phone, common phone and tablet dimensions.
- Record concrete defects: overflow, overlap, clipping, inaccessible controls, poor text wrapping, unusable game boards, sticky elements covering content, keyboard obstruction or orientation failure.
- Preserve existing behavior and working business/game logic. Separate layout changes from domain logic unless a functional change is required and approved.

### 2. Define the viewport and device matrix

At minimum, validate representative CSS viewport sizes near:

| Class | Width × height | Purpose |
|---|---:|---|
| Small phone | 320 × 640 | Narrow legacy/small devices |
| Typical phone | 360 × 800 | Common Android baseline |
| Modern phone | 390 × 844 | Common modern phone |
| Large phone | 430 × 932 | Large phone / phablet |
| Small tablet | 600 × 960 | Compact tablet / split view |
| Tablet portrait | 768 × 1024 | Standard tablet portrait |
| Tablet portrait large | 820 × 1180 | Common modern tablet |
| Tablet landscape | 1024 × 768 | Tablet landscape |
| Desktop | 1280 × 800 | Wider layout regression |

Adapt the matrix to the product's actual audience and supported browsers. Also test at least one narrow/short viewport and one landscape phone viewport for interactive experiences. Test split-screen or resized windows where relevant.

### 3. Build resilient layout primitives

- Use flexible containers such as `width: 100%`, `max-width`, CSS Grid, Flexbox, `minmax(0, 1fr)`, and intrinsic sizing.
- Prefer `clamp()`, relative units and content-based sizing for typography, spacing and component dimensions.
- Set `min-width: 0` on grid/flex children where long content could force overflow.
- Use `min-height` rather than fixed heights for content sections; allow text, localization and validation messages to expand.
- Define a small, intentional breakpoint system based on where the content stops fitting. Do not add a breakpoint for every device model.
- Keep readable line lengths and avoid excessively wide forms, cards and text blocks.
- Ensure images, video, SVG, tables, code, charts and embedded content scale or have an intentional contained overflow strategy.
- Check long labels, translated strings, large numbers, empty states and validation errors.
- Do not solve overflow by applying `overflow-x: hidden` to the whole page; find and correct the element causing it.

### 4. Handle mobile browser and PWA viewport behavior

- Include a correct viewport meta tag and preserve user zoom; do not disable pinch zoom.
- Account for notches and system areas with `env(safe-area-inset-*)` where edge-to-edge layouts require it.
- Use dynamic viewport units such as `dvh`/ `svh` with appropriate fallbacks when browser chrome changes available height. Avoid assuming `100vh` is always the visible mobile viewport.
- Ensure fixed/sticky headers, footers, bottom navigation, install prompts and floating controls do not obscure content or each other.
- For forms, test focus and virtual keyboard behavior; keep the active field and submit action reachable when the keyboard opens.
- Respect orientation changes without requiring a reload unless the product has a documented, justified restriction.
- Test installed PWA display mode as well as browser-tab mode when installability is part of the product.
- Verify scroll containers, overscroll behavior and safe-area padding on actual mobile browsers.

### 5. Make touch and pointer interactions reliable

- Provide touch targets around 44 × 44 CSS pixels where practical; never make essential controls difficult to hit.
- Use spacing between adjacent destructive or high-impact controls.
- Use `@media (hover: hover) and (pointer: fine)` for hover-only enhancements; never make hover the only way to discover or activate an action.
- Support touch, mouse and keyboard where the product's interaction model requires them.
- Use suitable `touch-action` only where necessary; do not block normal page scrolling or browser gestures indiscriminately.
- Prevent accidental double activation and ensure pressed, selected, disabled, focus and error states are visible.
- Avoid tiny icon-only controls without accessible names and adequate hit areas.

### 6. Special rules for games and interactive PWAs

- Treat the playable area as a constrained responsive system, not an ordinary content card.
- Calculate board/grid dimensions from the available container and viewport space. Keep cells, hit targets, labels and gestures usable at the smallest supported size.
- Preserve board aspect ratio where required, but allow the surrounding layout to reflow. Do not force a board to overflow just to preserve desktop dimensions.
- On short screens and landscape phones, prioritize the play area and keep score, instructions, controls and navigation reachable. Move secondary information into collapsible or stacked regions when needed; do not hide essential controls.
- Test every interaction at phone and tablet widths: taps, drags, swipes, selection, keyboard input, modals, restart/undo, hints and completion states as applicable.
- Avoid relying on hover, right-click, fine pointer movement or keyboard-only controls for core gameplay.
- If a game uses canvas/WebGL/SVG, scale the rendering surface and coordinate mapping together. Keep device-pixel-ratio handling bounded to avoid excessive memory/GPU use, and verify hit testing after resize/orientation changes.
- Recompute layout on container resize as well as window resize when embedded/resizable game surfaces are used.
- Test overlays, celebration effects, dialogs and bottom actions against safe areas and the on-screen keyboard. Animations must not block interaction.
- Never change game rules, scoring, persistence, API contracts or authoritative game logic as a side effect of responsive remediation.

### 7. Accessibility and motion

- Preserve semantic HTML, logical reading order, visible focus and keyboard operation.
- Ensure text remains usable at browser zoom and larger text settings; do not lock font scaling.
- Check contrast and avoid conveying state by colour alone.
- Respect `prefers-reduced-motion`; provide a reduced or non-animated alternative for non-essential movement.
- Ensure responsive reordering does not create a mismatch between visual and screen-reader order.
- Test labels, focus behavior and accessible names for controls that change presentation at different breakpoints.

### 8. Verify with automation and real devices

Use the project's existing tooling first (typically Playwright, browser devtools, screenshot tests or equivalent). Do not add a new dependency unless justified.

For each affected route:
- capture screenshots at the agreed viewport matrix;
- assert document-level horizontal overflow is absent, unless explicitly intended;
- inspect bounding boxes for clipped, overlapping or off-screen primary controls;
- exercise critical flows, not just initial page load;
- test portrait and landscape for touch-first experiences;
- verify resize and orientation changes do not leave stale dimensions or broken hit areas;
- check console errors and failed assets;
- test at least one real iOS Safari device and one real Android Chrome device when those platforms are in scope; include a tablet, ideally the actual target tablet, before release.

Example Playwright checks (adapt selectors and routes to the project):

```ts
import { test, expect } from '@playwright/test';

const viewports = [
  { width: 320, height: 640 },
  { width: 360, height: 800 },
  { width: 390, height: 844 },
  { width: 430, height: 932 },
  { width: 600, height: 960 },
  { width: 768, height: 1024 },
  { width: 820, height: 1180 },
  { width: 1024, height: 768 },
];

for (const viewport of viewports) {
  test(`layout fits at ${viewport.width}x${viewport.height}`, async ({ page }) => {
    await page.setViewportSize(viewport);
    await page.goto('/your-route');
    await expect(page.locator('body')).toBeVisible();

    const dimensions = await page.evaluate(() => ({
      clientWidth: document.documentElement.clientWidth,
      scrollWidth: document.documentElement.scrollWidth,
    }));

    expect(dimensions.scrollWidth).toBeLessThanOrEqual(dimensions.clientWidth + 1);
  });
}
```

This is a smoke test, not proof of visual quality. Pair it with screenshots, bounding-box checks and interaction tests. Avoid blanket assertions that hide intentional, contained horizontal scrollers.

## Outputs

- Responsive implementation or a prioritized defect list and remediation plan.
- Documented supported viewport/browser matrix and any justified exceptions.
- Updated responsive components/tokens without unnecessary duplication.
- Automated viewport/interaction tests or a clear explanation of unavailable tooling.
- Before/after screenshots for representative phone and tablet sizes.
- Real-device validation notes, including device/browser/orientation and any remaining limitations.

## Quality checks

Do not mark responsive work complete until

- [ ] Small phone, typical phone, large phone and tablet portrait layouts are checked.
- [ ] Tablet landscape and a short/landscape phone viewport are checked for interactive apps.
- [ ] No unintended page-level horizontal scrolling, clipped content or overlapping primary controls remains.
- [ ] Navigation, forms, dialogs, sticky elements and bottom actions remain reachable.
- [ ] Core interactions work with touch; no essential hover-only behavior exists.
- [ ] Game boards/canvases remain playable and resize correctly after orientation or container changes.
- [ ] Safe areas, browser chrome and virtual keyboard behavior are considered.
- [ ] Zoom, keyboard focus, readable text and reduced-motion behavior are preserved.
- [ ] Automated checks and screenshots are attached or referenced; real-device checks are recorded when devices are in scope.
- [ ] Existing product logic, game rules, API contracts and persistence behavior are unchanged unless explicitly approved.
- [ ] Known exceptions are documented with impact and rationale; no claim of universal device support is made without evidence.

## Boundaries

- Do not assume a screenshot at one width proves responsiveness.
- Do not make every page a scaled-down desktop layout.
- Do not fix overflow by clipping content or hiding essential controls.
- Do not add arbitrary breakpoints without identifying the content/layout constraint.
- Do not sacrifice accessibility, browser zoom or normal touch scrolling.
- Do not rewrite stable business logic, game mechanics or API contracts during a layout-only task.
- Do not claim validation on physical devices that were not actually tested.
- Coordinate with UX/UI Engineering for design decisions and Quality Assurance for broader regression/release gates; this skill owns responsive implementation and viewport-specific evidence.
