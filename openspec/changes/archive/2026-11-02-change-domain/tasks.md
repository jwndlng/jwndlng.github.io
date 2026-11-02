# Tasks

## 1. Update Hugo site configuration and content

- [x] 1.1 Set `baseURL` in `hugo.toml` to `https://wndlng.ch` and verify the configured value is exactly the apex origin.
- [x] 1.2 Change `CNAME` to `wndlng.ch` and verify it contains only the intended custom domain.
- [x] 1.3 Rewrite the closing introduction in `content/_index.md` to frame this as a personal website with writing/posts, then verify the page no longer describes the whole site as a blog.
- [~] 1.4 Build the Hugo site and inspect canonical links, RSS, sitemap, search JSON, and post permalinks to confirm generated absolute site URLs use `https://wndlng.ch` and existing post paths remain unchanged. Local Hugo build succeeded; RSS and sitemap URLs use the apex origin and `/posts/welcome/` remains unchanged. Hugo emitted no `index.json` or post HTML and warned their layouts are missing. Check the deployed build includes working search JSON and post page canonical metadata at `https://wndlng.ch/posts/welcome/`.

## 2. Configure and verify domain migration

- [~] 2.1 Set apex and `www` DNS records for the chosen GitHub Pages configuration and verify both hostnames resolve as intended. In your DNS provider, set the apex A/AAAA records to GitHub Pages' current published values and `www` as a CNAME to the GitHub Pages hostname; then check DNS resolution for both `wndlng.ch` and `www.wndlng.ch`.
- [~] 2.2 Set the GitHub Pages custom domain to `wndlng.ch`, enable HTTPS, and verify the apex site serves successfully over HTTPS. In the repository's Settings → Pages, set custom domain to `wndlng.ch`, enable Enforce HTTPS once available, and open `https://wndlng.ch` to confirm it loads without a certificate error.
- [~] 2.3 Configure an HTTPS redirect for `blog.wndlng.ch` that preserves paths and query strings, then verify a post URL, `/index.xml`, and a URL with query parameters reach their corresponding apex URLs. Configure this at the DNS/hosting provider, then check `https://blog.wndlng.ch/posts/welcome/`, `https://blog.wndlng.ch/index.xml`, and a query URL such as `https://blog.wndlng.ch/posts/welcome/?source=check` for matching apex destinations with path and query retained.
- [~] 2.4 Verify the published homepage shows the personal website introduction above the existing post listing and that listed post links retain their existing paths. After publishing, open `https://wndlng.ch` and confirm the new intro appears above the post list and the post link still targets `/posts/welcome/`.
