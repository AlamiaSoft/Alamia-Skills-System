# Responsive patterns

These patterns are decision guides. Select based on content, task priority, and available component width.

## Application shell and navigation

**Wide composition**
- Use a persistent sidebar only when it improves repeated navigation and does not compress the workspace.
- Use `minmax(0, 1fr)` for the main grid track and `min-width: 0` on nested panels.

**Narrow composition**
- Convert the sidebar into a labelled menu/disclosure, drawer, or compact navigation appropriate to the product.
- Preserve active-page context, keyboard access, focus order, and focus return.
- Keep primary actions visible. Do not rely on hover or visual reordering that conflicts with DOM reading order.

## KPI and metric cards

- Use intrinsic columns when each metric is independently understandable and has a known minimum useful width.
- Use container queries when a card can appear in different parent widths.
- Allow long values to wrap or scale conservatively; never clip values or shrink type excessively.
- Keep labels and units associated with values. Color must not be the only status indicator.

## Data tables

Choose deliberately:
1. **Bounded horizontal scroll** when column relationships matter. Give the region a visible boundary and keyboard access where needed.
2. **Priority columns** when secondary columns can be hidden without losing essential meaning. Never hide critical status or actions silently.
3. **Card/list transformation** when each row is a coherent record. Preserve labels in the transformed representation.

Do not apply page-level horizontal scrolling to compensate for a table. Scope scrolling to the table region.

## Charts and visualizations

- Bound the chart container with `min-width: 0` and a responsive block size.
- Preserve aspect ratio where it conveys meaning; use SVG viewBox scaling deliberately.
- Reduce tick density or provide a textual/data-table alternative rather than making labels microscopic.
- Provide an accessible name and summary; do not communicate meaning by color alone.

## Filters and toolbars

- Allow filters and actions to wrap naturally.
- On narrow screens, show the most-used filters first and place secondary filters in an explicit disclosure or sheet.
- Keep applied-filter state visible and provide a clear reset action.
- Ensure menus and popovers work with keyboard and touch.

## Forms and action areas

- Prefer one-column forms on narrow containers and group related fields semantically.
- Keep labels visible; placeholders are not labels.
- Associate validation messages with fields.
- Sticky/fixed action bars must respect safe areas, keyboard appearance, and focused-field visibility. Prefer normal document flow unless persistence is necessary.
- Test long labels, validation text, and enlarged text.

## Dialogs, drawers, and overlays

- Constrain overlay dimensions to the dynamic viewport and safe areas.
- Manage focus, Escape behavior, and focus return appropriately.
- On narrow screens, a full-height sheet may be appropriate, but it must not hide its close action or trap content behind the virtual keyboard.
- Avoid nested scroll regions unless behavior is clear and tested.

## Long content and localization

- Test long names, unbroken IDs, URLs, translated labels, empty states, and error messages.
- Use `overflow-wrap: anywhere` selectively for untrusted identifiers; do not globally break ordinary words.
- Avoid fixed heights for content cards unless clipping is an explicit, accessible decision.
