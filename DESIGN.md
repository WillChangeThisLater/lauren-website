# Visual Art Section Design

## Objective
Lay the foundation for a multimedia artist site focused on music, writing, and visual art. For now the primary deliverable is the Visual Art section, which should feel like a neutral gallery band that highlights 5–7 pieces with minimal friction for a non-technical author to update.

## Layout
- Single full-width band with a charcoal-neutral background and crisp white typography.
- Section intro (title + single sentence) that frames the art in the broader creative output.
- Responsive grid of art tiles (2–3 columns desktop, 1 column mobile) with consistent markup so new pieces are easy to add.
- Each tile displays a thumbnail, title, and medium; clicking opens a shared Micromodal lightbox with larger image, caption, and optional credits.
- Include a “Featured Series” hero callout beneath or adjacent to the grid for one highlighted project.

## Stack & Behavior
- Pure HTML/CSS baseline; avoid JavaScript frameworks or build tools for now.
- Include small dependencies only: Micromodal (or similarly minimal lightbox) and htmx only if direct dynamic swaps are needed later.
- Keep styling simple and neutral, using clean typography, soft spacing, and CSS variables to allow future tweaks.
- Lightbox content should be updated programmatically via a small vanilla script to keep markup DRY.

## Content Workflow
- Author updates should be manual HTML edits with clear copy/paste-ready tile blocks.
- Provide documentation (comments or nearby instructions) on how to add a new piece and how to configure the lightbox content.
- If the content set grows, plan to add a tiny script or data-driven templating step later so tiles can be driven from JSON/Markdown.

## Direction for Implementers
- Focus on delivering the Visual Art band as described; it should serve as a template for the eventual Music and Writing sections.
- Keep the codebase minimal and legible; future agents should be able to edit the section without understanding a complex stack.
- Document assumptions and corners where future expansion is expected (e.g., placeholder for “Featured Series” text or notes about future data flow).
