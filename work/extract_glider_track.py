import pandas as pd
import sys

def extract_track(input_file, output_file):

    # Read the CSV file
    df = pd.read_csv(input_file)

    # Try to detect latitude and longitude columns
    lat_col = None
    lon_col = None

    for col in df.columns:
        c = col.lower()
        if c in ["lat", "latitude", "y"]:
            lat_col = col
        if c in ["lon", "longitude", "long", "x"]:
            lon_col = col

    # Detect date/time columns
    date_col = None
    time_col = None
    datetime_col = None

    for col in df.columns:
        c = col.lower()

        if "datetime" in c or "timestamp" in c:
            datetime_col = col

        elif "date" in c:
            date_col = col

        elif "time" in c:
            time_col = col

    # Extract date and time
    if datetime_col:
        dt = pd.to_datetime(df[datetime_col], errors="coerce")
        date = dt.dt.date
        time = dt.dt.time

    else:
        date = df[date_col] if date_col else None
        time = df[time_col] if time_col else None

    # Create output dataframe
    out = pd.DataFrame({
        "date": date,
        "time": time,
        "latitude": df[lat_col],
        "longitude": df[lon_col]
    })

    # Save output
    out.to_csv(output_file, index=False)

    print("Output saved to:", output_file)


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: python extract_glider_track.py input.csv output.csv")
        sys.exit()

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    extract_track(input_file, output_file)