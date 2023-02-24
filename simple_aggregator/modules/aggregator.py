from typing import Dict
from datetime import datetime

class Aggregator:
    def __init__(self):
        self.buckets = {}

    def add_event(self,timestamp: str) -> None:
        '''Takes in timestamp and adds it to bucket report as key and tallies count'''
        event = datetime.strptime(timestamp, '%Y-%m-%d %H:%M')
        # event.hour:02 keeps leading zero for hour
        hour_bucket = f"{event.date()}T{event.hour:02}:00:00Z"
        self.buckets[hour_bucket] = 1 + self.buckets.get(hour_bucket, 0)

    def report(self) -> Dict[str,int] :
        '''Returns bucket report in dict form'''
        # Create data based on example given in README prompt.
        # Data in events.csv is formatted different, so chose Z formatting instead of
        # +00. So data will be returned in a dict using that format as key
        return self.buckets

    



