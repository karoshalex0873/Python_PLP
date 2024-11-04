# file_handling_assignment.py

# File Creation and Writing
try:
    # Step 1: Create and write to the file
    with open("my_file.txt", "w") as file:
        file.write("Line 1: Hello, World!\n")
        file.write("Line 2: 42 is the answer to life.\n")
        file.write("Line 3: Python is fun!\n")
    print("File created and initial content written successfully.")

    # Step 2: Reading and Displaying File Content
    with open("my_file.txt", "r") as file:
        print("\nInitial Content of 'my_file.txt':")
        print(file.read())

    # Step 3: Appending Additional Lines to the File
    with open("my_file.txt", "a") as file:
        file.write("Line 4: Adding more content.\n")
        file.write("Line 5: Another line with number 2023.\n")
        file.write("Line 6: File handling in Python.\n")
    print("\nAdditional content appended successfully.")

    # Step 4: Reading and Displaying Updated File Content
    with open("my_file.txt", "r") as file:
        print("\nUpdated Content of 'my_file.txt':")
        print(file.read())

except FileNotFoundError:
    print("Error: The file was not found.")

except PermissionError:
    print("Error: You do not have permission to write to this file.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    print("\nFile handling operation completed.")
