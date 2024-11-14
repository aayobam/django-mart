import os
import requests
import logging
import datetime


class FileUploadMiddleware:
    @staticmethod
    def read_in_chunck(self, file_object, chunk_size):
        while True:
            data = file_object.read(chunk_size)
            if not data:
                break
            yield data

    @staticmethod
    def upload_file(self, file, urls):
        content_name = str(file)
        content_path = os.path.abspath(content_name)
        content_size = os.stat(content_path).st_size
        file_object = open(content_path, "rb")
        index = 0
        offset = 0
        headers = {}
        chunk_size = 1024

        for chunk in self.read_in_chunck(file_object, chunk_size):
            offset = index + len(chunk)
            headers["Content-Range"] = f"bytes {index} - {offset - 1} / {content_size}"
            index = offset
            try:
                file = {"file": chunk}
                r = requests.post(urls, files=file, headers=headers)
            except:
                logging.error(f"error in sending chuncks of files | {datetime.timezone.fromutc}")
