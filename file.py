file = open("myfile.txt","r")
print(file.read())

#new file
newFile =open("filename","w")
newFile.write("adding new contents to the file")

#2def read_file():
    # Ask the user for the filename
    filename = input("Please enter the filename: ")
    
    try:
        # Attempt to open and read the file
        with open(filename, "r") as file:
            content = file.read()
            print("\nFile content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_file()
