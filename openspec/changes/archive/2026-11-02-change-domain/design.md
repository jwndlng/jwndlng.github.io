# Design

## Context

See proposal.md for motivation. The repository is a Hugo site using the PaperMod theme. `hugo.toml` sets `baseURL` to `https://blog.wndlng.ch`, `CNAME` contains that hostname, and `content/_index.md` contains the homepage introduction. Hugo templates use page permalinks for post links. GitHub Pages settings and DNS are external to this repository.

## Goals / Non-Goals

**Goals:**
- Make Hugo's configured base URL and the published Pages custom domain agree on `https://wndlng.ch`.
- Update only the homepage copy needed to establish personal-website framing while retaining the existing post list and URLs.
- Preserve legacy inbound links and feed subscriptions through an external host redirect.

**Non-Goals:**
- Add new site sections, change post URL structure, or redesign the theme.
- Manage DNS or GitHub repository settings from this repository.

## Decisions

- Set Hugo's `baseURL` to `https://wndlng.ch` and the Pages `CNAME` file to `wndlng.ch`. Hugo derives canonical and generated absolute URLs from the base URL, so this keeps page metadata, feeds, sitemap, and JSON output aligned.
- Keep the existing homepage content and layout, replacing the closing blog-centric paragraph with personal-website framing. The current `layouts/index.html` already renders the intro before the regular post list, so no layout change is needed.
- Configure `blog.wndlng.ch` redirection at the DNS/hosting layer outside this repository. The redirect service must preserve path and query string and support HTTPS for the legacy hostname. GitHub Pages custom-domain configuration covers one hostname per site and does not itself provide the required cross-host path-preserving redirect. Choose a redirect-capable provider/service as part of the deployment work, then validate representative post and feed URLs.
- Configure apex DNS records for GitHub Pages, retain the requested `www` alias behavior, and update the repository's Pages custom domain and HTTPS setting during deployment. The exact DNS values and redirect service settings are operational inputs and should be taken from the active provider's current guidance.

## Risks / Trade-offs

- [Legacy redirect is not deployed or does not preserve paths] → Configure and verify HTTPS redirects for post and feed paths before treating the domain move as complete.
- [DNS or Pages configuration is incomplete] → Coordinate DNS changes with the repository Pages custom domain update and verify the apex site and TLS after propagation.
- [External absolute URLs remain embedded in generated output] → Inspect a production build's canonical metadata, feed, sitemap, and JSON output after changing the base URL.

## Migration Plan

1. Update Hugo configuration, `CNAME`, and homepage copy in the repository.
2. Configure apex and `www` DNS and the GitHub Pages custom domain; enable HTTPS.
3. Configure `blog.wndlng.ch` as an HTTPS path- and query-preserving redirect to the apex domain.
4. Publish and verify the apex homepage, existing post paths, generated absolute URLs, and legacy redirects, including `/index.xml`.
5. If the new host fails, restore the prior Pages custom domain and `baseURL`; retain or repair the legacy redirect so inbound links remain reachable.
