from datetime import datetime, timedelta

def nanoseconds_to_readable_time(nanoseconds):
    # Convert nanoseconds to seconds
    seconds = nanoseconds / 1e9
    
    # Convert the Unix timestamp to a human-readable format
    readable_time = datetime(1970, 1, 1) + timedelta(seconds=seconds)
    return readable_time

nanoseconds = int(input("Enter nanoseconds since January 1, 1970: "))
readable_time = nanoseconds_to_readable_time(nanoseconds)

print(f"Readable time: {readable_time}")