import datetime
import time
import playsound

def set_alarm(alarm_time):
    """Sets an alarm and plays a sound when the alarm time is reached."""

    print(f"Alarm set for {alarm_time}")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Time's up!")
            playsound.playsound("alarm_sound.mp3")  # Replace with your alarm sound file
            break
        time.sleep(1)

# Get user input for the alarm time
alarm_hour = int(input("Enter hour (0-23): "))
alarm_minute = int(input("Enter minute (0-59): "))
alarm_second = int(input("Enter second (0-59): "))

alarm_time = f"{alarm_hour:02}:{alarm_minute:02}:{alarm_second:02}"

set_alarm(alarm_time)


