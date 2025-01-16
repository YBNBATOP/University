from datetime import datetime
import pytz

# Define the UTC timestamp
utc_timestamp = datetime.strptime('2023-03-03 11:06:55', '%Y-%m-%d %H:%M:%S')

# Define the timezone for Brussels
brussels_timezone = pytz.timezone('Europe/Brussels')

# Convert the UTC timestamp to Brussels timezone
brussels_timestamp = utc_timestamp.astimezone(brussels_timezone)

# Format the timestamp in Brussels timezone
formatted_timestamp = brussels_timestamp.strftime('%Y-%m-%d %H:%M:%S')

print("Timestamp in Brussels timezone:", formatted_timestamp)
