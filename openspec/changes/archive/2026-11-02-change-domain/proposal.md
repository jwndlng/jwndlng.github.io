# Proposal

## Why

The site is currently positioned and hosted as a blog at `blog.wndlng.ch`. I want it to be my personal website, served from the apex domain `wndlng.ch`, with the blog as one part of it rather than the whole identity. Doing this now, while there is only a single post, keeps the cost of breaking or redirecting existing links minimal.

## What Changes

- Serve the site from `https://wndlng.ch` instead of `https://blog.wndlng.ch` (Hugo `baseURL`, `CNAME`, GitHub Pages custom domain, DNS).
- All generated absolute URLs (canonical links, RSS feed, sitemap, search index JSON, permalinks) use `https://wndlng.ch`.
- **BREAKING**: `blog.wndlng.ch` is no longer the primary host. Requests to it SHALL be redirected to the same path on `wndlng.ch` so existing links and RSS subscriptions keep working.
- Reframe the homepage intro from "This blog is about…" to wording that presents the site as a personal website that includes writing/posts.
- Out of scope: new pages (about, projects, CV), visual redesign, and changing the URL structure of posts (`/posts/<slug>/` stays).

## Capabilities

### New Capabilities
- `site-domain`: Which domain the site is served from, how absolute URLs are generated, and how the legacy `blog.wndlng.ch` host behaves.
- `homepage`: How the homepage presents the site (personal-website framing, intro content, post listing).

### Modified Capabilities
<!-- None: no specs exist yet under openspec/specs/. -->

## Impact

- `hugo.toml`: `baseURL` changes to `https://wndlng.ch`.
- `CNAME`: changes to `wndlng.ch`.
- `content/_index.md`: intro copy no longer describes the site as "this blog".
- GitHub repository settings → Pages: custom domain changes to `wndlng.ch`, HTTPS enforced (external, manual).
- DNS for `wndlng.ch`: apex `A`/`AAAA` records to GitHub Pages; `www` CNAME; a redirect solution for `blog.wndlng.ch` (external, manual).
- RSS subscribers on `blog.wndlng.ch/index.xml` rely on the legacy redirect.
