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