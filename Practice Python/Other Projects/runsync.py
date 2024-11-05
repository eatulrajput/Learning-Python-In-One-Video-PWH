import os
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, extensions):
        self.extensions = extensions

    def on_modified(self, event):
        if event.is_directory:
            return
        if any(event.src_path.endswith(ext) for ext in self.extensions):
            print(f"Detected change in {event.src_path}")
            self.run_file(event.src_path)

    def run_file(self, path):
        # Run file based on extension
        if path.endswith('.py'):
            subprocess.run(["python", path])
        elif path.endswith('.go'):
            subprocess.run(["go", "run", path])
        elif path.endswith('.c'):
            # Compile and run C files
            output_file = path.rsplit('.', 1)[0]
            subprocess.run(["gcc", path, "-o", output_file])
            subprocess.run([f"./{output_file}"])
        # Add more cases as needed for other file types

def start_watching(directory, extensions):
    event_handler = FileChangeHandler(extensions)
    observer = Observer()
    observer.schedule(event_handler, directory, recursive=False)
    observer.start()
    print(f"Watching directory: {directory}")

    try:
        while True:
            pass  # Keeps the script running
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# Start watching
directory_to_watch = "/path/to/directory"
extensions_to_watch = [".py", ".c", ".cpp", ".go"]
start_watching(directory_to_watch, extensions_to_watch)
