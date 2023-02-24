import csv
import os
from modules.aggregator import Aggregator
from modules.utils import format_date 

curr_path = os.path.dirname(__file__)

def main():
    with open(f"{curr_path}/../data/events.csv", newline='') as csvfile:
        a = Aggregator()
        reader = csv.reader(csvfile,delimiter=',',quotechar='"')
        for row in reader:
            formatted_date = format_date(row[3])
            a.add_event(formatted_date)

    write_path = f"{curr_path}/../data/output.csv" 
    results = a.report()
    with open(write_path, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, results.keys())
        writer.writeheader()
        writer.writerow(results)
    print(f"Results written to {write_path}")


if __name__ == "__main__":
    main()
