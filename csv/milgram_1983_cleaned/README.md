# Milgram 1983 cleaned CSV files

These files were cleaned from the originally uploaded Milgram83 CSV files.

## Cleaning actions

1. Removed the first source-label row, e.g. `Milgram83,`.
2. Kept only numeric tabular data in each CSV.
3. Standardized the first column name to `z_hat`.
4. Renamed selected variables for clearer database use:
   - `bgD` → `b_g_over_D`
   - `Wc` → `W_c`
5. Sorted rows by `z_hat` to make plotting easier later.
6. Preserved duplicate `z_hat` values where present, because those may represent digitized scatter points or multiple data points from the source figure.

## Files

- `alpha_vs_z_hat.csv`
- `b_g_over_D_vs_z_hat.csv`
- `centerline_velocity_vs_z_hat.csv`
- `momentum_flux_vs_z_hat.csv`
- `volume_flux_vs_z_hat.csv`
- `metadata_stub.json`

## Note

The metadata file is only a placeholder. It should be completed after reviewing the Milgram 1983 paper.
