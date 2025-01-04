class Dictionary:
    def __init__(self):
        self.entries = {}
    def new_entry(self) -> None:
        """
        Prompts the user to enter a name and description, then adds the entry to the dictionary.
        """
        name = input("Enter name: ")
        description = input("Enter description: ")
        self.entries[name] = description
    def print_dict(self) -> None:
        """
        Prints the keys and values of the entries dictionary.
        """
        for key, value in self.entries.items():
            print(f"{key}: {value}")
    def look(self, name: str) -> str:
        """
        Returns the description of the entry with the given name.
        """
        return self.entries.get(name, "Entry not found.")
    def main(self) -> None:
        """
        Calls the new_entry method and prints the resulting dictionary.
        """
        while True:
            self.new_entry()
            if input("Do you want to add another entry? (y/n): ") != "y":
                break
        name = input("Enter name to find: ")
        print(self.look(name))
if __name__ == "__main__":
    manager = Dictionary()
    manager.main()