# Spec Delta

## Purpose

Defines the site's decorative page background, including its tile pattern, vertical fade, and relationship to the active theme. It keeps the background subtle while preserving the site's existing colors and content legibility.

## ADDED Requirements

### Requirement: Tiled page background
The site SHALL display a subtle repeating tile pattern behind page content while preserving the existing theme color palette.

#### Scenario: View site with light theme
- **WHEN** a visitor views any page using the light theme
- **THEN** the page shows the tile pattern in the existing light palette behind readable content

#### Scenario: View site with dark theme
- **WHEN** a visitor views any page using the dark theme
- **THEN** the page shows the tile pattern in the existing dark palette behind readable content

### Requirement: Background fades toward top
The tile pattern SHALL be most visible at the bottom of the page and fade to transparent toward the top.

#### Scenario: View lower page background
- **WHEN** a visitor views the lower portion of a page
- **THEN** the tile pattern is visible at its normal subtle contrast

#### Scenario: View upper page background
- **WHEN** a visitor views the upper portion of a page
- **THEN** the tile pattern gradually fades and becomes transparent toward the top
