# Bubble Plume Data Repository

This repository contains the first homepage prototype for the Bubble Plume Data Repository. The project will eventually organize literature-based bubble plume datasets, paper synopses, experimental metadata, and tools for comparing compatible datasets.

The website is intentionally built with plain HTML and CSS so it can be hosted directly with GitHub Pages. No build tools or programming frameworks are required.

## Project files

- `index.html` contains the homepage text and page structure.
- `group.html` contains the research group page and its placeholder profiles.
- `papers/milgram_1983.html` contains the Milgram 1983 paper and dataset detail page.
- `papers/li_2020.html` contains the Li et al. 2020 paper and dataset detail page.
- `style.css` contains the colors, spacing, responsive layout, and other visual styles.
- `AGENTS.md` contains project instructions for future Codex tasks.
- `LICENSE` contains the repository license.
- `csv/milgram_1983_cleaned/` contains the cleaned Milgram83 literature-comparison CSV files.
- `csv/li_2020_complete_cleaned/` contains the complete cleaned Li et al. 2020 datasets, separated into air-stone and single-orifice cases.

There is no JavaScript file yet because the current homepage does not need one.

## Preview the website locally

For a quick preview, open `index.html` in a web browser.

If you have Python installed, you can instead run a small local web server from the repository folder:

```bash
python -m http.server 8000
```

Then visit `http://localhost:8000` in your browser. Stop the server with `Ctrl+C` in the terminal.

## Publish with GitHub Pages

1. Push `index.html`, `style.css`, and the other project files to the `main` branch of a GitHub repository.
2. Open the repository on GitHub.
3. Select **Settings**, then select **Pages** in the sidebar.
4. Under **Build and deployment**, set **Source** to **Deploy from a branch**.
5. Select the `main` branch and the `/ (root)` folder.
6. Select **Save**.
7. Wait for GitHub to finish publishing, then use the website link shown on the Pages settings screen.

After later changes, push the updated files to `main`. GitHub Pages will publish them automatically.

## Current scope

This repository currently contains only the homepage prototype. Planned later work includes:

- defining a consistent metadata template;
- publishing representative CSV datasets;
- adding paper summaries and source information;
- creating simple browsing and filtering tools; and
- adding an interactive dataset comparison tool.

These features should be added gradually. The project should remain understandable to researchers who are new to web development.
