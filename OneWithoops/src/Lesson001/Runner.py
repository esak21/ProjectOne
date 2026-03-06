class Person:

    def __init__(self, name:str , age: int ):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(Name: {self.name}, Age: {self.age})"

    def greet(self):
        return f"Hello My name is {self.name} and I am {self.age} years old"



class User:

    def __init__(self, username: str, email: str, password: str, phone_number: int ):
        self.username = username
        self._email = email
        self.password = password
        self.__phone_number = phone_number

    def __str__(self):
        return f"User(username: {self.username}, email: {self._email})"

    def say_hi_to_user(self, user: 'User'):
        print(f"Sending Message to {user.username} :: Hi {user.username} - How are you from {self.username}")

    def clean_email(self):
        return self._email.lower().strip()

    def get_email(self):
        return self._email

    def set_email(self, email):
        if '@' in email:
            self._email = email


class ModernUser:

    def __init__(self, username: str, email: str, password: str, phone_number: int ):
        self.username = username
        self._email = email
        self.password = password
        self.__phone_number = phone_number

    def __str__(self):
        return f"User(username: {self.username}, email: {self._email})"

    def say_hi_to_user(self, user: 'User'):
        print(f"Sending Message to {user.username} :: Hi {user.username} - How are you from {self.username}")

    def clean_email(self):
        return self._email.lower().strip()

# we make the attribute read only / private
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if '@' in email:
            self._email = email

    @property
    def phone_number(self):
        return self.__phone_number

if __name__ == "__main__":
    admin_user = User("John", "jOhn@example.com", "password")
    print(admin_user)

    dev_user = User("Dev","dev@example.com", "password")

    admin_user.say_hi_to_user(dev_user)


    print(admin_user.clean_email())

    print(admin_user.__phone_number)
