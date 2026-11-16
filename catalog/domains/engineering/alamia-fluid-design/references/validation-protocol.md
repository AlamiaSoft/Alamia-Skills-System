# Responsive validation protocol

Use this protocol on the actual rendered application. Source inspection cannot establish visual correctness.

## 1. Establish the test target

Record the URL/build/commit, browser and version, operating system, device/emulation mode, supported minimum viewport, and test tooling. Reuse existing project automation where possible; do not add a mandatory browser dependency without approval.

## 2. Viewport matrix

Test the narrowest supported width, representative widths, and widths immediately around each meaningful layout transition.

Suggested baseline widths (CSS pixels):
`280, 320, 360, 375, 390, 430, 600, 768, 900, 1024, 1280, 1440, 1920, 2560, 3840`.

Also test portrait and short landscape (for example 320×480 and 844×390), narrow split-screen/container widths, just below and above each content-driven breakpoint, 200% browser zoom or equivalent narrow effective CSS viewport, and large text where supported.

This is a sampling plan, not a claim that every possible width has been tested.

## 3. Layout and overflow checks

At relevant widths:
- Compare document `scrollWidth` with `clientWidth`; investigate unexpected horizontal overflow.
- Inspect nested grid/flex children, tables, charts, menus, dialogs, and long strings independently.
- Confirm intentional horizontal scrollers are bounded to their component and operable.
- Verify sticky/fixed elements do not cover content, focus, or primary actions.
- Check content order, truncation, wrapping, and useful control sizes.

Browser devtools diagnostic:

```js
({
  viewportWidth: document.documentElement.clientWidth,
  documentScrollWidth: document.documentElement.scrollWidth,
  hasHorizontalOverflow:
    document.documentElement.scrollWidth > document.documentElement.clientWidth,
  overflowingElements: [...document.querySelectorAll('body *')]
    .filter((el) => {
      const style = getComputedStyle(el);
      return el.getBoundingClientRect().width > 0 &&
        el.scrollWidth > el.clientWidth + 1 &&
        !['auto', 'scroll'].includes(style.overflowX);
    })
    .slice(0, 30)
    .map((el) => ({
      tag: el.tagName,
      id: el.id,
      className: typeof el.className === 'string' ? el.className : '',
      clientWidth: el.clientWidth,
      scrollWidth: el.scrollWidth
    }))
});
```

This is a diagnostic aid, not a substitute for visual inspection; some components intentionally scroll internally.

## 4. Interaction and accessibility checks

Exercise keyboard-only navigation, focus order and visibility, menus/drawers/dialogs, touch targets, software keyboard behavior, 200% zoom, text enlargement, reduced motion, forced colors, semantics, labels, table headers, accessible names, status announcements, and contrast. Verify that meaning is not communicated by color alone.

## 5. Runtime checks

- Review browser console errors and failed critical assets.
- Exercise loading, empty, error, success, and unusually long content states.
- Check behavior after resize/orientation change and after opening overlays.
- For PWAs, test standalone mode and safe-area behavior on supported devices.

## 6. Evidence and reporting

Capture screenshots at the narrowest supported width, common mobile, tablet/split-pane, desktop, ultrawide (when claimed), and around structural transitions.

Report viewport, scenario, result, and evidence reference. Record browser/tool versions and untested cases. Use status terms precisely:
- **Passed**: directly exercised and observed with a recorded method/evidence.
- **Failed**: a reproducible issue remains.
- **Not tested**: no direct validation was performed.
- **Not applicable**: explain why it does not apply.

Never describe an implementation as fully validated, cross-browser proven, or production-ready based only on CSS inspection, a static screenshot, or a successful build.
