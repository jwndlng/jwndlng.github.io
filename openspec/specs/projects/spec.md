# projects Specification

## Purpose

Gives visitors a dedicated place to discover selected projects by Jan and follow links to their public source repositories.

## Requirements

### Requirement: Projects page discovery
The site SHALL provide a Projects page reachable from its main navigation.

#### Scenario: Navigate to projects
- **WHEN** a visitor uses the main navigation to open Projects
- **THEN** the site displays the Projects page

### Requirement: Featured project summaries
The Projects page SHALL list Benny Watchman, Spec Control, and the Plesk cert-manager webhook with a concise description for each.

#### Scenario: Review featured projects
- **WHEN** a visitor views the Projects page
- **THEN** all three named projects appear with concise descriptions

### Requirement: Project repository links
Each featured project SHALL link to its corresponding public GitHub repository.

#### Scenario: Open a project repository
- **WHEN** a visitor follows a featured project's repository link
- **THEN** the browser opens that project's corresponding GitHub repository
