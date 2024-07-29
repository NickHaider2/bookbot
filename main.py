def main():
    """
        This file parses a book represented in a text file, and generates a report of the number of words, 
        and number of each character found within.
    """

    book_path = "books/frankenstein.txt"
    book_content = get_book_content(book_path)
    count_of_chars = sortDictionary(count_characters(book_content))

    print(f"--- Begin report of {book_path} ---")
    generate_report(book_content, count_of_chars)
    print("\n--- End report ---")

    return 0


def get_book_content(book_path: str) -> str:
    """
        Returns a list of words found within a .txt file
        params:
            book_path: Type str, relative directory path to where the .txt file is located.
        returns:
            book_content: Type str, text found within the parsed .txt file at book_path
    """
    with open(book_path) as f:
        book_content = f.read()
    return book_content


def count_words(input_text: str) -> int:
    """
        Returns the number of words found in a string. Converts an input string into a list of 
        separate words with the .split() method and returns the number of words in that list.
        params:
            input_text: Type str, text.
        returns:
            Int type, Number of words found in input_text.
    """
    return len(input_text.split())


def count_characters(input_text: str) -> dict:
    """
        Returns a dictionary with the count of each alphabetic character found in an input string. 
        Not case-sensitive - i.e. 'A' and 'a' characters would be counted as the same key in the dictonary.
        params:
            input_text: Type str, text.
        returns:
            count_of_characters: Type dict, keys (type str); being the alphabetic characters found in input_text (lower case),
                                                  values (type int);being the number of times the key is found in input_text.
    """
    count_of_characters = {}
    for char in input_text:
        lower_char = char.lower()
        if lower_char in count_of_characters:
            count_of_characters[lower_char] += 1
        elif lower_char.isalpha():
            count_of_characters[lower_char] = 1
    return count_of_characters 


def sortDictionary(input_dictionary: dict) -> dict:
    """
        Returns a dictionary that is sorted by its values, in descending order. 
        params:
            input_dictionary: Type dict, {key (type str): value (type int)}
        returns:
            sorted_dict: Type dict, {key (type str): value (type int)}
    """
    sorted_dict = dict(sorted(input_dictionary.items(), key=lambda x:x[1],reverse = True))
    return sorted_dict


def generate_report(book_content: str, count_of_chars: dict) -> None:
    """
        Generates a report of a given text's contents, namely the number of words it contains 
        and the number of each alphabetic letter. 
        params:
            book_content: Type str, text found within the parsed .txt file at book_path
            count_of_chars: Type dict, {key (type str): value (type int)}
        
    """
    print(f"{count_words(book_content)} words found in the document")
    print("\n")
    for char in count_of_chars:
            print(f"The {char} character was found {count_of_chars[char]} times")
    return 0


if __name__ == '__main__':
    main()