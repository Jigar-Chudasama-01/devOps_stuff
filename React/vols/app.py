import os

def main():
    # Step 1: Ask if user wants to enter a name
    enter = input("Do you want to enter a name? (y/n): ").strip().lower()
    if enter == 'y':
        name = input("Enter name: ")
        with open("name.txt", "a") as file:
            file.write(name + "\n")
        print("Name added.")
    elif enter != 'n':
        print("Invalid input for name entry.")

    # Step 2: Ask if user wants to display names
    show = input("Do you want to display names? (y/n): ").strip().lower()
    if show == 'y':
        if os.path.exists("name.txt"):
            with open("name.txt", "r") as file:
                content = file.read().strip()
                if content:
                    print("Names in name.txt:")
                    print(content)
                else:
                    print("name.txt is empty.")
        else:
            print("name.txt does not exist.")
    elif show != 'n':
        print("Invalid input for display choice.")

if __name__ == "__main__":
    main()

# list = [i*2 for i in range(2,10)]
# print(list)