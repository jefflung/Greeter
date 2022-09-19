class Greeter:
    name = ""
    filename = ""
    def __init__(self, name, filename): # The constructor
        self.name = name
        self.filename = filename
    def greet_to_screen(self):
        print("Hello,", self.name)
    def greet_to_file(self):
        with open(self.filename, mode="w") as my_file:
            my_file.write("Hello, " + self.name)

greeter = Greeter("Fred","hi.txt")
greeter.greet_to_screen()
greeter.greet_to_file()
