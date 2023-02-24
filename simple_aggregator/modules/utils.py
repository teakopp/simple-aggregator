from datetime import datetime

def format_date(timestamp:str) -> str:
    # replace T with space to format properly if T exists
    timestamp = timestamp.replace("T"," ")
    # if date is certain length fix it
    if len(timestamp) > 16:
        timestamp = timestamp[0:16]
    # if date is invalid throw exception
    try:
        datetime.strptime(timestamp, '%Y-%m-%d %H:%M')
    except ValueError as err:
        raise err
    print(timestamp)
    return timestamp
