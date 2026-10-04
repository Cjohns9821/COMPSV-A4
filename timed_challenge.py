# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!

## Timed Challenge: First Repeated Value
# Return the first value that repeats in the collection.
# Input: [1, 4, 3, 5, 3, 2, 1]
# Output: 3

def first_repeated_value(values):
    seen = set()
    for v in values:
        if v in seen:
            return v
        seen.add(v)
    return None  # If no repeats found


# Quick tests
print(first_repeated_value([1, 4, 3, 5, 3, 2, 1]))  # Expected: 3
print(first_repeated_value([1, 2, 3, 4]))          # Expected: None
print(first_repeated_value([]))                    # Expected: None
print(first_repeated_value([7, 7]))                # Expected: 7

# Edge case tests
print(first_repeated_value([]))                 # Empty list → None
print(first_repeated_value([7]))                # Single value → None
print(first_repeated_value([7, 7]))             # Immediate repeat → 7
print(first_repeated_value([1, 2, 3, 4]))       # No repeats → None
print(first_repeated_value([1, 1, 2, 2]))       # First repeat is 1 → 1
print(first_repeated_value([5, 3, 5, 3]))       # First repeat is 5 → 5
print(first_repeated_value([0, -1, -1, 0]))     # Works with negative numbers → -1
print(first_repeated_value(["a", "b", "a"]))    # Works with strings → "a"
print(first_repeated_value([True, False, True]))# Works with booleans → True
