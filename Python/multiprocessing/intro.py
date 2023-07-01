"""mutliprocessing is a great way to speed up cpu-bound tasks"""
import multiprocessing

def square_sum(numbers):
    """Calculate the sum of squares of a list of numbers."""
    total = sum([num**2 for num in numbers])
    print(f"Sum of squares from {numbers=}: {total}")

# Define the list of numbers to calculate the sum of squares for
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Divide the list of numbers into 2 chunks
chunk1 = numbers[:5]
chunk2 = numbers[5:]

process1 = multiprocessing.Process(target=square_sum, args=(chunk1,))
process2 = multiprocessing.Process(target=square_sum, args=(chunk2,))

process1.start()
process2.start()

process1.join()
process2.join()
