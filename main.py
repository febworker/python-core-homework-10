from collections import UserDict
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Invalid command format"
    return wrapper
class Assistant:
    def __init__(self):
        self.contacts = {}
    @input_error
    def hello(self):
        return "How can I help you?"
    @input_error
    def add_contact(self, name, phone_number):
        self.contacts[name] = phone_number
        return f"Contact {name} added with phone number {phone_number}."
    @input_error
    def change_contact(self, name, new_phone_number):
        if name in self.contacts:
            self.contacts[name] = new_phone_number
            return f"Phone number for {name} updated: {new_phone_number}."
        else:
            raise KeyError
    @input_error
    def phone_contact(self, name):
        if name in self.contacts:
            return f"Phone number for {name}: {self.contacts[name]}."
        else:
            raise KeyError
    @input_error
    def show_all_contacts(self):
        if self.contacts:
            result = "All saved contacts:\n"
            for name, phone_number in self.contacts.items():
                result += f"{name}: {phone_number}\n"
            return result.strip()
        else:
            return "No contacts saved."
    def main(self):
        while True:
            user_input = input("Enter a command: ").lower()
            if user_input in ["good bye", "close", "exit"]:
                print("Good bye!")
                break
            elif user_input.startswith("hello"):
                print(self.hello())
            elif user_input.startswith("add"):
                try:
                    _, name, phone_number = user_input.split()
                    print(self.add_contact(name, phone_number))
                except ValueError:
                    print("Invalid command format. Usage: add [name] [phone_number]")
            elif user_input.startswith("change"):
                try:
                    _, name, new_phone_number = user_input.split()
                    print(self.change_contact(name, new_phone_number))
                except ValueError:
                    print("Invalid command format. Usage: change [name] [new_phone_number]")
            elif user_input.startswith("phone"):
                try:
                    _, name = user_input.split()
                    print(self.phone_contact(name))
                except ValueError:
                    print("Invalid command format. Usage: phone [name]")
            elif user_input == "show all":
                print(self.show_all_contacts())
            else:
                print("Unknown command. Please try again.")
if __name__ == "__main__":
    assistant = Assistant()
    assistant.main()
