class User:

    def __init__(self, first_name, last_name, gender, age):
        self.fn = first_name
        self.ln = last_name
        self.g = gender
        self.a = age
        self.login_attempts = 0

    def describe_user(self):
        print("------ User's data ------")
        print(f"Name: {self.fn} {self.ln}")
        print(f"Gender: {self.g}")
        print(f"Age: {int(self.a)}")

    def greet_user(self):
        print(f"Hello {self.fn}, we're very excited to have you here in our company,"
              f" people with {int(self.a)} years old use to like our workplace")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        for priv in self.privileges:
            print(priv)

class Admin(User):
    def __init__(self, first_name, last_name, gender, age):
        super().__init__(first_name, last_name, gender, age)
        self.privileges = Privileges()

user_1 = User("Rodrigo", "Felix", "Male", 22)
user_2 = User("Gabrielle", "Rosa", "Female", 23)

# user_2.describe_user()
# user_2.greet_user()

# print(user_1.login_attempts)
# user_1.increment_login_attempts()
# user_1.increment_login_attempts()
# user_1.increment_login_attempts()
# user_1.increment_login_attempts()
# user_1.increment_login_attempts()
# user_1.increment_login_attempts()
# user_1.increment_login_attempts()
# user_1.increment_login_attempts()
# user_1.increment_login_attempts()
# user_1.increment_login_attempts()
# user_1.increment_login_attempts()
# print(user_1.login_attempts)
# user_1.reset_login_attempts()
# print(user_1.login_attempts)

# manager = Admin("Icaro", "Felix", "Male", 24)
# manager.show_privileges()

manager = Admin("Icaro", "Felix", "Male", 24)
manager.privileges.show_privileges()