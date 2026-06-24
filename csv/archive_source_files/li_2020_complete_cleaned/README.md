# Li et al. 2020 complete cleaned datasets

These files are cleaned nondimensional plotting datasets associated with:

Li, G., Wang, B., Wu, H., & DiMarco, S. F. (2020). *Impact of bubble size on the integral characteristics of bubble plumes in quiescent and unstratified water*. International Journal of Multiphase Flow, 125, 103230. DOI: 10.1016/j.ijmultiphaseflow.2020.103230

## Included case folders

- `air_stone/` — cleaned files from the previously uploaded air-stone dataset
- `single_orifice/` — cleaned files from the newly uploaded single-orifice dataset

## Cleaning actions

1. Removed non-numeric source-label/header rows from the top of each uploaded CSV.
2. Kept only numeric two-column data.
3. Standardized the x-column name as `z_hat`.
4. Renamed y-columns to explicit nondimensional variables:
   - `b_g_over_D`
   - `W_c_over_W_s`
   - `Q_over_D2_W_s`
   - `M_over_D2_W_s2`
5. Sorted rows numerically by `z_hat`.
6. Preserved duplicate `z_hat` values where present.
7. Added `manifest.csv` and `metadata_stub.json`.

## Variables

- `z_hat` = `z/D`
- `b_g_over_D` = `b_g/D`, nondimensional plume half-width
- `W_c_over_W_s` = `W_c/W_s`, centerline velocity normalized by bubble slip velocity
- `Q_over_D2_W_s` = `Q/(D^2 W_s)`, nondimensional liquid volume flux
- `M_over_D2_W_s2` = `M/(D^2 W_s^2)`, nondimensional momentum flux

## Suggested GitHub repository location

Place this folder at:

`csv/li_2020_complete_cleaned/`

The website page can then link to files such as:

`../csv/li_2020_complete_cleaned/single_orifice/b_g_over_D_vs_z_hat.csv`
