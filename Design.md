# Personal Website Design Document

This document outlines the design principles, visual style, and component structure for the personal website.

## 1. Design Philosophy

The primary goal is to create a website that is:

*   **Minimalist & Clean:** The design should be simple, uncluttered, and professional. The focus is on the content (resume and portfolio) without unnecessary distractions.
*   **Fast & Lightweight:** Built with Astro and custom CSS for optimal performance and a snappy user experience.
*   **Elegant & Modern:** A sophisticated and contemporary aesthetic that is easy to navigate.

## 2. Visual Design

### 2.1. Color Palette

The site uses a dark slate theme with a subtle rhombus grid background, designed for a modern and professional feel. Colors are managed via CSS variables for consistency.

*   **Primary Background (`--color-bg-primary`):** Dark Slate (e.g., `#1E293B`)
*   **Secondary Background (`--color-bg-secondary`):** Medium Slate (e.g., `#475569`)
*   **Text (`--color-text-primary`):** Light Slate (e.g., `#E2E8F0`)
*   **Accent Blue (`--color-accent-blue`):** A vibrant blue for interactive elements (e.g., `#60A5FA`)
*   **Accent Blue Hover (`--color-accent-blue-hover`):** A darker blue for hover states (e.g., `#3B82F6`)
*   **Nav Button Background (`--color-nav-button-bg`):** Darker Slate for navigation buttons (e.g., `#334155`)
*   **Nav Button Text (`--color-nav-button-text`):** Lighter Blue for navigation button text (e.g., `#BFDBFE`)

### 2.2. Typography

*   **Font:** 'agave monospace' will be used as the primary font for its clean, technical, and elegant look.
*   **Headings:** Clear and concise headings (`<h1>`, `<h2>`, etc.) will be used to structure content.
*   **Body Text:** Legible and well-spaced for readability.

### 2.3. Spacing

Consistent spacing is applied throughout the site using custom CSS.

## 3. Component Library

We will create a set of reusable components to ensure consistency.

*   **Navigation:** Floating arrow navigation positioned relative to the main content card, with text revealing on hover.
*   **Cards:** For portfolio items, a card component will be used to display a project image, title, and a brief description.
*   **Buttons:** Simple call-to-action buttons with a clear hover state (currently not used on the Home page).
*   **Timeline:** A component designed to display chronological events (e.g., education, experience).
    *   **Structure:** Items are displayed along a central vertical line with markers. Content alternates between left and right sides of the line.
    *   **Interactivity:** Item descriptions are initially collapsed and expand on hover, revealing full details.
    *   **Styling:** Uses `timeline.css` for dedicated styles, including a darker background for content cards (`--color-bg-primary`) and right-aligned timeframes for left-aligned content.
    *   **Scrolling:** The entire timeline card is scrollable (`max-height: 500px; overflow-y: auto;`) to accommodate extensive content without resizing the main page layout.
    *   **Responsiveness:** Adapts for smaller screens by aligning all content to the left of the timeline line.
*   **Skills:** A component to display a grid of technical skills, each with an associated logo.
    *   **Structure:** Skills are displayed in a responsive grid.
    *   **Visuals:** Each skill item includes a logo sourced from `shields.io`. The `skill-logo` class is styled to accommodate these badges (e.g., `height: 20px;`). The skill name is embedded within the badge itself. The background color of each skill pill now dynamically matches the color of its corresponding Shields.io badge, with the hex color code correctly prefixed with `#`.
    *   **Styling:** Uses `skills.css` for dedicated styles. The `skills-container ul` now uses `grid-template-columns: repeat(auto-fit, min-content)` to ensure pills size to their content. `skills-container li` has no padding and `display: inline-block` to tightly wrap the badges.

## 4. Page Layouts

### 4.1. Global Layout

All pages share a common layout (`Layout.astro`) that includes the main content area flanked by floating arrow navigation.

### 4.2. Home/Resume Page

*   This will be a single, combined page that serves as both the landing page and the resume.
*   It will feature a brief, scannable summary of skills and experience.
*   Includes the new Timeline component for displaying chronological education and experience.
*   Includes the new Skills component for showcasing technical proficiencies.

### 4.3. Portfolio Page

*   A grid-based layout to display portfolio project cards.