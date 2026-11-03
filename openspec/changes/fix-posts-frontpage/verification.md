# Verification

Verified locally with Hugo v0.168.0 and the existing pinned PaperMod revision `3bb0ca281fd17eff8e3489011a444f326d7c4c72`.

## Commands and results

- Baseline: `hugo --minify --destination /private/tmp/fix-posts-frontpage-baseline --cacheDir /private/tmp/fix-posts-frontpage-cache`. Homepage article links were `/projects/benny-watchman/`, `/projects/spec-control/`, and `/projects/cert-manager-plesk-webhook/`, reproducing the reported bug.
- After configuration fix: `hugo --minify --destination /private/tmp/fix-posts-frontpage-fixed --cacheDir /private/tmp/fix-posts-frontpage-cache`. Homepage article link was only `/posts/welcome/`; the personal introduction and Posts/Projects navigation remained present.
- `python3 /private/tmp/verify-fix-posts-frontpage.py`: temporary HTMLParser-based assertions checked the production output and an isolated source copy. All checks passed:
  - Posts page links to the welcome post and its generated destination exists.
  - Projects page retains all three summaries and corresponding repository links.
  - Thirteen eligible posts appear in descending date order across two homepage pages, with working pagination links; a draft and a homepage-hidden post are excluded.
  - With all posts removed and projects retained, the homepage has no article entry links and does not fall back to projects.
- `openspec validate fix-posts-frontpage --strict` and `git diff --check` passed.

Fixtures and the verification script were temporary and are not part of the site source. Output directories are outside the repository. The theme revision, content URLs, and deployment workflow are unchanged.

## Existing environment observations

Hugo 0.168.0 uses a page size of 10 with this site's legacy `paginate = 5` setting. The pagination fixture therefore used thirteen eligible posts to exercise both pages. This existing configuration behavior was left unchanged. Builds also emit existing language configuration/template deprecation warnings; builds succeed.

No user-only verification or account actions are required by these tasks.
