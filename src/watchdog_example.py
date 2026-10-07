from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f"Modified: {event.src_path}")

    def on_created(self, event):
        print(f"Created: {event.src_path}")

observer = Observer()
observer.schedule(Handler(), path=".", recursive=True)
observer.start()
time.sleep(30)
observer.stop()