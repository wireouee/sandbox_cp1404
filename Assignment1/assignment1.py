"""
Name: Deqian He
Date started: 15/04/2022
GitHub URL: https://github.com/wireouee/sandbox_cp1404
"""
menu = "Menu:\n" \
       "L - List all books\n" \
       "A - Add new book\n" \
       "M - Mark a book as completed\n" \
       "Q - Quit"
file_name = "books.csv"


def main():
    """Reading Tracker"""
    book_data, total_book_num = get_data()
    preamble(total_book_num)
    # Select loop and loop checking
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            page, book = display_all_book(book_data)
            print("You need to read {} pages in {} books.".format(page, len(book)))
        elif choice == "A":
            book_data, total_book_num = add_new_book(book_data, total_book_num)
        elif choice == "M":
            book_data = completion_mark(book_data, total_book_num)
        else:
            print("Invalid menu choice")
        print(menu)
        choice = input(">>> ").upper()
    else:
        quit_function(book_data)


def preamble(total_book_num):
    """Display preamble including designer, total book and menu"""
    print("Reading Tracker 1.0 - by Deqian He")
    print("{} books loaded".format(total_book_num))
    print(menu)


def get_data():
    """book's data recorder"""
    total_book_num = 0
    book_file = open(file_name, "r")
    book_list = []
    for line in book_file:
        line = line.strip()
        parts = line.split(',')  # Separate data to list
        parts[2] = int(parts[2])  # Make the number an integer
        book_list.append(parts)
        total_book_num += 1
    book_file.close()
    return book_list, total_book_num


def display_all_book(book_data):
    """Display books information and status"""
    status = None
    unread_page = 0
    read_book = []
    # List books
    for index, value in enumerate(book_data, 1):
        if value[3] == "c":
            status = " "
        elif value[3] == "r":
            status = "*"
            unread_page += value[2]
            read_book.append(index)  # Record books number which have read
        print("{}{}. {:<39} by {:<18} {:>4} pages".format(status, index, *value))
    return unread_page, read_book


def add_new_book(book_data, total_book_num):
    """register information about new book"""
    add_new_list = []
    # Title loop checking
    book_title = input("Title: ")
    while book_title == "" or book_title == " ":
        print("Input can not be blank")
        book_title = input("Title: ")
    add_new_list.append(book_title)
    # Author loop checking
    book_author = input("Author: ")
    while book_author == "" or book_author == " ":
        print("Input can not be blank")
        book_author = input("Author: ")
    add_new_list.append(book_author)
    # page loop checking
    while True:
        book_page = input("Pages: ")
        try:
            book_page = int(book_page)
            if book_page > 0:
                add_new_list.append(book_page)
                break
            elif book_page <= 0:
                print("Number must be > 0")
        except ValueError:
            print("Invalid input; enter a valid number")

    print("{} by {}, ({} pages) added to Reading Tracker".format(*add_new_list))
    add_new_list.append("r")
    book_data.append(add_new_list)
    total_book_num += 1
    return book_data, total_book_num


def completion_mark(book_data, total_book_num):
    """Mark book which has read"""
    book_serial_num = 1
    page, books_read = display_all_book(book_data)   # display book information
    if total_book_num - len(books_read) == total_book_num:  # Repeat marking and quit this function
        print("No required books")
    else:
        # Mark loop checking
        while True:
            book_mark = input(">>> ")
            try:
                book_mark = int(book_mark)
                if total_book_num >= book_mark > 0:
                    break
                elif book_mark <= 0:
                    print("Number must be > 0")
                elif book_mark > total_book_num:
                    print("Invalid book number")
            except ValueError:
                print("Invalid input; enter a valid number")
        book_mark = int(book_mark)
        if book_mark in books_read:
            print("{} by {} completed!".format(*book_data[book_mark - 1]))
            # Register complete information
            for part in book_data:
                if book_serial_num == book_mark:
                    part[3] = "c"
                book_serial_num += 1
        else:
            print("That book is already completed")
        return book_data


def quit_function(book_data):
    """stop program and print book information"""
    print("{} books saved to {}".format(len(book_data), file_name))
    book_file = open(file_name, "w")
    for line in book_data:
        line[2] = str(line[2])
        print(",".join(line), file=book_file)
    book_file.close()
    print("So many books, so little time. Frank Zappa")


if __name__ == '__main__':
    main()
