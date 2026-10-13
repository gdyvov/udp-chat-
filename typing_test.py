"""Typing Test System.

Tests how quickly and accurately a user can type a randomly generated
sequence of characters.
"""

import random
import string
import time

MIN_CHARS = 5
MAX_CHARS = 15
CHARACTER_POOL = string.ascii_letters + string.digits


def get_name(prompt):
    """Ask for a name until a non-blank value made of letters is entered."""
    while True:
        name = input(prompt).strip()
        # Allow spaces, hyphens and apostrophes, e.g. "Mary-Jane" or "O'Neil".
        if name and name.replace(" ", "").replace("-", "").replace("'", "").isalpha():
            return name
        print("Invalid name. Please use letters only (spaces, - and ' allowed).")


def get_character_count():
    """Ask for the number of characters until a whole number in range is entered."""
    while True:
        entry = input(f"Number of characters to generate ({MIN_CHARS}-{MAX_CHARS}): ").strip()
        if not entry.isdigit():
            print("Invalid entry. Please enter a whole number.")
            continue
        count = int(entry)
        if MIN_CHARS <= count <= MAX_CHARS:
            return count
        print(f"Invalid entry. The number must be between {MIN_CHARS} and {MAX_CHARS}.")


def generate_characters(count):
    """Return a random string of `count` letters and digits."""
    return "".join(random.choice(CHARACTER_POOL) for _ in range(count))


def count_correct(generated, entered):
    """Count characters typed correctly in the same position as generated."""
    return sum(1 for g, e in zip(generated, entered) if g == e)


def calculate_accuracy(correct, total):
    """Accuracy % = (correct / total) * 100, rounded to 2 decimal places."""
    if total == 0:
        return 0.0
    return round(correct / total * 100, 2)


def run_test():
    print("=" * 40)
    print("         TYPING TEST SYSTEM")
    print("=" * 40)

    first_name = get_name("First Name: ")
    last_name = get_name("Last Name: ")
    count = get_character_count()

    generated = generate_characters(count)

    print("\nType the following characters exactly as shown:")
    print(f"\n    {generated}\n")
    input("Press Enter when you are ready to begin...")

    start_time = time.perf_counter()
    entered = input("Start typing: ")
    end_time = time.perf_counter()

    time_taken = end_time - start_time
    correct = count_correct(generated, entered)
    accuracy = calculate_accuracy(correct, len(generated))

    print("\n" + "=" * 40)
    print("              RESULTS")
    print("=" * 40)
    print(f"Name:                {first_name} {last_name}")
    print(f"Generated:           {generated}")
    print(f"Entered:             {entered}")
    print(f"Time taken:          {time_taken:.2f} seconds")
    print(f"Correct characters:  {correct} / {len(generated)}")
    print(f"Accuracy:            {accuracy:.2f}%")
    print("=" * 40)


if __name__ == "__main__":
    run_test()
