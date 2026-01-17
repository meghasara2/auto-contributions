# EDUCATIONAL CODE TUTORIAL: Real-time System Monitor using psutil

# Learning Objective:
# This tutorial teaches you how to build a basic command-line utility
# to display real-time CPU, memory, and disk usage statistics.
# You will learn to use the 'psutil' library to fetch system metrics,
# format the output for readability, and update it continuously in the terminal.

import psutil       # The primary library for system monitoring. 'psutil' stands for process and system utilities.
import time         # Used for pausing execution to create the "real-time" effect.
import os           # Used to clear the terminal screen for a cleaner display.

# --- Configuration Constants ---
# These are defined at the top so they are easy to find and modify.
REFRESH_INTERVAL = 1  # How often (in seconds) the stats will update.
                      # A value of 1 means updates every second.


# --- Helper Function: Format Bytes ---
# This function converts raw byte counts into human-readable units (KB, MB, GB, etc.).
# It's a common utility needed when dealing with memory or disk sizes, making them easier to understand.
def format_bytes(bytes_count):
    """
    Converts a byte count (integer) into a human-readable string (e.g., 1024 -> 1.00 KB).
    """
    # Define the units and their corresponding power of 1024.
    # The order matters, from smallest to largest unit.
    units = ["Bytes", "KB", "MB", "GB", "TB", "PB"]
    
    # Initialize index to 0, representing Bytes.
    unit_index = 0
    
    # Loop while the bytes_count is greater than or equal to 1024 (and we still have larger units to use).
    # We divide by 1024 because 1 KB = 1024 Bytes, 1 MB = 1024 KB, and so on.
    while bytes_count >= 1024 and unit_index < len(units) - 1:
        bytes_count /= 1024.0  # Use float division to maintain precision for decimal values.
        unit_index += 1        # Move to the next unit (e.g., from Bytes to KB, then KB to MB).
    
    # Format the number to two decimal places and append the appropriate unit.
    # f-strings are a modern and readable way to format strings in Python.
    return f"{bytes_count:.2f} {units[unit_index]}"


# --- Core Function: Get System Statistics ---
# This function encapsulates all the calls to psutil to fetch the desired metrics.
# Keeping it in a separate function makes the main loop cleaner and easier to read.
def get_system_stats():
    """
    Fetches current CPU, memory, and disk usage statistics using the psutil library.
    Returns a dictionary containing these collected statistics.
    """
    
    # 1. CPU Usage
    # psutil.cpu_percent(interval=None) samples the CPU usage since the last call.
    # Using None means it's non-blocking and calculates the percentage
    # based on the time elapsed *since the last call to cpu_percent* (or module import).
    # For a continuously running loop where `time.sleep()` provides the interval, this is ideal.
    cpu_usage = psutil.cpu_percent(interval=None)

    # 2. Memory Usage (Virtual Memory)
    # psutil.virtual_memory() returns an object with various memory statistics.
    # We are interested in total, available, used, and the percentage used.
    mem_info = psutil.virtual_memory()
    mem_total = mem_info.total       # Total physical memory (RAM).
    mem_used = mem_info.used         # Memory currently in use.
    mem_percent = mem_info.percent   # Percentage of memory used.

    # 3. Disk Usage
    # psutil.disk_usage('/') returns disk usage statistics for the given path.
    # '/' typically represents the root partition on Unix-like systems (Linux, macOS).
    # On Windows, you might use 'C:\\' or specify a different drive letter.
    # This example assumes a Unix-like system or focuses on the primary drive.
    disk_info = psutil.disk_usage('/')
    disk_total = disk_info.total     # Total capacity of the disk partition.
    disk_used = disk_info.used       # Space currently used on the partition.
    disk_percent = disk_info.percent # Percentage of disk space used.
    
    # Return all collected statistics in a dictionary.
    # This makes it easy to access the data by descriptive names later.
    return {
        "cpu_usage": cpu_usage,
        "mem_total": mem_total,
        "mem_used": mem_used,
        "mem_percent": mem_percent,
        "disk_total": disk_total,
        "disk_used": disk_used,
        "disk_percent": disk_percent,
    }


# --- Main Loop: Display Statistics ---
# This function orchestrates the continuous fetching and display of statistics.
def display_stats_loop():
    """
    Continuously fetches and displays system statistics in the terminal.
    Clears the screen between updates for a "real-time" dashboard effect.
    """
    print("Starting real-time system monitor... Press Ctrl+C to exit.")
    
    # The 'while True' loop ensures the program runs indefinitely
    # until explicitly stopped (e.g., by a KeyboardInterrupt from the user).
    while True:
        # Clear the terminal screen.
        # 'os.system()' executes a shell command.
        # 'cls' is the command for clearing the screen on Windows.
        # 'clear' is the command for clearing the screen on Unix-like systems (Linux/macOS).
        # 'os.name' checks the operating system type ('nt' for Windows, 'posix' for Unix-like).
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Get the latest system statistics by calling our helper function.
        stats = get_system_stats()
        
        # --- Print Formatted Output ---
        # This section uses f-strings for clear and concise output formatting.
        print("--- Real-time System Usage ---")
        # CPU usage is printed with one decimal place.
        print(f"CPU Usage:   {stats['cpu_usage']:.1f}%") 
        # Memory usage: format used and total bytes, then add percentage.
        print(f"Memory:      {format_bytes(stats['mem_used'])} / {format_bytes(stats['mem_total'])} ({stats['mem_percent']:.1f}%)")
        # Disk usage: format used and total bytes for the root partition, then add percentage.
        print(f"Disk (Root): {format_bytes(stats['disk_used'])} / {format_bytes(stats['disk_total'])} ({stats['disk_percent']:.1f}%)")
        # Show when the data was last updated for user clarity.
        print(f"\nLast updated: {time.strftime('%Y-%m-%d %H:%M:%S')}") 
        
        # Pause execution for the defined REFRESH_INTERVAL.
        # This creates the "real-time" update effect without hogging CPU resources.
        time.sleep(REFRESH_INTERVAL)


# --- Entry Point of the Program ---
# This block ensures that 'display_stats_loop()' is called only when the script
# is executed directly (i.e., not when imported as a module into another script).
if __name__ == "__main__":
    try:
        # Start the continuous display loop.
        display_stats_loop()
    except KeyboardInterrupt:
        # Catch KeyboardInterrupt (which happens when the user presses Ctrl+C).
        # This allows the program to exit gracefully instead of crashing.
        print("\nExiting system monitor. Goodbye!")
    except Exception as e:
        # Catch any other unexpected errors that might occur during execution
        # and print a descriptive error message.
        print(f"\nAn unexpected error occurred: {e}")

# --- Example Usage ---
# To run this utility:
# 1. Make sure you have 'psutil' installed. If not, open your terminal and run:
#    `pip install psutil`
# 2. Save the code above into a Python file (e.g., `sys_monitor.py`).
# 3. Open your terminal or command prompt.
# 4. Navigate to the directory where you saved the file using the `cd` command.
# 5. Run the script using the Python interpreter:
#    `python sys_monitor.py`
#
# You will see the system statistics update every second in your terminal.
# To stop the monitor, simply press `Ctrl+C`.