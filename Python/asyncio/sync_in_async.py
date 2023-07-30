import asyncio
import subprocess

async def run_command(command):
    print_friendly = " ".join(command)
    print(f"Running command: {print_friendly}")
    process = await asyncio.to_thread(
        subprocess.run, command, stdin=subprocess.PIPE, stdout=subprocess.PIPE
    )
    print(f"Command {print_friendly} finished with return code {process.returncode}")
    if process.stdout:
        print(f"Command {print_friendly} stdout:\n{process.stdout.decode()}")
    if process.stderr:
        print(f"Command {print_friendly} stderr:\n{process.stderr.decode()}")

async def main():
    commands = [
        ["whoami"],
        ["ping", "-c", "5", "google.com"],
        ["lsb_release", "-a"],
        ["python", "--version"],
    ]
    tasks = []
    for command in commands:
        task = asyncio.create_task(run_command(command))
        tasks.append(task)
    await asyncio.gather(*tasks)

asyncio.run(main())
