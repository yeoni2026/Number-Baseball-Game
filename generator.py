import random

def generate_number():
    """Generate a random 3-digit number with unique digits."""
    digits = list(range(10))
    random.shuffle(digits)
    return digits[:3]

if __name__ == "__main__":
    print(generate_number())