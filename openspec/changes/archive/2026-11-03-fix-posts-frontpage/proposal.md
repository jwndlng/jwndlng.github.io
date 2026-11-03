# Proposal

## Why

The frontpage is reported to display projects in place of posts. Visitors need the writing list to remain reliable as other sections grow; the existing homepage requirement does not explicitly exclude other content.

## What Changes

- Restrict the homepage post list to published posts, excluding projects and other sections.
- Keep existing post links, ordering, visibility filtering, pagination, and introduction behavior.
- Verify the rendered homepage with mixed content and multiple pages of posts, while preserving the dedicated Projects page.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `homepage`: Clarify that the homepage post listing contains only eligible posts, including across pagination and when no posts are available.

## Impact

The intended fix is an explicit `params.mainSections` setting in `hugo.toml`, consumed by `layouts/index.html` and the home branch of `layouts/_default/list.html`. Verification covers generated homepage HTML and the Projects page. No new dependencies, content migrations, URL changes, or theme upgrade are planned.
