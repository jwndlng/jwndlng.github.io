# Design

## Context

The site is a Hugo static site using PaperMod. Its main navigation is configured in `hugo.toml`, while the homepage template lists posts and displays the home intro. The Projects page can use Hugo's standard content and section rendering without changing the homepage.

## Goals / Non-Goals

**Goals:**
- Add a standalone page at `/projects/` and make it discoverable in the main menu.
- Keep project summaries and repository links as simple page content.

**Non-Goals:**
- Add project-specific detail pages, filtering, or dynamic repository data.
- Change the homepage post listing or introduce a new theme component.

## Decisions

- Create `content/projects.md` as a regular Hugo page. Hugo renders it through the existing default single-page layout, which supports a straightforward heading and list of project summaries.
- Add a `Projects` entry to `menu.main` in `hugo.toml`. This follows the existing `Posts` and `Search` navigation pattern and lets Hugo resolve the page URL consistently.
- Keep summaries in Markdown and use direct GitHub links to the provided repositories. This avoids custom data structures or external dependencies for three stable entries.

## Risks / Trade-offs

- Concise summaries may omit project details → Keep descriptions factual and limited to the basic overview requested; richer project pages can be added later.
- A content filename or menu URL could drift from the intended route → Use Hugo's conventional `projects` slug and verify the built page and navigation link resolve to `/projects/`.
