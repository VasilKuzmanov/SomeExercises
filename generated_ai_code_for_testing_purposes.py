import os

class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def write_to_file(self, data):
        with open(self.filename, 'w') as file:
            file.write(data)

    def read_from_file(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return file.read()
        else:
            return "File not found."

def main():
    file_manager = FileManager("sample.txt")

    data_to_write = "Hello, this is a sample text file!"
    file_manager.write_to_file(data_to_write)
    print(f"Data written to file: {data_to_write}")

    data_read = file_manager.read_from_file()
    print(f"Data read from file: {data_read}")

if __name__ == "__main__":
    main()
