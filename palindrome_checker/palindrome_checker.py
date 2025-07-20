def remove_non_alphanumeric(text: str) -> str:
    """Remove non-alphanumeric characters from a string."""
    return ''.join(char.lower() for char in text if char.isalnum())


def is_palindrome(text: str) -> bool:
    """Check if a string is a palindrome."""
    left, right = 0, len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True


def main():
    """Main function to run the palindrome checker."""
    print("Welcome to the Palindrome Checker")
    text = input("Enter a string to check if it's a palindrome: ")
    text = remove_non_alphanumeric(text)
    if is_palindrome(text):
        print(f"{text} is a palindrome.")
    else:
        print(f"{text} is not a palindrome.")


if __name__ == "__main__":
    main()