import os
import time
from datetime import datetime

class File:
    def __init__(self, filename, created_time, updated_time):
        self.filename = filename
        self.created_time = created_time
        self.updated_time = updated_time

    def is_changed(self, snapshot_time):
        return self.updated_time > snapshot_time

    def info(self):
        return f"{self.filename} - Created: {datetime.fromtimestamp(self.created_time)}, Updated: {datetime.fromtimestamp(self.updated_time)}"

class ImageFile(File):
    def __init__(self, filename, created_time, updated_time, image_size):
        super().__init__(filename, created_time, updated_time)
        self.image_size = image_size

    def info(self):
        return f"{super().info()}, Image Size: {self.image_size}"

class TextFile(File):
    def __init__(self, filename, created_time, updated_time, line_count, word_count, char_count):
        super().__init__(filename, created_time, updated_time)
        self.line_count = line_count
        self.word_count = word_count
        self.char_count = char_count

    def info(self):
        return f"{super().info()}, Line Count: {self.line_count}, Word Count: {self.word_count}, Character Count: {self.char_count}"

class ProgramFile(File):
    def __init__(self, filename, created_time, updated_time, line_count, class_count, method_count):
        super().__init__(filename, created_time, updated_time)
        self.line_count = line_count
        self.class_count = class_count
        self.method_count = method_count

    def info(self):
        return f"{super().info()}, Line Count: {self.line_count}, Class Count: {self.class_count}, Method Count: {self.method_count}"

class FolderMonitor:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.files = {}
        self.snapshot_time = time.time()
        self.load_files()

    def load_files(self):
        for filename in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, filename)
            if os.path.isfile(file_path):
                created_time = os.path.getctime(file_path)
                updated_time = os.path.getmtime(file_path)

                if filename.lower().endswith((".jpg", ".png")):
                    file = ImageFile(filename, created_time, updated_time, "1024x860")
                elif filename.lower().endswith(".txt"):
                    with open(file_path, 'r') as text_file:
                        lines = text_file.readlines()
                        line_count = len(lines)
                        word_count = sum(len(line.split()) for line in lines)
                        char_count = sum(len(line) for line in lines)
                    file = TextFile(filename, created_time, updated_time, line_count, word_count, char_count)
                elif filename.lower().endswith((".py", ".java")):
                    with open(file_path, 'r') as program_file:
                        lines = program_file.readlines()
                        line_count = len(lines)
                        class_count = sum(1 for line in lines if line.strip().startswith("class "))
                        method_count = sum(1 for line in lines if line.strip().startswith("def "))
                    file = ProgramFile(filename, created_time, updated_time, line_count, class_count, method_count)
                else:
                    file = File(filename, created_time, updated_time)

                self.files[filename] = file

    def commit(self):
        self.snapshot_time = time.time()
        print("Snapshot time updated.")

    def info(self, filename):
        file = self.files.get(filename)
        if file:
            print(file.info())
        else:
            print("File not found.")

    def status(self):
        print("Status:")
        for filename, file in self.files.items():
            changed = "Changed" if file.is_changed(self.snapshot_time) else "Not Changed"
            print(f"{filename} - {changed}")

    def list_files(self):
        print("List of files:")
        for filename in self.files:
            print(filename)

if __name__ == "__main__":
    # Updated folder path
    folder_path = "C:\\Users\\User\\Desktop\\lab2"

    # Create an instance of FolderMonitor
    folder_monitor = FolderMonitor(folder_path)

    while True:
        command = input("Enter a command (commit, info <filename>, status): ").split()

        if command[0] == "commit":
            folder_monitor.commit()
        elif command[0] == "info":
            if len(command) == 2:
                folder_monitor.list_files()  # Debug: Print the list of files
                folder_monitor.info(command[1])
            else:
                print("Invalid command. Usage: info <filename>")
        elif command[0] == "status":
            folder_monitor.status()
        else:
            print("Invalid command. Please enter a valid command.")
