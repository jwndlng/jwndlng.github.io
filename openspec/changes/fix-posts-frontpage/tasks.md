# Tasks

## 1. Explicit homepage selection

- [x] 1.1 Initialize the pinned PaperMod submodule if missing and run a baseline production Hugo build into temporary output; record the homepage article entry URLs to confirm the reported section-selection failure or document any discrepancy.
- [x] 1.2 Set `mainSections = ["posts"]` directly under `[params]` in `hugo.toml`; rebuild with `hugo --minify` using temporary output and verify the homepage lists `/posts/welcome/`, excludes project article entries, and retains its introduction and existing post URL.
- [x] 1.3 Validate the homepage spec scenarios in an isolated fixture copy: retain projects while adding more than five eligible posts, a draft, and a hidden post; verify all pagination pages contain only eligible posts in the existing ordering. Repeat with zero eligible posts and verify no projects replace them. Record commands and results without committing fixture content or generated output.

## 2. Site integration

- [x] 2.1 Inspect the production build's `/posts/` and `/projects/` pages; verify the post remains reachable and all three featured projects retain their summaries and repository links, and confirm the homepage navigation still reaches both sections.
- [x] 2.2 Review the final diff and build results; verify only the intended selection fix and any necessary regression support are included, with no theme revision, content URL, or deployment workflow changes.
