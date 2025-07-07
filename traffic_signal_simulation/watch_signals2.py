# import time
# import sys
# import lgpio
# import json
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
# from google.cloud import vision

# ########## Load traffic.json to access data ################
# FILE_PATH = r"/home/pi/Desktop/Smart-Traffic-Control-and-Surveillance-System-v2/traffic_signal_simulation/traffic.json"

# # Load existing dictionary (if available)
# def load_data():
#     try:
#         with open(FILE_PATH, "r") as file:
#             return json.load(file)
#     except (FileNotFoundError, json.JSONDecodeError):
#         return {}  # Default to empty dict if file doesn't exist or is corrupted

# ############# Raspberry Pi #####################

# H=lgpio.gpiochip_open(0)

# traffic_lights=[17,27,5,6,13,19,26,18,23,24,25,9] # R1,R2...Y4

# for light in traffic_lights:
#     lgpio.gpio_claim_output(H,light)

# ############## Watch traffic.json ####################

# WATCH_FOLDER="/home/pi/Desktop/Smart-Traffic-Control-and-Surveillance-System-v2/traffic_signal_simulation"

# class detected_image_Handler(FileSystemEventHandler):
#     def on_modified(self, event):
#         if event.is_directory:
#             return
        
#         file_path = event.src_path
        
#         if file_path.lower().endswith(('.json')):
#             traffic=load_data()
#             for light in traffic_lights:
#                 lgpio.gpio_write(H,light,0) # off all lights

#             X="R"
#             for i in range (12):
#                 if(traffic[X+f"{(((i)%4)+1)}"]):
#                     lgpio.gpio_write(H,traffic_lights[i],1)
#                 if(i==3):
#                     X="G"
#                 if(i==7):
#                     X="Y"

#             print(f"TRAFFIC SIGNALS ARE UPDATED")
        
# def start_monitoring():
#     """Start monitoring the folder for new images."""
#     event_handler = detected_image_Handler()
#     observer = Observer()
#     observer.schedule(event_handler, WATCH_FOLDER, recursive=True)
#     observer.start()
#     print(f"Watching folder: {WATCH_FOLDER}")
    
#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         observer.stop()
#     observer.join()

# if __name__ == "__main__":
#     start_monitoring()


# import time
# import sys
# import lgpio
# import json
# import os
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
# from google.cloud import vision

# ########## Load traffic.json to access data ################
# FILE_PATH = r"/home/pi/Desktop/Smart-Traffic-Control-and-Surveillance-System-v2/traffic_signal_simulation/traffic.json"

# # Load existing dictionary (if available)
# def load_data():
#     try:
#         with open(FILE_PATH, "r") as file:
#             data = json.load(file)
#             print(f"Loaded traffic data: {data}")  # Debug print
#             return data
#     except (FileNotFoundError, json.JSONDecodeError) as e:
#         print(f"Error loading traffic data: {e}")
#         return {}  # Default to empty dict if file doesn't exist or is corrupted

# ############# Raspberry Pi #####################

# H = lgpio.gpiochip_open(0)

# traffic_lights = [17, 27, 5, 6, 13, 19, 26, 18, 23, 24, 25, 9]  # R1,R2...Y4

# # Initialize GPIO pins
# for light in traffic_lights:
#     try:
#         lgpio.gpio_claim_output(H, light)
#         lgpio.gpio_write(H, light, 0)  # Start with all lights off
#         print(f"GPIO {light} initialized successfully")
#     except Exception as e:
#         print(f"Error initializing GPIO {light}: {e}")

# ############## Watch traffic.json ####################

# WATCH_FOLDER = "/home/pi/Desktop/Smart-Traffic-Control-and-Surveillance-System-v2/traffic_signal_simulation"

# class detected_image_Handler(FileSystemEventHandler):
#     def on_modified(self, event):
#         if event.is_directory:
#             return
        
#         file_path = event.src_path
#         print(f"File modified: {file_path}")  # Debug print
        
#         if file_path.lower().endswith('.json') and 'traffic.json' in file_path:
#             try:
#                 traffic = load_data()
                
#                 # Validate that we have traffic data
#                 if not traffic:
#                     print("No traffic data available")
#                     return
                
#                 # Turn off all lights first
#                 for light in traffic_lights:
#                     lgpio.gpio_write(H, light, 0)
                
#                 print("All lights turned off, updating based on traffic data...")
                
#                 # Update lights based on traffic.json with safe key access
#                 X = "R"
#                 for i in range(12):
#                     key = X + f"{((i % 4) + 1)}"
#                     print(f"Checking key: {key}, Value: {traffic.get(key, False)}")
                    
#                     if traffic.get(key, False):  # Safe dictionary access
#                         lgpio.gpio_write(H, traffic_lights[i], 1)
#                         print(f"Turned ON light {i} (GPIO {traffic_lights[i]}) for key {key}")
#                     else:
#                         lgpio.gpio_write(H, traffic_lights[i], 0)
#                         print(f"Turned OFF light {i} (GPIO {traffic_lights[i]}) for key {key}")
                    
#                     if i == 3:
#                         X = "G"
#                     if i == 7:
#                         X = "Y"
                
#                 print("TRAFFIC SIGNALS ARE UPDATED")
                
#             except Exception as e:
#                 print(f"Error updating traffic signals: {e}")

# def create_sample_traffic_json():
#     """Create a sample traffic.json file if it doesn't exist"""
#     if not os.path.exists(FILE_PATH):
#         sample_data = {
#             "R1": True, "R2": False, "R3": False, "R4": False,
#             "G1": False, "G2": True, "G3": False, "G4": False,
#             "Y1": False, "Y2": False, "Y3": True, "Y4": False
#         }
#         try:
#             with open(FILE_PATH, 'w') as f:
#                 json.dump(sample_data, f, indent=2)
#             print(f"Created sample traffic.json at {FILE_PATH}")
#         except Exception as e:
#             print(f"Error creating sample file: {e}")

# def test_all_lights():
#     """Test all lights by turning them on briefly"""
#     print("Testing all lights...")
#     for i, light in enumerate(traffic_lights):
#         lgpio.gpio_write(H, light, 1)
#         print(f"Testing light {i} (GPIO {light})")
#         time.sleep(0.5)
#         lgpio.gpio_write(H, light, 0)
#         time.sleep(0.2)
#     print("Light test completed")

# def start_monitoring():
#     """Start monitoring the folder for JSON file changes."""
#     # Create sample file if needed
#     create_sample_traffic_json()
    
#     # Test all lights first
#     test_all_lights()
    
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
#     finally:
#         # Clean up GPIO resources
#         print("Cleaning up GPIO resources...")
#         for light in traffic_lights:
#             lgpio.gpio_write(H, light, 0)  # Turn off all lights
#         lgpio.gpiochip_close(H)
#         print("GPIO cleanup completed")
    
#     observer.join()

# if __name__ == "__main__":
#     start_monitoring()

import time
import sys
import lgpio
import json
import os
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

########## Load traffic.json to access data ################
FILE_PATH = r"/home/pi/Desktop/Smart-Traffic-Control-and-Surveillance-System-v2/traffic_signal_simulation/traffic.json"

# Load existing dictionary (if available)
def load_data():
    try:
        with open(FILE_PATH, "r") as file:
            data = json.load(file)
            print(f"Loaded traffic data: {data}")
            return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading traffic data: {e}")
        return {}

############# Raspberry Pi GPIO Setup #####################

H = lgpio.gpiochip_open(0)

# Traffic lights GPIO pins (existing)
traffic_lights = [17, 27, 5, 6, 13, 19, 26, 18, 23, 24, 25, 9]  # R1,R2...Y4

# 7-Segment Display GPIO Pins - Fixed for Common Cathode
# Using different pins to avoid conflicts with traffic lights
SEGMENT_PINS = {
    'a': 2,   # Top segment
    'b': 3,   # Top right segment  
    'c': 4,   # Bottom right segment
    'd': 14,  # Bottom segment
    'e': 15,  # Bottom left segment
    'f': 7,   # Top left segment (changed from 18 to avoid conflict)
    'g': 8,   # Middle segment (changed from 22 to avoid conflict)
    'dp': 10  # Decimal point
}

# Digit control pins for multiplexing (Common Cathode - LOW to turn ON)
DIGIT_PINS = [11, 12]  # Control pins for tens and units digit

# 7-Segment digit patterns for Common Cathode (1 = ON, 0 = OFF)
DIGIT_PATTERNS = {
    0: {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 0, 'dp': 0},  # 0
    1: {'a': 0, 'b': 1, 'c': 1, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'dp': 0},  # 1
    2: {'a': 1, 'b': 1, 'c': 0, 'd': 1, 'e': 1, 'f': 0, 'g': 1, 'dp': 0},  # 2
    3: {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 0, 'f': 0, 'g': 1, 'dp': 0},  # 3
    4: {'a': 0, 'b': 1, 'c': 1, 'd': 0, 'e': 0, 'f': 1, 'g': 1, 'dp': 0},  # 4
    5: {'a': 1, 'b': 0, 'c': 1, 'd': 1, 'e': 0, 'f': 1, 'g': 1, 'dp': 0},  # 5
    6: {'a': 1, 'b': 0, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'dp': 0},  # 6
    7: {'a': 1, 'b': 1, 'c': 1, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'dp': 0},  # 7
    8: {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1, 'f': 1, 'g': 1, 'dp': 0},  # 8
    9: {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 0, 'f': 1, 'g': 1, 'dp': 0},  # 9
    'off': {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'dp': 0}  # All off
}

# Initialize GPIO pins
def initialize_gpio():
    # Initialize traffic lights
    for light in traffic_lights:
        try:
            lgpio.gpio_claim_output(H, light)
            lgpio.gpio_write(H, light, 0)
            print(f"Traffic light GPIO {light} initialized successfully")
        except Exception as e:
            print(f"Error initializing traffic light GPIO {light}: {e}")
    
    # Initialize 7-segment display pins
    for segment, pin in SEGMENT_PINS.items():
        try:
            lgpio.gpio_claim_output(H, pin)
            lgpio.gpio_write(H, pin, 0)  # Start with segments off
            print(f"Segment {segment} GPIO {pin} initialized successfully")
        except Exception as e:
            print(f"Error initializing segment {segment} GPIO {pin}: {e}")
    
    # Initialize digit control pins
    for i, pin in enumerate(DIGIT_PINS):
        try:
            lgpio.gpio_claim_output(H, pin)
            lgpio.gpio_write(H, pin, 1)  # Start with digits off (Common Cathode - HIGH = OFF)
            print(f"Digit {i+1} GPIO {pin} initialized successfully")
        except Exception as e:
            print(f"Error initializing digit {i+1} GPIO {pin}: {e}")

############# 7-Segment Display Control #####################

class SevenSegmentController:
    def __init__(self):
        self.current_number = 0
        self.display_active = True
        self.display_thread = None
        self.lock = threading.Lock()
        self.start_display_thread()
    
    def start_display_thread(self):
        """Start the display refresh thread"""
        self.display_thread = threading.Thread(target=self._refresh_display, daemon=True)
        self.display_thread.start()
    
    def _refresh_display(self):
        """Continuously refresh the display using multiplexing"""
        while self.display_active:
            with self.lock:
                number = self.current_number
            
            if number < 0 or number > 99:
                number = 0
            
            tens_digit = number // 10
            units_digit = number % 10
            
            # Display tens digit (only if > 0 to avoid leading zero)
            if tens_digit > 0:
                self._show_digit(tens_digit, 0)  # Position 0 = tens
            else:
                self._clear_digit(0)
            
            time.sleep(0.005)  # 5ms
            
            # Display units digit
            self._show_digit(units_digit, 1)  # Position 1 = units
            time.sleep(0.005)  # 5ms
    
    def _show_digit(self, digit, position):
        """Show a specific digit at a specific position"""
        # Turn off all digits first
        for pin in DIGIT_PINS:
            lgpio.gpio_write(H, pin, 1)  # HIGH = OFF for Common Cathode
        
        # Set segment pattern
        pattern = DIGIT_PATTERNS.get(digit, DIGIT_PATTERNS['off'])
        for segment, pin in SEGMENT_PINS.items():
            lgpio.gpio_write(H, pin, pattern[segment])
        
        # Turn on the specific digit
        if position < len(DIGIT_PINS):
            lgpio.gpio_write(H, DIGIT_PINS[position], 0)  # LOW = ON for Common Cathode
    
    def _clear_digit(self, position):
        """Clear a specific digit position"""
        # Turn off all digits first
        for pin in DIGIT_PINS:
            lgpio.gpio_write(H, pin, 1)
        
        # Set all segments off
        for segment, pin in SEGMENT_PINS.items():
            lgpio.gpio_write(H, pin, 0)
        
        # Turn on the digit position briefly to show "off"
        if position < len(DIGIT_PINS):
            lgpio.gpio_write(H, DIGIT_PINS[position], 0)
    
    def update_timer(self, value):
        """Update the timer value to display"""
        with self.lock:
            self.current_number = max(0, min(99, value))
        print(f"7-Segment display updated: {self.current_number:02d}")
    
    def stop_display(self):
        """Stop the display"""
        self.display_active = False
        if self.display_thread:
            self.display_thread.join()
        self._clear_display()
    
    def _clear_display(self):
        """Clear all segments"""
        for pin in DIGIT_PINS:
            lgpio.gpio_write(H, pin, 1)  # Turn off digits
        for segment, pin in SEGMENT_PINS.items():
            lgpio.gpio_write(H, pin, 0)  # Turn off segments

# Global display controller
seven_segment_controller = None

############## Watch traffic.json ####################

WATCH_FOLDER = "/home/pi/Desktop/Smart-Traffic-Control-and-Surveillance-System-v2/traffic_signal_simulation"

class detected_image_Handler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        
        file_path = event.src_path
        print(f"File modified: {file_path}")
        
        if file_path.lower().endswith('.json') and 'traffic.json' in file_path:
            try:
                traffic = load_data()
                
                if not traffic:
                    print("No traffic data available")
                    return
                
                # Update 7-segment display with countdown timer
                self._update_display(traffic)
                
                # Update traffic lights
                self._update_traffic_lights(traffic)
                
                print("TRAFFIC SIGNALS AND DISPLAY UPDATED")
                
            except Exception as e:
                print(f"Error updating traffic signals: {e}")
    
    def _update_display(self, traffic):
        """Update the 7-segment display with timer value"""
        global seven_segment_controller
        
        if seven_segment_controller is None:
            return
        
        # Get current timer value from traffic data
        current_timer = traffic.get("C", 0)
        seven_segment_controller.update_timer(current_timer)
    
    def _update_traffic_lights(self, traffic):
        """Update traffic lights based on traffic data"""
        # Turn off all lights first
        for light in traffic_lights:
            lgpio.gpio_write(H, light, 0)
        
        print("All lights turned off, updating based on traffic data...")
        
        # Update lights based on traffic.json with safe key access
        X = "R"
        for i in range(12):
            key = X + f"{((i % 4) + 1)}"
            print(f"Checking key: {key}, Value: {traffic.get(key, False)}")
            
            if traffic.get(key, False):
                lgpio.gpio_write(H, traffic_lights[i], 1)
                print(f"Turned ON light {i} (GPIO {traffic_lights[i]}) for key {key}")
            else:
                lgpio.gpio_write(H, traffic_lights[i], 0)
                print(f"Turned OFF light {i} (GPIO {traffic_lights[i]}) for key {key}")
            
            if i == 3:
                X = "G"
            if i == 7:
                X = "Y"

def create_sample_traffic_json():
    """Create a sample traffic.json file if it doesn't exist"""
    if not os.path.exists(FILE_PATH):
        sample_data = {
            "R1": True, "R2": True, "R3": True, "R4": True,
            "G1": False, "G2": False, "G3": False, "G4": False,
            "Y1": False, "Y2": False, "Y3": False, "Y4": False,
            "C": 0,  # Current timer value
            "T1": 1, "T2": 3, "T3": 8, "T4": 20,  # Traffic density
            "A1": False, "A2": False, "A3": False, "A4": False  # Ambulance flags
        }
        try:
            with open(FILE_PATH, 'w') as f:
                json.dump(sample_data, f, indent=2)
            print(f"Created sample traffic.json at {FILE_PATH}")
        except Exception as e:
            print(f"Error creating sample file: {e}")

def test_all_components():
    """Test all components"""
    global seven_segment_controller
    
    print("Testing traffic lights...")
    for i, light in enumerate(traffic_lights):
        lgpio.gpio_write(H, light, 1)
        print(f"Testing light {i} (GPIO {light})")
        time.sleep(0.3)
        lgpio.gpio_write(H, light, 0)
        time.sleep(0.1)
    print("Traffic light test completed")
    
    if seven_segment_controller:
        print("Testing 7-segment display...")
        for i in range(10, -1, -1):
            seven_segment_controller.update_timer(i)
            time.sleep(0.5)
        seven_segment_controller.update_timer(0)
        print("7-segment display test completed")

def start_monitoring():
    """Start monitoring the folder for JSON file changes"""
    global seven_segment_controller
    
    # Initialize GPIO
    initialize_gpio()
    
    # Initialize 7-segment display controller
    seven_segment_controller = SevenSegmentController()
    
    # Create sample file if needed
    create_sample_traffic_json()
    
    # Test all components
    test_all_components()
    
    # Load initial state
    traffic = load_data()
    if traffic:
        print("Loading initial traffic state...")
        handler = detected_image_Handler()
        class MockEvent:
            def __init__(self):
                self.is_directory = False
                self.src_path = FILE_PATH
        handler.on_modified(MockEvent())
    
    event_handler = detected_image_Handler()
    observer = Observer()
    observer.schedule(event_handler, WATCH_FOLDER, recursive=True)
    observer.start()
    print(f"Watching folder: {WATCH_FOLDER}")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping monitoring...")
        observer.stop()
    except Exception as e:
        print(f"Error in monitoring: {e}")
        observer.stop()
    finally:
        # Clean up GPIO resources
        print("Cleaning up GPIO resources...")
        
        # Stop 7-segment display
        if seven_segment_controller:
            seven_segment_controller.stop_display()
        
        # Turn off all traffic lights
        for light in traffic_lights:
            lgpio.gpio_write(H, light, 0)
        
        # Turn off all 7-segment displays
        for pin in DIGIT_PINS:
            lgpio.gpio_write(H, pin, 1)
        for segment, pin in SEGMENT_PINS.items():
            lgpio.gpio_write(H, pin, 0)
        
        lgpio.gpiochip_close(H)
        print("GPIO cleanup completed")
    
    observer.join()

if __name__ == "__main__":
    start_monitoring()
