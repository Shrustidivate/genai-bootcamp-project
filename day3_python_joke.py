# day3_python_joke.py

import random

jokes = [
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the math book look sad? Because it had too many problems."
]

def tell_joke():
    print(random.choice(jokes))

if __name__ == "__main__":
    tell_joke()
