import re


class TexFixer:
    def __init__(self, path):
        self.path = path
        self.__single_letter_words = "aAiIoOuUwWzZ"
        self.__fixed_file = []
        self.__single_letter_counter = 0
        self.__quotes_counter = 0

    def fix_all(self):
        inside_listing = False
        with open(self.path, "r") as file:
            for line in file:
                if re.search(r'\\begin{listing}', line):
                    inside_listing = True

                if re.search(r'\\end{listing}', line):
                    inside_listing = False

                if not inside_listing:
                    line = self.__fix_single_letter_words(line)
                    line = self.__replace_quotes(line)
                self.__fixed_file.append(line)

        self.__write_file()

        print(f"Fixed {self.__single_letter_counter} single words!")
        print(f"Fixed {self.__quotes_counter} quotes!")

    def __write_file(self):
        with open(self.path, "w") as file:
            file.writelines("")
            for line in self.__fixed_file:
                file.write(line)

    def __replace_quotes(self, line: str):
        pattern = r'"(.*?)"'
        result = re.sub(pattern, r"``\1''", line)
        if result != line: self.__quotes_counter += 1
        return result

    def __fix_single_letter_words(self, line: str):
        result = line
        for word in self.__single_letter_words:
            prev_result = result
            result = result.replace(f" {word} ", f" {word}~")

            if prev_result != result: self.__single_letter_counter += 1
        return result

path = "main.tex"
texFixer = TexFixer(path)
texFixer.fix_all()
