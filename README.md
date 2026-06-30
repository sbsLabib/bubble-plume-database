# Bubble Plume Data Repository

This repository contains a one-page GitHub Pages data catalog for the Bubble Plume Data Repository. The site provides DOI links, paper-level CSV/XLSX downloads, and reproducible plotting resources for selected bubble plume publications.

The website is intentionally built with plain HTML and CSS so it can be hosted directly with GitHub Pages. No build tools or programming frameworks are required.

## Project files

- `index.html` contains the one-page public website and data catalog.
- `style.css` contains the colors, spacing, responsive layout, and other visual styles.
- `notebooks/reproducible_plots.ipynb` contains the notebook-only reproducible plotting workflow.
- `figures/reproducible_plots/` contains static PNG figures generated from the paper-level master CSV files.
- `requirements.txt` lists the Python packages needed for the plotting workflow.
- `AGENTS.md` contains project instructions for future Codex tasks.
- `LICENSE` contains the repository license.
- `csv/paper_data_downloads/` contains the public paper-level CSV and XLSX downloads.
- `csv/archive_source_files/` contains older split CSV folders and source/development files retained for provenance.

There is no JavaScript file yet because the current homepage does not need one.

The public website is intended to work as a single page. Older secondary pages may remain in the repository for reference, but users should not need them to find DOI links, data downloads, or plotting resources.

## Paper data downloads

Public data files live under `csv/paper_data_downloads/`.

Each paper should provide:

- one official CSV file in `csv/paper_data_downloads/csv/papers/`;
- one formatted XLSX file in `csv/paper_data_downloads/xlsx/papers/`.

CSV files are intended for reproducible analysis in scripts, notebooks, and other machine-readable workflows. XLSX files are formatted companion workbooks for human inspection and include a Details sheet plus a Data sheet.

Older split CSV folders are source/development files. They may be retained in `csv/archive_source_files/`, but they are not the main public downloads.

Current public paper downloads include:

- `csv/paper_data_downloads/csv/papers/milgram_1983.csv`
- `csv/paper_data_downloads/xlsx/papers/milgram_1983.xlsx`
- `csv/paper_data_downloads/csv/papers/li_2020.csv`
- `csv/paper_data_downloads/xlsx/papers/li_2020.xlsx`
- `csv/paper_data_downloads/csv/papers/wang_lai_socolofsky_2019.csv`
- `csv/paper_data_downloads/xlsx/papers/wang_lai_socolofsky_2019.xlsx`
- `csv/paper_data_downloads/csv/papers/kobus_1968.csv`
- `csv/paper_data_downloads/xlsx/papers/kobus_1968.xlsx`

The Wang et al. 2019 CSV contains nondimensional weak bubble plume data blocks for:

- Figure 8: `Um/Us` vs `z/D`
- Figure 10: `alpha` vs `z/D`
- Figure 11: `b_g/D` vs `z/D`
- Figure 12a: `Q_hat` vs `z/D`
- Figure 12b: `M_hat` vs `z/D`

The Kobus 1968 CSV currently contains single-orifice data blocks for:

- Figure 4: centerline velocity above a single orifice
- Figure 6: velocity profiles above a single orifice
- Figure 13: volume flux ratio for a single orifice

## Reproducible plotting

Install the plotting requirements from the repository root:

```bash
pip install -r requirements.txt
```

Open the notebook for inspection, modification, and rerunning:

```bash
jupyter notebook notebooks/reproducible_plots.ipynb
```

The notebook reads data from `csv/paper_data_downloads/csv/papers/` and saves figures to `figures/reproducible_plots/`.

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

This repository currently contains a one-page static data catalog, paper-level CSV/XLSX downloads, and a reproducible plotting workflow. Planned later work includes:

- defining a consistent metadata template;
- adding paper summaries and source information;
- creating simple browsing and filtering tools; and
- adding an interactive dataset comparison tool.

These features should be added gradually. The project should remain understandable to researchers who are new to web development.
