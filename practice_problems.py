"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    seen = set()
    for pid in product_ids:
        if pid in seen:
            return True
        seen.add(pid)
    return False

# Justification:
# I used a set because it provides O(1) average-time membership checks, making it ideal for detecting duplicates efficiently.
# As we iterate, checking whether an element is already in the set is fast, and insertion is also O(1).
# Using a list would require O(n) duplicate checks per element, resulting in much slower performance.

    pass


"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

from collections import deque

class TaskQueue:
    def __init__(self):
        self.queue = deque()

    def add_task(self, task):
        self.queue.append(task)

    def remove_oldest_task(self):
        if self.queue:
            return self.queue.popleft()
        return None

# Justification:
# I used a deque because it supports O(1) enqueue (append) and O(1) dequeue (popleft), which is perfect for FIFO task processing.
# A list would make removing from the front O(n), which becomes inefficient as the number of tasks grows.
# The deque ensures tasks are processed in the exact order they were added. Also, this was the best idea I had. 

        pass

    def add_task(self, task):
        pass

    def remove_oldest_task(self):
        pass


"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    def __init__(self):
        self.seen = set()

    def add(self, value):
        self.seen.add(value)

    def get_unique_count(self):
        return len(self.seen)

# Justification:
# I used a set because it automatically maintains unique values and supports O(1) average-time insertion and membership checks.
# This makes counting unique values extremely efficient, even with large input streams.
# Using a list would require O(n) duplicate checks, making it slower and less scalable.

