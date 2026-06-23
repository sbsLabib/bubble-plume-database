from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

def find_repo_root() -> Path:
    """Return repository root whether this is run from root, scripts/, or notebooks/."""
    cwd = Path.cwd()
    if (cwd / "csv").exists():
        return cwd
    if (cwd.parent / "csv").exists():
        return cwd.parent
    raise FileNotFoundError(
        "Could not find a csv/ folder. Run this notebook/script from the repository root "
        "or from the notebooks/ or scripts/ folder inside the repository."
    )

REPO_ROOT = find_repo_root()
CSV_DIR = REPO_ROOT / "csv"
FIG_DIR = REPO_ROOT / "figures" / "literature_scaling"
FIG_DIR.mkdir(parents=True, exist_ok=True)


def first_existing_path(*candidates: Path) -> Path:
    """Return the first path that exists, allowing current and future CSV layouts."""
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return candidates[0]


LITERATURE_SERIES_DIR = first_existing_path(
    CSV_DIR / "li2020_literature_series_nondimensional",
    CSV_DIR / "milgram83_tabular_and_related_nondim_data" / "li2020_literature_series_nondimensional",
)

DATASETS = {
    "Milgram83": {
        "folder": CSV_DIR / "milgram_1983_cleaned",
        "files": {
            "bg": "b_g_over_D_vs_z_hat.csv",
            "wc": "centerline_velocity_vs_z_hat.csv",
            "q": "volume_flux_vs_z_hat.csv",
            "m": "momentum_flux_vs_z_hat.csv",
        },
        "marker": "o",
    },
    "Li2020 AS": {
        "folder": CSV_DIR / "li_2020_complete_cleaned" / "air_stone",
        "files": {
            "bg": "b_g_over_D_vs_z_hat.csv",
            "wc": "centerline_velocity_over_W_s_vs_z_hat.csv",
            "q": "volume_flux_over_D2_W_s_vs_z_hat.csv",
            "m": "momentum_flux_over_D2_W_s2_vs_z_hat.csv",
        },
        "marker": "^",
    },
    "Li2020 SO": {
        "folder": CSV_DIR / "li_2020_complete_cleaned" / "single_orifice",
        "files": {
            "bg": "b_g_over_D_vs_z_hat.csv",
            "wc": "centerline_velocity_over_W_s_vs_z_hat.csv",
            "q": "volume_flux_over_D2_W_s_vs_z_hat.csv",
            "m": "momentum_flux_over_D2_W_s2_vs_z_hat.csv",
        },
        "marker": "s",
    },
    "FS80": {
        "folder": LITERATURE_SERIES_DIR / "fannelop_sjoen_1980",
        "files": {
            "bg": "b_g_over_D_vs_z_hat.csv",
            "wc": "centerline_velocity_over_W_s_vs_z_hat.csv",
            "q": "volume_flux_over_D2_W_s_vs_z_hat.csv",
            "m": "momentum_flux_over_D2_W_s2_vs_z_hat.csv",
        },
        "marker": "D",
    },
    "MV82": {
        "folder": LITERATURE_SERIES_DIR / "milgram_van_houten_1982",
        "files": {
            "bg": "b_g_over_D_vs_z_hat.csv",
            "wc": "centerline_velocity_over_W_s_vs_z_hat.csv",
            "q": "volume_flux_over_D2_W_s_vs_z_hat.csv",
            "m": "momentum_flux_over_D2_W_s2_vs_z_hat.csv",
        },
        "marker": "v",
    },
}

PLOT_SPECS = {
    "bg": {
        "filename": "bgD_vs_zhat.png",
        "title": "Plume half-width scaling",
        "xlabel": r"$\hat{z} = z/D$",
        "ylabel": r"$b_g/D$",
        "y_candidates": ["b_g_over_D", "bgD"],
    },
    "wc": {
        "filename": "WcWs_vs_zhat.png",
        "title": "Centerline velocity scaling",
        "xlabel": r"$\hat{z} = z/D$",
        "ylabel": r"$W_c/W_s$",
        "y_candidates": ["W_c_over_W_s", "W_c", "Wc"],
    },
    "q": {
        "filename": "Qhat_vs_zhat.png",
        "title": "Volume flux scaling",
        "xlabel": r"$\hat{z} = z/D$",
        "ylabel": r"$Q/(D^2 W_s)$",
        "y_candidates": ["Q_over_D2_W_s", "Q"],
    },
    "m": {
        "filename": "Mhat_vs_zhat.png",
        "title": "Momentum flux scaling",
        "xlabel": r"$\hat{z} = z/D$",
        "ylabel": r"$M/(D^2 W_s^2)$",
        "y_candidates": ["M_over_D2_W_s2", "M"],
    },
}

def load_xy(path: Path, y_candidates):
    """Load a two-column CSV and return x/y arrays using robust column detection."""
    df = pd.read_csv(path)
    if "z_hat" in df.columns:
        x_col = "z_hat"
    elif "zhat" in df.columns:
        x_col = "zhat"
    else:
        x_col = df.columns[0]

    y_col = None
    for candidate in y_candidates:
        if candidate in df.columns:
            y_col = candidate
            break
    if y_col is None:
        y_col = [c for c in df.columns if c != x_col][0]

    df = df[[x_col, y_col]].dropna()
    df = df.sort_values(x_col)
    return df[x_col], df[y_col]

def plot_scaling(plot_key: str):
    spec = PLOT_SPECS[plot_key]
    fig, ax = plt.subplots(figsize=(6.5, 4.8))

    plotted = 0
    for label, dataset in DATASETS.items():
        file_name = dataset["files"].get(plot_key)
        if not file_name:
            continue

        path = dataset["folder"] / file_name
        if not path.exists():
            print(f"Skipping missing file: {path}")
            continue

        x, y = load_xy(path, spec["y_candidates"])
        if len(x) == 0:
            print(f"Skipping empty file: {path}")
            continue

        ax.scatter(x, y, label=label, marker=dataset["marker"], s=24)
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
    for key in ["bg", "wc", "q", "m"]:
        plot_scaling(key)
