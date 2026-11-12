
current_file = None
text = ""


# -------------------------
# Notepad Functions
# -------------------------

def new_file():
    global current_file, text

    text = ""
    current_file = None

    current_file = input("Enter filename for new document: ")
    print("New document created.")


def open_file():
    global current_file, text

    current_file = input("Enter filename to open: ")

    with open(current_file, "r") as file:
        text = file.read()

    print("File opened successfully.")
    print(text)


def save_file():
    if current_file is None:
        save_as()
        return

    with open(current_file, "w") as file:
        file.write(text)

    print("File saved successfully.")


def save_as():
    global current_file

    current_file = input("Enter filename: ")
    save_file()


def edit_text():
    global text

    print("Enter your text (type SAVE on a new line to finish):")

    lines = []

    while True:
        line = input()

        if line == "SAVE":
            break

        lines.append(line)

    text = "\n".join(lines)


# -------------------------
# REST API Integration
# -------------------------

def api_request():
    # REST API requests will be implemented here later.
    pass


def api_response():
    # REST API responses will be handled here later.
    pass


# -------------------------
# Main Application
# -------------------------

def main():
    while True:
        print("\n--- My Notepad ---")
        print("1. New")
        print("2. Open")
        print("3. Edit")
        print("4. Save")
        print("5. Save As")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            new_file()
        elif choice == "2":
            open_file()
        elif choice == "3":
            edit_text()
        elif choice == "4":
            save_file()
        elif choice == "5":
            save_as()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid selection.")


if __name__ == "__main__":
    main()
