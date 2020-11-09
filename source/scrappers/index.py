import os

class Scrapper():
    def does_file_exist(self, file_path):
        return os.path.isfile(file_path)        