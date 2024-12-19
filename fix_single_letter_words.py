path = "main.tex"
single_letter_words = "aAiIoOuUwWzZ"
new_file = []

replace_counter = 0
with open(path, "r") as file:
    for line in file.readlines():
        for word in single_letter_words:
            new_line = line.replace(f" {word} ", f" {word}~ ")

            if line == new_line:
                continue

            line = new_line
            replace_counter += 1

        new_file.append(line)


with open(path, "w") as file:
    file.writelines("")

    for line in new_file:
        file.write(line)

print(f"Replaced {replace_counter} single words!")
