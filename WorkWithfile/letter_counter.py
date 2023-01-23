from string import ascii_lowercase as letters


class Counter:

    def __init__(self, file_path):
        self.path = file_path
        self.__letter_list = self.custom_letter_counter()

    def read_file(self, file_path: str) -> str:
        with open(file_path, "r") as my_file:
            result = my_file.read().lower()
        return result

    def custom_letter_counter(self) -> dict:
        """
        This function count the unique letters.
        letters in upper case are equal to letters in lower case.
        The spacing and special symbols will skip.
        """
        file_content = self.read_file(self.path).lower()
        return {letter: file_content.count(letter) for letter in file_content if letter in letters}

    @property
    def get_counted_letter(self):
        return self.__letter_list


if __name__ == "__main__":
    count_letter = Counter("text.txt")
    for key, value in count_letter.get_counted_letter.items():
        print(f"{key}: {value}", end="\n")

