from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def find_repo_root() -> Path:
    """Return repository root whether this is run from root, scripts/, or notebooks/."""
    cwd = Path.cwd()
    if (cwd / "csv").exists():
        return cwd
    if (cwd.parent / "csv").exists():
        return cwd.parent
    raise FileNotFoundError(
        "Could not find a csv/ folder. Run this script from the repository root "
        "or from the scripts/ folder inside the repository."
    )


REPO_ROOT = find_repo_root()
MASTER_CSV = REPO_ROOT / "csv" / "paper_data_downloads" / "csv" / "papers" / "li_2020.csv"
FIG_DIR = REPO_ROOT / "figures" / "literature_scaling"
FIG_DIR.mkdir(parents=True, exist_ok=True)

SERIES = {
    "Li2020 air stone": ("li2020_air_stone_x", "li2020_air_stone_y", "^"),
    "Li2020 single orifice": ("li2020_single_orifice_x", "li2020_single_orifice_y", "s"),
    "Milgram83": ("milgram83_x", "milgram83_y", "o"),
    "Fannelop & Sjoen 1980": ("fs80_x", "fs80_y", "D"),
    "Milgram & Van Houten 1982": ("mv82_x", "mv82_y", "v"),
}

PLOT_SPECS = {
    "figure_10a": {
        "filename": "bgD_vs_zhat.png",
        "title": "Plume half-width scaling",
        "xlabel": r"$\hat{z} = z/D$",
        "ylabel": r"$b_g/D$",
    },
    "figure_10b": {
        "filename": "WcWs_vs_zhat.png",
        "title": "Centerline velocity scaling",
        "xlabel": r"$\hat{z} = z/D$",
        "ylabel": r"$W_c/W_s$",
    },
    "figure_11a": {
        "filename": "Qhat_vs_zhat.png",
        "title": "Volume flux scaling",
        "xlabel": r"$\hat{z} = z/D$",
        "ylabel": r"$Q/(D^2 W_s)$",
    },
    "figure_11b": {
        "filename": "Mhat_vs_zhat.png",
        "title": "Momentum flux scaling",
        "xlabel": r"$\hat{z} = z/D$",
        "ylabel": r"$M/(D^2 W_s^2)$",
    },
}


def load_master_data() -> pd.DataFrame:
    """Load the paper-level Li et al. 2020 master CSV."""
    if not MASTER_CSV.exists():
        raise FileNotFoundError(f"Missing master CSV: {MASTER_CSV}")
    return pd.read_csv(MASTER_CSV)


def plot_scaling(master_df: pd.DataFrame, plot_id: str):
    """Create one nondimensional scaling plot from a plot block in the master CSV."""
    spec = PLOT_SPECS[plot_id]
    plot_df = master_df[master_df["plot_id"] == plot_id]
    if plot_df.empty:
        raise ValueError(f"No rows found for plot_id={plot_id}")

    fig, ax = plt.subplots(figsize=(6.5, 4.8))
    plotted = 0

    for label, (x_col, y_col, marker) in SERIES.items():
        if x_col not in plot_df.columns or y_col not in plot_df.columns:
            continue

        xy = plot_df[[x_col, y_col]].dropna()
        if xy.empty:
            continue

        xy = xy.sort_values(x_col)
        ax.scatter(xy[x_col], xy[y_col], label=label, marker=marker, s=24)
        plotted += 1

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel(spec["xlabel"])
    ax.set_ylabel(spec["ylabel"])
    ax.set_title(spec["title"])
    ax.grid(True, which="both", linewidth=0.5, alpha=0.35)
    if plotted:
        ax.legend(frameon=False)
    fig.tight_layout()

    output_path = FIG_DIR / spec["filename"]
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    print(f"Saved {output_path}")
    return fig, ax


if __name__ == "__main__":
    df = load_master_data()
    for key in ["figure_10a", "figure_10b", "figure_11a", "figure_11b"]:
        plot_scaling(df, key)
