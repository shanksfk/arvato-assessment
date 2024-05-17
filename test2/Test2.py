"""
    FILL IN THE CODE

    such that isPalindrome(...) is a RECURSIVE function to determine if passed word is a palindrome.
    A palindrome is a word, phrase, or sequence that reads the same backward as forward,
    e.g., madam or nursesrun.

    @param word the word
    @return true if word is palindrome, false otherwise
"""


def is_palindrome(word: str) -> bool:
    if len(word) <= 1:
        return True

    if word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    else:
        return False


if __name__ == "__main__":
    # sample tests
    words = ["madam", "nursesrun", "lol", "kodok", "love", "peep", "peek"]
    for word in words:
        print(f"{word} is {is_palindrome(word)}")
