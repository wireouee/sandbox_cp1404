from programming_languages import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage('Ruby', "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python.__str__())
    language_fields = [ruby, python, visual_basic]
    print("The dynamically typed languages are:")
    for language in language_fields:
        if language.is_dynamic():
            print(language.field)


main()
