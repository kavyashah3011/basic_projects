import time

def alarm_clock():
    alarm_time = input("Set your alarm time (HH:MM:SS): ")
    
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Time's up! Alarm ringing!")
            break
        time.sleep(1)  # Wait for a second before checking again

alarm_clock()
