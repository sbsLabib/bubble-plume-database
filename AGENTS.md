# Project instructions for Codex

## Project purpose

This repository is a GitHub Pages website for the Bubble Plume Data Repository. The long-term project will collect literature-based bubble plume research data, including CSV files extracted from publications, short paper synopses, experimental metadata, and an interactive plotting tool.

The intended audience includes professors, researchers, graduate students, and students working with bubble plumes, multiphase flows, environmental hydraulics, and related experimental datasets.

## Current scope

The repository is currently an early homepage prototype. Improve the homepage incrementally, but do not build the full database unless a later task explicitly requests it.

Preserve the existing homepage sections unless there is a clear content, usability, or accessibility reason to change them:

- About
- Data model
- Compare data
- Contributors
- Project roadmap

## Technical constraints

- Keep the website compatible with GitHub Pages.
- Use plain HTML, CSS, and JavaScript only.
- Do not add React, Next.js, npm, a bundler, a backend, or a database server.
- Do not require a build step for the homepage.
- Use relative paths for site files so project pages work correctly.
- Prefer a small number of clearly named files and folders.
- Add third-party libraries only when a requested feature truly needs one and a simpler browser-native solution is not reasonable.

## Code style

- Write semantic HTML with a logical heading order.
- Keep CSS selectors simple and reuse the custom properties in `:root` for colors and shared dimensions.
- Use descriptive class names such as `.section-heading` rather than presentation-only names such as `.large-blue-text`.
- Keep content readable without JavaScript whenever possible.
- Add comments only when they explain the purpose of a major structure or a non-obvious choice. Do not comment every line.
- Write for a maintainer who knows Python and MATLAB but is new to HTML, CSS, and JavaScript.

## Design and accessibility

- Keep the visual style academic, restrained, and professional.
- Test layouts at both desktop and mobile widths.
- Maintain readable font sizes, line lengths, spacing, and color contrast.
- Preserve keyboard navigation, visible focus indicators, meaningful link text, and the skip link.
- Include useful `alt` text if images are added. Decorative images should use empty alt text or be hidden from assistive technology.
- Respect reduced-motion preferences when adding animation.

## Content and research data

- Do not invent citations, datasets, measurements, contributors, funding sources, or institutional affiliations.
- Clearly distinguish current features from planned features.
- Keep source publication details, units, variable definitions, digitization notes, and experimental metadata connected to future datasets.
- Prefer open, documented formats such as CSV for tabular data.

## Before finishing a change

- Confirm that `index.html` opens without a build step.
- Check that internal navigation links point to unique section IDs.
- Check desktop and mobile layouts for overflow and awkward wrapping.
- Check that edited text files use UTF-8 and do not contain broken characters.
- Update `README.md` when setup, publishing, or the file structure changes.
- Summarize what changed and note any checks that could not be completed.
