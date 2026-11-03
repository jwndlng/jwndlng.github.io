# Spec Delta

## MODIFIED Requirements

### Requirement: Homepage post listing
The homepage SHALL show only published posts eligible for the homepage beneath the introduction, using their existing post URLs and ordering. Projects and other non-post content SHALL be excluded from every page of the list. Draft posts and posts hidden from the homepage SHALL remain excluded from the production homepage.

#### Scenario: View available posts
- **WHEN** a visitor opens the homepage with published posts available
- **THEN** the homepage lists those posts and links each one to its existing post URL

#### Scenario: Posts coexist with projects
- **WHEN** published posts and projects are available, including more projects than posts
- **THEN** the homepage post list contains eligible posts and no projects or other non-post entries

#### Scenario: Browse paginated posts
- **WHEN** eligible posts exceed the homepage page size and a visitor follows pagination
- **THEN** every page contains only eligible posts in the existing ordering, with no post displaced by a project

#### Scenario: No eligible posts
- **WHEN** projects exist but there are no posts eligible for the homepage
- **THEN** the homepage renders without post entries and does not substitute projects for posts

#### Scenario: Exclude unpublished or hidden posts
- **WHEN** draft posts or posts marked hidden from the homepage exist alongside eligible published posts
- **THEN** the production homepage lists only the eligible published posts
