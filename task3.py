def concatenate_nth_letters(words: list[str]) -> str:
    """
    Concatenates the nth letter from each word to construct a new word.

    :param words: List of words.
    :return: New word constructed by concatenating the nth letter from each word.
    """
    new_word = ""
    for i, word in enumerate(words):
        if i < len(word):
            new_word += word[i]
    return new_word
def main():
    words = ["yoda", "best", "has"]
    result = concatenate_nth_letters(words)
    print(result)  # Output: "abce"

if __name__ == "__main__":
    main() 