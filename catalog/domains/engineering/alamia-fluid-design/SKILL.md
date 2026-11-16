---
name: alamia-fluid-design
description: >-
  Design and build web pages, Progressive Web Apps (PWAs), and web applications that fluidly adapt across any screen size (from 280px foldables to 4K+ ultrawides) using CSS clamp typography, fluid spacing ladders, container queries, and intrinsic layouts.
license: MIT
metadata:
  type: specialist-capability
  category: engineering
  domain: product-engineering
  version: "1.1.0"
---

# Alamia Fluid Design

## Purpose
Design, architect, and engineer frontend user interfaces, web applications, PWAs, and design systems that seamlessly adapt to **any screen size, aspect ratio, orientation, and resolution** (from 280px foldables to 3840px+ 4K ultrawides) without breakpoint snapping, layout blowout, or horizontal scroll.

## Activation
Trigger this skill whenever designing or implementing responsive layouts, fluid web interfaces, PWAs, mobile-first dashboards, or adapting frontend code across diverse viewports.

## Inputs
- Application wireframes, UI mockups, or component specifications.
- Product requirements: target surfaces (mobile, PWA, tablet, desktop, ultrawide).
- Design tokens: typography choices, color palette, surface materials.
- Interaction constraints: touch pointers, software keyboards, hardware hinges.

## Procedure
1. **Establish Fluid Scale Functions (CSS `clamp()` Curves)**:
   - Calculate typography and spacing using continuous linear interpolation between minimum viewport ($W_{\min} = 320\text{px}$) and maximum viewport ($W_{\max} = 1800\text{px}$):
     $$\text{font-size} = \text{clamp}(y_{\min},\; \text{calc}(y_{\min} + \text{slope} \times (100\text{vw} - W_{\min})),\; y_{\max})$$
   - Never use static `px` values for typography or section padding.
2. **Implement Intrinsic Zero-Breakpoint Grids**:
   - Build card and content grids using auto-fit:
     ```css
     .fluid-grid {
       display: grid;
       grid-template-columns: repeat(auto-fit, minmax(min(100%, var(--grid-min-item, 280px)), 1fr));
       gap: var(--space-md);
       min-width: 0;
       width: 100%;
     }
     ```
   - Enforce `.fluid-grid > * { min-width: 0; max-width: 100%; }` to prevent child min-content blowout.
3. **Declare Container Queries (`@container`) for Context-Aware Components**:
   - Set `container-type: inline-size` on cards, sidebars, and panels.
   - Reflow component layout based on available parent container width, not global viewport width.
4. **Align Multi-Column Card Rows via CSS Subgrid**:
   - Apply `grid-template-rows: subgrid; grid-row: span 3;` on cards so titles, descriptions, and action buttons align horizontally across columns regardless of copy length.
5. **Configure Mobile & PWA Ergonomics**:
   - Include `<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover, interactive-widget=resizes-content">`.
   - Use `100dvh` for full-height shells to prevent mobile URL bar layout thrashing.
   - Bind notch insets: `max(var(--space-sm), env(safe-area-inset-bottom))`.
   - Enforce 44×44px minimum tap target sizes on touchscreens (`@media (pointer: coarse)`).
6. **Apply Edge-Case Defenses**:
   - Defend against short landscape heights ($\le 480\text{px}$) by compacting header/footer padding.
   - Handle dual-screen hinges via `@media (horizontal-viewport-segments: 2)`.
   - Support High Contrast Mode via `@media (forced-colors: active)`.

## Outputs
- Reusable design token stylesheet (`tokens.css`).
- Universal fluid responsive layout stylesheet (`fluid-engine.css`).
- Viewport and container measurement engine (`fluid-engine.js`).
- Working, fully validated responsive templates and components (PWA games, dashboards, configurators).

## Quality checks
- [ ] No horizontal scrollbars appear on any screen width between 280px and 3840px.
- [ ] Text maintains optimal reading line length (50–75 characters, `max-width: 65ch`) on wide displays.
- [ ] Mobile virtual keyboard does not obscure action buttons or sticky inputs (`interactive-widget=resizes-content`).
- [ ] Interactive touch elements meet WCAG 2.2 AA (24px min) and AAA (44px min) target size standards.
- [ ] Data tables and SVG charts scroll or resize within their own containers without blowing out grid tracks (`min-width: 0`).

## Boundaries
- Do not use fixed pixel widths (`width: 1200px`) on main layout wrappers.
- Do not hide critical content or functionality on mobile simply because of space constraints.
- Do not write media queries every 50px—rely on mathematical interpolation and container queries.
- Do not ignore notch safe-area insets on mobile/standalone PWA apps.
