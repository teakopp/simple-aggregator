# Simple Aggregator 

### What this does

Reads csv logs and aggregates the events into buckets by timestamp

### Get Started

Instructions on how to install and run the project:

1. Clone the repository: `git clone https://github.com/teakopp/simple-aggregator.git`
2. Navigate to the project directory: `cd simple-aggregator`
3. Create virtual environment using `python3 -m venv myenv`
4. Run `source myenv/bin/activate`
5. Install the required packages: `pip install -r requirements.txt`
6. Run the project: `python3 simple_aggregator/main.py`

### How to use

Instructions on how to use the project:

1. Provide csv named events.csv in data directory 
2. Run `python3 main.py`
3. Output will be saved as file called `output.csv` in `data` directory

### Testing
1. Run `source myenv/bin/activate`
2. Run `pytest`

