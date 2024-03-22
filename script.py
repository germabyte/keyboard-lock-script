import ctypes
import sys
import os
import time
import subprocess
from pynput import keyboard

# Flag to track if the keyboard is locked
keyboard_locked = False

# Process ID of this script
current_pid = os.getpid()

# Function to lock the keyboard
def lock_keyboard():
    global keyboard_locked
    if not keyboard_locked:
        ctypes.windll.user32.BlockInput(True)
        keyboard_locked = True
        print(f"Keyboard is locked by process {current_pid}.")

# List to store the timestamps of spacebar presses
spacebar_presses = []

# Function to handle key press events
def on_press(key):
    if key == keyboard.Key.space:
        spacebar_presses.append(time.time())
        if len(spacebar_presses) > 5:
            spacebar_presses.pop(0)
        if len(spacebar_presses) == 5 and spacebar_presses[-1] - spacebar_presses[0] < 1:
            terminate_script()
            spacebar_presses.clear()

# Function to terminate the script and close all windows
def terminate_script():
    global keyboard_locked
    if keyboard_locked:
        keyboard_locked = False
        ctypes.windll.kernel32.TerminateProcess(int(current_pid), 1)
        print("Keyboard locking process killed.")
        # Close all windows opened by the script
        subprocess.run(["taskkill", "/F", "/IM", "python.exe"], capture_output=True)
        # Close the terminal window
        subprocess.run(["taskkill", "/F", "/FI", "WINDOWTITLE eq %PROMPT%"], capture_output=True)
        sys.exit()

# Request admin permissions (only works on Windows Vista and later)
if not ctypes.windll.shell32.IsUserAnAdmin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

# Lock the keyboard initially
lock_keyboard()

# Set up the keyboard listener
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Keep the script running to listen for keyboard events
print("Press the spacebar 5 times rapidly to terminate the script and close all windows.")
while True:
    pass