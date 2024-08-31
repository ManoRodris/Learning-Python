from administration import Admin
from users import User


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