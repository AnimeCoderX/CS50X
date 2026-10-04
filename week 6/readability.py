import re
import math


def count_letters(text):
    """Count the number of letters in the text."""
    return sum(1 for char in text if char.isalpha())


def count_words(text):
    """Count the number of words in the text."""
    return len(text.split())


def count_sentences(text):
    """Count the number of sentences in the text."""
    return sum(1 for char in text if char in ['.', '!', '?'])


def compute_index(letters, words, sentences):
    """Compute the Coleman-Liau index."""
    L = (letters / words) * 100
    S = (sentences / words) * 100
    return round(0.0588 * L - 0.296 * S - 15.8)


def main():
    # Prompt the user for a string of text
    text = input("Text: ")

    # Count letters, words, and sentences
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    # Compute the Coleman-Liau index
    index = compute_index(letters, words, sentences)

    # Determine the reading grade level
    if index >= 16:
        print("Grade 16+")
    elif index < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {index}")


if __name__ == "__main__":
    main()
