# Description: Write a function that concatenates the nth letter from each word to construct a new word.
def concatenate_nth_letters(words: list[str]) -> str:
    """
    Concatenates the nth letter from each word to construct a new word.

    :param words: List of words.
    :return: New word constructed by concatenating the nth letter from each word.
    """
    new_word = ""

    # Iterate over the words and concatenate the nth letter from each word.
    for i, word in enumerate(words):
        if i < len(word):
            new_word += word[i]
    return new_word

# Example usage of the function.
def main():
    words = ["yoda", "best", "has"]
    result = concatenate_nth_letters(words)
    print(result)  # Output: "yes"

if __name__ == "__main__":
    main() 