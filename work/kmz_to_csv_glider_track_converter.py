# Read the uploaded CSV and attempt to extract/standardize date, time, latitude, longitude
import pandas as pd
import re

input_path = "/mnt/data/1095_track_data_final.csv"
df = pd.read_csv(input_path)

# Identify possible lat/lon columns
lat_col = None
lon_col = None
for c in df.columns:
    cl = c.lower()
    if cl in ["lat", "latitude", "y"]:
        lat_col = c
    if cl in ["lon", "longitude", "long", "x"]:
        lon_col = c

# Identify datetime column candidates
date_col = None
time_col = None
datetime_col = None

for c in df.columns:
    cl = c.lower()
    if "date" in cl and date_col is None:
        date_col = c
    if "time" in cl and time_col is None:
        time_col = c
    if "datetime" in cl or "timestamp" in cl:
        datetime_col = c

# Build output dataframe
if datetime_col:
    dt = pd.to_datetime(df[datetime_col], errors="coerce")
    out = pd.DataFrame({
        "date": dt.dt.date,
        "time": dt.dt.time,
        "latitude": df[lat_col] if lat_col else None,
        "longitude": df[lon_col] if lon_col else None
    })
else:
    out = pd.DataFrame({
        "date": df[date_col] if date_col else None,
        "time": df[time_col] if time_col else None,
        "latitude": df[lat_col] if lat_col else None,
        "longitude": df[lon_col] if lon_col else None
    })

output_path = "/mnt/data/glider_track_extracted.csv"
out.to_csv(output_path, index=False)

output_path