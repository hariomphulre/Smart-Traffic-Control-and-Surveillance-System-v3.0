import time
import sys
import lgpio
import json
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import drivers
from time import sleep
display = drivers.Lcd()

########## Load traffic.json to access data ################
FILE_PATH = r"/home/pi/Desktop/Smart-Traffic-Control-and-Surveillance-System-v3.0/traffic_signal_simulation/traffic.json"

# Load existing dictionary (if available)
def load_data():
    try:
        with open(FILE_PATH, "r") as file:
            data = json.load(file)
            # print(f"Loaded traffic data: {data}") 
            return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading traffic data: {e}")
        return {}  

WATCH_FOLDER = "/home/pi/Desktop/Smart-Traffic-Control-and-Surveillance-System-v3.0/traffic_signal_simulation"

class detected_image_Handler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        
        file_path = event.src_path
        # print(f"File modified: {file_path}")  # Debug print
        
        if file_path.lower().endswith('.json') and 'traffic.json' in file_path:
            try:
                traffic = load_data()

                c_value = traffic.get("C", "N/A")
                if isinstance(c_value, int):
                    c_str = f"{c_value:02d}"
                else:
                    c_str = str(c_value)

                display.lcd_clear()
                display.lcd_display_string(f"R1 Timer: {c_str}".ljust(16), 1)

                print(f"R1 Countdown updated: {c_value}")
                
            except KeyboardInterrupt:
                print(f"Error updating countdown: {e}")
                # print("Cleaning up!")
                display.lcd_clear()

if __name__ == "__main__":
    observer = Observer()
    handler = detected_image_Handler()
    observer.schedule(handler, path=WATCH_FOLDER, recursive=True)
    observer.start()
    print("Watching for file changes...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# def start_monitoring():
#     """Start monitoring the folder for JSON file changes."""
    
#     # Load initial state
#     traffic = load_data()
#     if traffic:
#         print("Loading initial traffic state...")
#         # Trigger initial update
#         handler = detected_image_Handler()
#         class MockEvent:
#             def __init__(self):
#                 self.is_directory = False
#                 self.src_path = FILE_PATH
#         handler.on_modified(MockEvent())
    
#     event_handler = detected_image_Handler()
#     observer = Observer()
#     observer.schedule(event_handler, WATCH_FOLDER, recursive=True)
#     observer.start()
#     print(f"Watching folder: {WATCH_FOLDER}")
    
#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         print("Stopping monitoring...")
#         observer.stop()
#     except Exception as e:
#         print(f"Error in monitoring: {e}")
#         observer.stop()