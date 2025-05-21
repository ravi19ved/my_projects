# Manually parse the file to ensure consistent formatting
parsed_rows = []
with open(file_path, 'r') as f:
    for i, line in enumerate(f):
        if i < 10:
            continue  # Skip metadata and headers
        if line.strip() == "":
            continue  # Skip empty lines

        parts = line.strip().split()
        if len(parts) == 13:
            # Convert parts to appropriate types and append
            try:
                parsed_rows.append([
                    int(parts[0]), int(parts[1]), float(parts[2]), float(parts[3]),
                    float(parts[4]), float(parts[5]), float(parts[6]), float(parts[7]),
                    float(parts[8]), float(parts[9]), float(parts[10]), float(parts[11])
                ])
            except ValueError:
                continue  # Skip rows with conversion issues

# Create DataFrame from parsed data
columns = [
    "min", "s", "Hght_gpm", "Press_hPa", "Temp_degC", "Hum_pct", "Td_degC",
    "MixR_g_per_kg", "DD_deg", "FF_mps", "Latitude", "Longitude"
]
df_clean = pd.DataFrame(parsed_rows, columns=columns)

# Add time in seconds
df_clean["time_seconds"] = df_clean["min"] * 60 + df_clean["s"]

# Convert to xarray Dataset and save as NetCDF
ds_clean = xr.Dataset.from_dataframe(df_clean.set_index("time_seconds"))
netcdf_clean_path = "/mnt/data/SN_2024_ekamsat2406271203_clean.nc"
ds_clean.to_netcdf(netcdf_clean_path)

netcdf_clean_path
# This code reads a radio sonde data file, parses it, and converts it into a clean xarray Dataset.