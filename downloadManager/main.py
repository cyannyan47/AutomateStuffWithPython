# Check newly download files and move them to the correct folder
# Code copied from https://www.youtube.com/watch?v=qbW6FRbaSl0

import os
import json
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
  
  def on_any_event(self, event):
    for filename in os.listdir(folderToTrack):
      src = os.path.join(folderToTrack, filename)
      print(src)
      newDestination = os.path.join(folderDestination, filename)
      print(newDestination)
      os.rename(src, newDestination)
      print("Moved")

folderToTrack = "/mnt/c/Users/quang/Desktop/Test1"
folderDestination = "/mnt/c/Users/quang/Desktop/Test2"
eventHandler = MyHandler()
observer = Observer()
observer.schedule(eventHandler, folderToTrack, recursive=True)
observer.start()

try:
  while True:
    time.sleep(10)
except KeyboardInterrupt:
  observer.stop()

observer.join()

