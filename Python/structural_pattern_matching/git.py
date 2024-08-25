"""Matching against sequences starts to show SPM's utility"""
import sys

match sys.argv[1:]:
    case ["init"]:
        print("Initializing a new git repository")
    case ["add", "-u" | "."]:
        print("Adding multiple files.")
    case ["add", filename]:
        print(f"Adding '{filename}' to the staging area...")
    case ["add", *filenames]:
        print(f"Adding multiple files: {filenames}")
    case ["commit", "-m", message]:
        print(f"Committing change with message: '{message}'")
    case miss:
        print(
            f"Invalid command: {miss}.\n" "Try 'init', 'add', or 'commit -m <message>'"
        )
