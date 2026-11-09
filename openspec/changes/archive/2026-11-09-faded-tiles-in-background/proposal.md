# Proposal

## Why

The site currently uses a plain page background, so it lacks the subtle texture and depth requested for the personal site. A tiled background that is fully visible near the bottom and fades to transparency toward the top adds that detail while preserving the established color palette and readable content.

## What Changes

- Add a low contrast tile pattern behind the site content.
- Fade the pattern vertically so it is most visible at the bottom and transparent at the top.
- Preserve the current light and dark theme coloring and keep foreground content readable.

## Capabilities

### New Capabilities
- `site-background`: Defines the tiled background appearance and its fade behavior across themes.

### Modified Capabilities

## Impact

- CSS in `assets/css/extended/` and the site's shared page surfaces.
- No content model, routes, or external dependencies change.
