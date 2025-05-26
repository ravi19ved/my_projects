import pandas as pd
import re

def load_radiosonde_edt(filepath):
    """
    Loads radiosonde data from a .edt ASCII file into a pandas DataFrame,
    handling the split 'Time min s' column.

    Args:
        filepath (str): The path to the .edt ASCII file.

    Returns:
        tuple: A tuple containing:
            - pd.DataFrame: The radiosonde data.
            - dict: A dictionary containing parsed header metadata.
            - dict: A dictionary mapping column names to their units.
    """
    header_lines = []
    column_names_raw = []
    units_raw = []
    data_start_line_idx = -1

    with open(filepath, 'r') as f:
        lines = f.readlines()

    # Identify header, column names, and data start
    for i, line in enumerate(lines):
        # Look for the line containing column headers
        if "Time" in line and "Hght" in line and "Press" in line:
            column_names_raw = re.split(r'\s{2,}', line.strip())
            column_names_raw = [col for col in column_names_raw if col] # Clean up
            # The units line is immediately below the column names
            units_raw = re.split(r'\s{2,}', lines[i+1].strip())
            units_raw = [unit for unit in units_raw if unit] # Clean up
            data_start_line_idx = i + 3 # Data starts 3 lines after column names (column names, units, empty line)
            break
        else:
            header_lines.append(line.strip())

    if not column_names_raw or data_start_line_idx == -1:
        raise ValueError("Could not determine column names or data start in the file.")

    # --- Process Column Names and Units ---
    processed_column_names = []
    units_map = {}

    # Handle the 'Time min s' column specifically
    if column_names_raw[0] == "Time":
        # The first column 'Time' actually represents 'min' and 's'
        processed_column_names.append("Time_min")
        processed_column_names.append("Time_s")
        # Map units for 'min' and 's'
        if len(units_raw) >= 2:
            units_map["Time_min"] = units_raw[0] # Assuming 'min' unit is first
            units_map["Time_s"] = units_raw[1]   # Assuming 's' unit is second
            # Adjust units_raw to skip the first two units as they've been handled
            remaining_units = units_raw[2:]
        else:
            print("Warning: Insufficient units found for 'Time min s'. Assigning empty units.")
            units_map["Time_min"] = ""
            units_map["Time_s"] = ""
            remaining_units = units_raw
    else:
        # Fallback if 'Time' is not the first column as expected (less likely for this format)
        processed_column_names.append(column_names_raw[0])
        if len(units_raw) >= 1:
            units_map[column_names_raw[0]] = units_raw[0]
            remaining_units = units_raw[1:]
        else:
            remaining_units = []

    # Process the rest of the columns and their units
    for j, col_name in enumerate(column_names_raw[1:]): # Start from the second column
        processed_column_names.append(col_name)
        if j < len(remaining_units): # Ensure we have a corresponding unit
            units_map[col_name] = remaining_units[j]
        else:
            units_map[col_name] = "" # Assign empty string if no unit found

    # --- Parse Header Metadata ---
    metadata = {}
    for h_line in header_lines:
        if ':' in h_line:
            key, value = h_line.split(':', 1)
            metadata[key.strip()] = value.strip()

    # --- Load Data into DataFrame ---
    data_lines = lines[data_start_line_idx:]
    processed_data = []

    for line in data_lines:
        # Split line by one or more spaces, and filter out empty strings
        parts = re.split(r'\s+', line.strip())
        parts = [p for p in parts if p] # Clean up any remaining empty strings

        if not parts: # Skip empty lines
            continue

        try:
            # Convert parts to float, ensuring correct order for min and s
            row_data = [float(p) for p in parts]
            processed_data.append(row_data)
        except ValueError as e:
            print(f"Skipping malformed data line: '{line.strip()}' - Error: {e}")
            continue


    # Create DataFrame
    # Use the processed_column_names that correctly splits 'Time'
    if len(processed_column_names) != len(processed_data[0]):
        raise ValueError(f"Mismatch between number of columns ({len(processed_column_names)}) "
                         f"and number of data points per row ({len(processed_data[0])}). "
                         f"Please check column parsing logic. Example row: {processed_data[0]}")


    df = pd.DataFrame(processed_data, columns=processed_column_names)

    return df, metadata, units_map


if __name__ == "__main__":
    file_path = "D:\\Data\\ekam-radiosonde-data\\Data for Analysis\\Vaisala Data along with AZISTA sonde-reg\\sample.EDT" # Replace with your actual file path

    # Create a dummy .edt file for demonstration
    dummy_data = """Station         : SN_2024_ekamsat
Location      : 11.2567 72.5357 9 m
Launch time   : 2024 07 08 at 05 57 UTC
RS type       : RS41-SG
RS number     : W1857420

    Time     Hght   Press   Temp   Hum     Td    MixR     DD    FF Latitude  Longitude
    min s     gpm     hPa   degC     %   degC    g/kg    deg   m/s     deg       deg

    0  0      5.09 1005.08  29.40  75.0  24.52   19.60    258  11.0   11.2567    72.5357
    0  1      9.55 1004.29  30.32  73.9  25.17   20.42    258   6.5   11.2564    72.5362
    0  2     11.39 1004.28  30.26  73.9  25.11   20.35    257   5.1   11.2563    72.5364
    0  3     12.87 1004.27  30.26  74.1  25.14   20.39    256   4.9   11.2563    72.5364
    0  4     15.68 1004.17  30.19  74.4  25.16   20.42    256   5.2   11.2563    72.5364
    0  5     20.89 1003.37  30.09  74.6  25.10   20.37    256   5.7   11.2563    72.5365
    0  6     27.79 1002.44  29.99  74.4  24.96   20.21    255   6.1   11.2563    72.5365
    0  7     34.91 1001.51  29.88  74.0  24.75   19.97    255   6.5   11.2563    72.5366
    0  8     41.08 1001.05  29.72  73.9  24.59   19.77    255   6.8   11.2563    72.5367
    0  9     46.55 1000.53  29.59  74.0  24.48   19.64    255   7.2   11.2564    72.5368
    0 10     51.87  999.84  29.53  73.8  24.38   19.53    254   7.7   11.2564    72.5369
    0 11     57.20  999.25  29.48  73.8  24.33   19.48    254   8.1   11.2564    72.5370
    0 12     62.66  998.74  29.43  74.0  24.33   19.49    254   8.5   11.2564    72.5371
    0 13     68.25  998.01  29.37  74.3  24.34   19.52    253   8.9   11.2564    72.5372
"""
    with open(file_path, "w") as f:
        f.write(dummy_data)


    try:
        df, metadata, units = load_radiosonde_edt(file_path)

        print("--- Radiosonde Data Loaded Successfully ---")
        print("\nMetadata:")
        for key, value in metadata.items():
            print(f"  {key}: {value}")

        print("\nUnits:")
        for col, unit in units.items():
            print(f"  {col}: {unit}")

        print("\nFirst 5 rows of DataFrame:")
        print(df.head())

        print("\nDataFrame Info:")
        df.info()

        print("\nBasic Statistics for 'Temp' and 'Hght' columns:")
        print(df[['Temp', 'Hght']].describe())

        # Example of further analysis:
        # Calculate total time in seconds from launch
        df['Total_Time_s'] = df['Time_min'] * 60 + df['Time_s']
        print("\nFirst 5 rows with 'Total_Time_s' column:")
        print(df[['Time_min', 'Time_s', 'Total_Time_s']].head())


        # Plot temperature vs. height (requires matplotlib)
        try:
            import matplotlib.pyplot as plt
            plt.figure(figsize=(10, 6))
            plt.plot(df['Temp'], df['Hght'])
            plt.xlabel(f"Temperature ({units['Temp']})")
            plt.ylabel(f"Height ({units['Hght']})")
            plt.title("Radiosonde: Temperature vs. Height Profile")
            plt.grid(True)
            plt.show()

            plt.figure(figsize=(10, 6))
            plt.plot(df['Press'], df['Hght'])
            plt.xlabel(f"Pressure ({units['Press']})")
            plt.ylabel(f"Height ({units['Hght']})")
            plt.title("Radiosonde: Pressure vs. Height Profile")
            plt.grid(True)
            plt.gca().invert_xaxis() # Pressure typically decreases with height
            plt.show()

            plt.figure(figsize=(12, 6))
            plt.plot(df['Total_Time_s'], df['Hght'])
            plt.xlabel("Total Time (s)")
            plt.ylabel(f"Height ({units['Hght']})")
            plt.title("Radiosonde: Height vs. Total Time")
            plt.grid(True)
            plt.show()


        except ImportError:
            print("\nMatplotlib not installed. Skipping plotting examples.")
            print("To install: pip install matplotlib")

    except ValueError as e:
        print(f"Error loading file: {e}")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found. Please check the path.")