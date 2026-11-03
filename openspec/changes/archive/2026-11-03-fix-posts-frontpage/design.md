# Design

## Context

See proposal.md for the reported bug. This Hugo site uses PaperMod and a local `layouts/index.html` override. That template selects regular pages by `Type` from `site.Params.mainSections`, filters `hiddenInHomeList`, and paginates the result. The home branch in `layouts/_default/list.html` uses the same selection. `hugo.toml` has no explicit `mainSections`; the repository contains one post and three project entries. The dedicated Projects page has its own template.

The live URL could not be retrieved during planning, and the PaperMod submodule content is unavailable in this checkout. Consequently, automatic section selection is a likely cause rather than a reproduced diagnosis. A design is included to settle whether selection belongs in configuration or templates before implementation.

## Goals / Non-Goals

**Goals:** Make homepage content selection explicit and independent of relative section sizes, preserving the rendering and pagination pipeline.

**Non-Goals:** Change project discovery, search, feed policy, typography, post URLs, or content models; upgrade Hugo or PaperMod.

## Decisions

1. Set `mainSections = ["posts"]` directly under `[params]` in `hugo.toml`, before nested parameter tables. Both existing home selectors already consume this setting, so a configuration fix avoids duplicating policy in templates. Hardcoding a posts filter in each template is an alternative but introduces two places to maintain the same selection rule. Marking every project hidden would require authors to remember a flag on future entries and would not express a posts-only policy.
2. Preserve filtering before pagination and leave current sorting and entry rendering intact. Filtering after pagination could yield short or empty pages and displace posts. No template change is planned unless a rendered build demonstrates the existing selectors do not honor the configuration.
3. Verify generated HTML with production build settings. Use current content for the reported mixed-content case and temporary fixture content in an isolated copy for more than five posts, hidden/draft posts, and zero eligible posts. Check article entry links rather than all links, since navigation must still link to Projects. Keep fixtures and build output out of committed site content.

## Risks / Trade-offs

- [Theme behavior has not been reproduced locally] → Initialize the pinned theme submodule and compare production builds before and after the setting; confirm the resulting entry URLs.
- [A shared configuration parameter can affect theme consumers beyond the homepage] → Check `/posts/` and `/projects/` as well as the homepage; do not redefine feed or search behavior in this change.
- [An empty posts section might trigger unwanted fallback] → Build an isolated no-eligible-posts fixture and assert there are no project entries on the homepage.

## Migration Plan

No content migration is required. Build and validate locally, then use the existing GitHub Pages workflow when the implementation is merged. Rollback consists of reverting the configuration change and rebuilding the site.
