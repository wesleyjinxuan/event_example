
import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import pandas as pd
# import the data processing class (DataProcess)

class EventHandler(FileSystemEventHandler):

    def on_created(self, event):
        
        # output location
        input_location = event.src_path
        output_location = os.path.join(os.path.dirname(__file__), "processed_data", "")
        
        raw_file_name = os.path.basename(input_location)
        processed_file_name = output_location + raw_file_name

        # file = open(input_location, "r")
        data = pd.read_csv(input_location)

        # call a method in the data processing class to load the file from input_location, then process, then save to output_location, eg:
        # DataProcess.process(input_location, output_location)     
           
        data.to_csv(processed_file_name, index=False)

        
        print (f"File loaded from {input_location} and saved to {output_location}")


file_observer = Observer()
event_handler = EventHandler()

file_observer.schedule(event_handler, path=os.path.join(os.path.dirname(__file__), "raw_data"))
file_observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    file_observer.stop()

file_observer.join()

if __name__ == "__main__":
    main()