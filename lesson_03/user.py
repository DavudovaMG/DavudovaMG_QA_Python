# Создание класса
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def printfirst_name(self):
        print(self.first_name)

    def printlast_name(self):
        print(self.last_name)

    def printFullname(self):
        print(self.first_name, self.last_name)


# alex = User("Alex", "Melnikov")
# alex.printfirst_name()
# alex.printlast_name()
# alex.printFullname()
