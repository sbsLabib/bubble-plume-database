# Li et al. 2020 cleaned datasets

These files were cleaned from the uploaded Li et al. dataset CSV files.

## Source paper

Li, G., Wang, B., Wu, H., & DiMarco, S. F. (2020). Impact of bubble size on the integral characteristics of bubble plumes in quiescent and unstratified water. International Journal of Multiphase Flow, 125, 103230. https://doi.org/10.1016/j.ijmultiphaseflow.2020.103230

## Cleaning actions

1. Removed the first source-label row, e.g. `Lietal19,`.
2. Kept only numeric tabular data in each CSV.
3. Standardized the x-column name as `z_hat`.
4. Renamed y-columns to explicit nondimensional variables:
   - `bgD` → `b_g_over_D`
   - `Wc` → `W_c_over_W_s`
   - `Q` → `Q_over_D2_W_s`
   - `M` → `M_over_D2_W_s2`
5. Sorted rows numerically by `z_hat`.
6. Did not split AS/SO or Q1/Q2 cases because the uploaded CSV files do not include case labels.

## Cleaned files

- `b_g_over_D_vs_z_hat.csv`
- `centerline_velocity_over_W_s_vs_z_hat.csv`
- `volume_flux_over_D2_W_s_vs_z_hat.csv`
- `momentum_flux_over_D2_W_s2_vs_z_hat.csv`
- `manifest.csv`
- `metadata_stub.json`

## Suggested GitHub repository location

For the current website structure, place this folder at:

`csv/li_2020_cleaned/`

Later, this can be migrated to a more formal data structure such as:

`data/papers/li_2020/processed/`
