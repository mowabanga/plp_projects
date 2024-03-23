#Attempt to open file
try:
    # Write into file
    with open("my_file.txt", "w") as file:
        file.write("Hello, World!\n")
        file.write("1, 2, 3, 4\n")
        file.write("Today's date is 23/03/2024\n")
        
    # Read file and print file content on console
    with open("my_file.txt", "r") as file:
        content = file.read()
        print(content)
        
    # Append file
    with open("my_file.txt", "a") as file:
        file.write("This line has been appended to the file.\n")
        
except FileNotFoundError:
    # File does not exist
    print("Error: File not found.")
    
except PermissionError:
    # Permission denied for changing file
    print("Error: Permission denied!")
    
except Exception as e:
    # Handle any other unexpected errors
    print("An unexpected error occured!")
    
finally:
    # Perform other tasks upon success
    print("Finished modifying the file")