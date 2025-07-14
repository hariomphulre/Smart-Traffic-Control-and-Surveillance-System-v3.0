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
FILE_PATH = r"/home/pi/Desktop/Smart-Traffic-Control-and-Surveillance-System-v3.0/traffic_signal_simulation/traffic2.json"

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
        
        if file_path.lower().endswith('.json') and 'traffic2.json' in file_path:
            try:
                traffic = load_data()

                c1_value = traffic.get("C1", "N/A")
                if isinstance(c1_value, int):
                    c1_str = f"{c1_value:02d}"
                else:
                    c1_str = str(c1_value)
                
                c2_value = traffic.get("C2", "N/A")
                if isinstance(c2_value, int):
                    c2_str = f"{c2_value:02d}"
                else:
                    c2_str = str(c2_value)

                c3_value = traffic.get("C3", "N/A")
                if isinstance(c3_value, int):
                    c3_str = f"{c3_value:02d}"
                else:
                    c3_str = str(c3_value)

                c4_value = traffic.get("C4", "N/A")
                if isinstance(c4_value, int):
                    c4_str = f"{c4_value:02d}"
                else:
                    c4_str = str(c4_value)

                display.lcd_clear()
                # display.lcd_display_string(f"R1 Timer: {c1_str}".ljust(16), 1)
                # if(traffic.get("A1","N/A")):
                #     display.lcd_display_string(f"      EMERGENCY!".ljust(16), 2)

                # print(f"R1 Countdown updated: {c1_value}")


                display.lcd_display_string(f"C1: {c1_str} ,C2: {c2_str}".ljust(16), 1)
                display.lcd_display_string(f"C3: {c3_str} ,C4: {c4_str}".ljust(16), 2)
                
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

    # try:
    #     while True:
    #         time.sleep(1)
    # except KeyboardInterrupt:
    #     observer.stop()
    # observer.join()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopped by user.")
    finally:
        observer.stop()
        observer.join()
        display.lcd_clear()  # Clear the display on exit
        print("Display cleared and observer stopped.")

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