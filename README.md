# jwndlng.github.io

## Future Ideas

### Blog comments via GitHub Issues

Display comments on blog posts using GitHub's public API, with no third-party apps or OAuth.

**How it would work:**

1. A GitHub Actions workflow automatically creates a new Issue when a post is published (triggered by push to `content/posts/`)
2. The workflow writes the Issue number back to the post's front matter as `github_issue: <number>`
3. A small JS script on each post fetches comments from `GET /repos/jwndlng/jwndlng.github.io/issues/{number}/comments` (public API, no auth)
4. Comments are rendered inline below the post
5. A "Leave a comment" link points directly to the Issue on GitHub — readers comment there natively

**Pros:** Zero dependencies, no OAuth, no third-party apps, full control, GitHub-native moderation (close/lock/delete)

**Cons:** Readers must go to GitHub to comment, comments may be slightly delayed (API caching)