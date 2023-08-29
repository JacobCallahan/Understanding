"""Generators that work together are often called coroutines"""
import subprocess
import time
from collections import deque
from pprint import pprint


class AsyncScheduler:
    def __init__(self):
        self.ready = deque()
        self.sleeping = []

    def call_soon(self, coro):
        self.ready.append(coro)

    def call_later(self, coro, delay):
        self.sleeping.append((time.time()+delay, coro))

    def run_until_complete(self):
        while self.ready or self.sleeping:
            if not self.ready and self.sleeping:
                deadline = min(map(lambda sleeper: sleeper[0], self.sleeping))
                if (sleep_for := deadline - time.time()) >0:
                    time.sleep(sleep_for)
                self.call_soon(self.sleeping.pop(0)[1])
            while self.ready:
                self.current = self.ready.popleft()
                try:
                    self.current.send(None)
                    if self.current:
                        self.call_soon(self.current)
                except StopIteration:
                    pass

def sleep(duration):
    until = time.time() + duration
    while time.time() < until:
        yield

def do_tasks(tasks, duration=3):
    for task in tasks:
        print(f"Running {task=}")
        yield from sleep(duration)

def monitor_process(process):
    while process.poll() is None:
        yield

def run_command(command):
    print(f"Running {command=}")
    process = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    yield from monitor_process(process)
    stdout, stderr = process.communicate()
    pprint({
        "command": command,
        "stdout": stdout.decode() if stdout else None,
        "stderr": stderr.decode() if stderr else None,
        "status": process.returncode,
        "pid": process.pid
    })

asyncio = AsyncScheduler()
asyncio.call_soon(do_tasks(["task1", "task2", "task3"]))
asyncio.call_soon(do_tasks(["task4", "task5", "task6"], duration=1))
asyncio.call_soon(run_command(["ls -l"]))
asyncio.call_soon(run_command(["ping -c 3 google.com"]))
asyncio.call_later(run_command(["hostname"]), 10)
asyncio.run_until_complete()
