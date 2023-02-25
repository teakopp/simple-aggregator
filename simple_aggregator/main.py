import csv
import os
from modules.aggregator import Aggregator
from modules.utils import format_date 

# Get current dir path to reference to find csvs
curr_path = os.path.dirname(__file__)

def main():
    # Read csv to get event timestamps
    with open(f"{curr_path}/../data/events.csv", newline='') as csvfile:
        a = Aggregator()
        reader = csv.reader(csvfile,delimiter=',',quotechar='"')
        for row in reader:
            # Get timestamps from csv 
            formatted_date = format_date(row[3])
            # Pass timestamps to aggregator class to be counted
            a.add_event(formatted_date)

    write_path = f"{curr_path}/../data/output.csv" 
    # Timestamp bucket count results
    results = a.report()
    # Write them to csv called output.csv
    with open(write_path, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Time Bucket,Number of Events"]) 
        sorted_results = []
        for key, value in results.items():
            row = [f"{key},{value}"]
            sorted_results.append(row)

        sorted_results.sort()
        for row in sorted_results:
            writer.writerow(row) 

    print(f"\n{results}\n")
    print(f"Results written to {write_path}")


if __name__ == "__main__":
    main()
