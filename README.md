# Keyboard Lock Script

This Python script utilizes the `ctypes` and `pynput` libraries to lock the keyboard input and prevent any accidental keystrokes. It's particularly useful in scenarios where non-users, like toddlers or pets, might come into contact with the keyboard, ensuring that their playful activities don't cause unintended actions on the computer.

## Features

- **Keyboard Lock**: Prevents all keyboard input until the script is terminated.
- **Safe Termination**: Allows the script to be safely terminated by pressing the spacebar five times rapidly.
- **Admin Privileges**: Requests admin permissions to ensure it can block input effectively.

## Use Cases

- **Child-Proofing**: When toddlers are playing near a computer, this script can prevent them from sending emails, deleting files, or performing other unintended operations.
- **Pet Safety**: Pets, especially cats, are known to walk on keyboards. This script ensures they don't disrupt your work.
- **Cleaning Mode**: When cleaning your keyboard, you can run this script to avoid inputting random commands.

## How to Use

1. Ensure you have `Python` and the `pynput` library installed.
2. Run the script with administrator privileges.
3. The keyboard will be locked immediately.
4. To unlock, press the spacebar five times quickly.

## Disclaimer

This script requires administrative privileges to run effectively. Use it responsibly, and ensure that it's only used in appropriate scenarios.

