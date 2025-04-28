#  Below code is not working
#  Ravi Chandra V
#  28 April 2025

import csv
import re

input_file = 'C:\Users\ravic\Desktop\Desktop\Glider_Tracks\1129_Mauritius\DLD4345449615463055265\Surfacing.csv'   # Replace with your actual file name
output_file = 'C:\Users\ravic\Desktop\Desktop\Glider_Tracks\1129_Mauritius\DLD4345449615463055265\parsed_output.csv'    # Output file location 

# Regex to extract the GPS time
gps_time_regex = re.compile(r'Time of GPS Position:\s*(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2})')

with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile, delimiter='\t')
    writer = csv.writer(outfile)
    writer.writerow(['Latitude', 'Longitude', 'Date', 'Time'])  # Header

    for row in reader:
        try:
            lon = row[0]
            lat = row[1]
            info = row[3]

            # Extract GPS date and time
            match = gps_time_regex.search(info)
            if match:
                date = match.group(1)
                time = match.group(2)
                writer.writerow([lat, lon, date, time])
        except IndexError:
            continue  # Skip lines that don't have expected format

#  Need to test this programme. 
