"""Python threads aren't truly parallel, but are still useful for I/O bound tasks"""
import threading
import requests
from pathlib import Path

def download_file(url, filename):
    print(f"Downloading {url} to {filename}")
    response = requests.get(url)
    Path(filename).write_bytes(response.content)
    print(f"Finished downloading {filename}")

base_url = "https://raw.githubusercontent.com/JacobCallahan/Understanding/master/Python/file_io"
urls = [
    f"{base_url}/binary_file",
    f"{base_url}/files.py",
    f"{base_url}/names.txt",
    f"{base_url}/new_file.txt",
]

threads = []
for url in urls:
    filename = "downloads/" + url.split("/")[-1]
    t = threading.Thread(target=download_file, args=(url, filename))
    t.start()
    threads.append(t)

[t.join() for t in threads]
