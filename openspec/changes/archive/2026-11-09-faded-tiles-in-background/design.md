# Design

## Context

The site uses Hugo with PaperMod and loads shared styles from `assets/css/extended/`. Theme colors are exposed through CSS variables, and `polish.css` already has global body and list styling. See proposal.md for motivation and `specs/site-background/spec.md` for the behavior contract.

## Goals / Non-Goals

**Goals:**
- Add a decorative pattern behind content across site pages.
- Respect the active light or dark theme and fade the pattern vertically.
- Keep the implementation small, local to the existing CSS layer, and independent of assets.

**Non-Goals:**
- Change theme palettes, page layout, content, or theme switching.
- Add animation, user controls, or a new background image asset.

## Decisions

- Implement the tiles as a low-contrast repeating CSS pattern in a pseudo-element attached to the page background. This allows a vertical CSS mask to fade only the decoration while leaving page content and the base theme color untouched. A raster image would add an asset and could become blurry or mismatched across screen sizes; a body mask would also fade content and is unsuitable.
- Derive the tile color from the active foreground/theme variables with low opacity, so the same pattern follows both theme modes without hardcoding a second palette. Keep the pseudo-element non-interactive and behind page content.
- Keep the pattern and fade in `assets/css/extended/polish.css`, which already owns global body refinements. Avoid template changes because the effect is decorative and applies across pages.

## Risks / Trade-offs

- [Pseudo-element stacking can place decoration above or below theme surfaces unexpectedly] → Keep it behind page content, set it non-interactive, and inspect representative pages in both themes during implementation.
- [Mask support can vary in older browsers] → Treat the pattern as progressive enhancement; if masking is unavailable, retain a very subtle pattern rather than compromising content visibility.

## Migration Plan

No migration is required. Deploy the stylesheet with the site; rollback by removing the background pseudo-element rules.
