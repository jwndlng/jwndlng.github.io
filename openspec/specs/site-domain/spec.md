# Site Domain

## Purpose

Defines the canonical domain for the personal website, the hostnames used in generated absolute URLs, and the behavior expected from the retired blog subdomain.

## Requirements

### Requirement: Canonical site domain
The published site SHALL use `https://wndlng.ch` as its canonical origin. Generated canonical links, RSS feeds, sitemap entries, search index URLs, permalinks, and other absolute site URLs SHALL use that origin.

#### Scenario: Generated absolute URLs use the apex domain
- **WHEN** the site is built for publication
- **THEN** its generated absolute site URLs use `https://wndlng.ch`

### Requirement: Legacy blog host redirects
Requests to `blog.wndlng.ch` SHALL redirect to `https://wndlng.ch` while preserving the requested path and query string.

#### Scenario: Redirect a post URL
- **WHEN** a visitor requests a post path on `blog.wndlng.ch`
- **THEN** the visitor is redirected to the same path on `https://wndlng.ch`

#### Scenario: Redirect an RSS subscription URL
- **WHEN** a feed reader requests `/index.xml` on `blog.wndlng.ch`
- **THEN** it is redirected to `https://wndlng.ch/index.xml`

#### Scenario: Preserve query parameters
- **WHEN** a visitor requests a URL with a query string on `blog.wndlng.ch`
- **THEN** the redirect target retains that query string
