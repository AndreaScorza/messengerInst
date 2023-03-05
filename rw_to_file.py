class StringArrayFile:
    def __init__(self, filename):
        self.filename = filename
        self.string_array = []

        # Check if file exists, if not create a new file
        try:
            with open(self.filename, 'r') as f:
                self.string_array = f.read().splitlines()
        except FileNotFoundError:
            with open(self.filename, 'w') as f:
                pass

    def append(self, string):
        if not self.contains(string):
            self.string_array.append(string)

            # Write to file
            with open(self.filename, 'a') as f:
                f.write(string + "\n")
        else:
            print(f"{string} already exists in the file.")

    def read(self):
        # Read from file
        with open(self.filename, 'r') as f:
            self.string_array = f.read().splitlines()

        return self.string_array
    
    def contains(self, string):
        return string in self.string_array
    
    def is_unwanted(self, sender):
        try:
            with open("unwanted.txt", "r") as f:
                for line in f:
                    if sender in line:
                        return True
        except FileNotFoundError:
            pass
        return False


