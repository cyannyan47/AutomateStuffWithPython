# Check newly download files and move them to the correct folder
# Code copied from https://www.youtube.com/watch?v=qbW6FRbaSl0

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


import os
import json
import time

class MyHandler(FileSystemEventHandler):
  
  def on_modified(self, event):
    for filename in os.listdir(folderToTrack):
      src = folderToTrack + "/" + filename
      newDestination = folderDestination + "/" + filename
      os.rename(src, newDestination)

folderToTrack = '/Users/quang/Desktop'
folderDestination = '/Users/quang/Documents'
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

