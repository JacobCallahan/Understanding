"""Logging is an important part of any non-trivial program"""
import logging
import sys

logger = logging.getLogger("myapp")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    fmt="[{levelname} {name} {asctime}] {message}",
    datefmt="%H:%M:%S",
    style="{",
)

handler = logging.StreamHandler(stream=sys.stderr)
handler.setFormatter(formatter)
handler.setLevel(logging.INFO)
logger.addHandler(handler)

file_handler = logging.FileHandler("myapp.log")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)
logger.addHandler(file_handler)

print("I'm here first!")

logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")

print("I'm here last!")
