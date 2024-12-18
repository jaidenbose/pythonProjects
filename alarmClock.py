# Import Required Libraries
from tkinter import *
import datetime
import time
import winsound
from threading import Thread

# Initialize the main window
app = Tk()
app.geometry("400x200")
app.title("Alarm Clock")

# Function to handle threading for the alarm
def start_alarm_thread():
    alarm_thread = Thread(target=alarm_checker)
    alarm_thread.start()

# Function to check and trigger the alarm
def alarm_checker():
    while True:
        # Combine selected time values into a single alarm time string
        alarm_time = f"{selected_hour.get()}:{selected_minute.get()}:{selected_second.get()}"

        # Pause for 1 second to avoid high CPU usage
        time.sleep(1)

        # Get the current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Current Time: {current_time}, Alarm Time: {alarm_time}")

        # Trigger the alarm if the current time matches the set time
        if current_time == alarm_time:
            print("Alarm Triggered! Time to Wake Up!")
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break  # Exit the loop after the alarm is triggered

# GUI Components: Labels, Frames, Dropdowns, and Buttons
Label(app, text="Alarm Clock", font=("Helvetica", 20, "bold"), fg="red").pack(pady=10)
Label(app, text="Set Alarm Time", font=("Helvetica", 15)).pack()

# Frame for time input dropdowns
time_frame = Frame(app)
time_frame.pack()

# Hour dropdown menu
selected_hour = StringVar(app)
hour_options = [f"{i:02}" for i in range(24)]  # List of hours (00 to 23)
selected_hour.set(hour_options[0])  # Default value
hour_menu = OptionMenu(time_frame, selected_hour, *hour_options)
hour_menu.pack(side=LEFT)

# Minute dropdown menu
selected_minute = StringVar(app)
minute_options = [f"{i:02}" for i in range(60)]  # List of minutes (00 to 59)
selected_minute.set(minute_options[0])  # Default value
minute_menu = OptionMenu(time_frame, selected_minute, *minute_options)
minute_menu.pack(side=LEFT)

# Second dropdown menu
selected_second = StringVar(app)
second_options = [f"{i:02}" for i in range(60)]  # List of seconds (00 to 59)
selected_second.set(second_options[0])  # Default value
second_menu = OptionMenu(time_frame, selected_second, *second_options)
second_menu.pack(side=LEFT)

# Button to set the alarm
Button(app, text="Set Alarm", font=("Helvetica", 15), command=start_alarm_thread).pack(pady=20)

# Start the Tkinter main loop
app.mainloop()
