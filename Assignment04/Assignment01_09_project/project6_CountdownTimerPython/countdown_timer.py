import time  # To use the sleep function

# Step 1: Ask user to enter time in seconds
seconds = int(input("⏱ Enter time in seconds: "))

# Step 2: Start countdown loop
while seconds > 0:
    mins, secs = divmod(seconds, 60)  # Convert seconds to minutes and seconds
    time_format = '{:02d}:{:02d}'.format(mins, secs)  # Format time like 02:59
    print(time_format, end='\r')  # Print and overwrite in the same line
    time.sleep(1)  # Wait for 1 second
    seconds -= 1  # Reduce time by 1 second

# Step 3: When countdown is finished
print("⏰ Time’s up!")
