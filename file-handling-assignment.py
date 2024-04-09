def create_file():
    # Create a new text file named "my_file.txt" in write mode ('w')
    try:
        with open("my_file.txt", "w") as file:
            # Write at least three lines of text to the file
            file.write("This is line 1\n")
            file.write("12345\n")
            file.write("Another line here\n")
        print("File 'my_file.txt' created and initial content written successfully.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred while creating or writing to file: {e}")
    finally:
        print("File creation process completed.\n")


def read_file():
    # Read the contents of "my_file.txt" and display them on the console
    try:
        with open("my_file.txt", "r") as file:
            file_contents = file.read()
            print(f"Contents of 'my_file.txt':\n{file_contents}")
    except FileNotFoundError:
        print("File 'my_file.txt' not found.")
    except PermissionError:
        print("Permission denied to read the file.")
    except Exception as e:
        print(f"Error occurred while reading file: {e}")
    finally:
        print("File reading process completed.\n")


def append_to_file():
    # Append three additional lines of text to the existing content of "my_file.txt"
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appending line 1\n")
            file.write("98765\n")
            file.write("Another appending line here\n")
        print("Content appended to 'my_file.txt' successfully.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error occurred while appending to file: {e}")
    finally:
        print("File appending process completed.\n")


if __name__ == "__main__":
    # Perform file creation, reading, and appending
    create_file()
    read_file()
    append_to_file()
    read_file()  # Display updated content after appending
