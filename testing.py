import random
import string
class Account:
    def password(length):
       password = ""

       for i in range(length):
        password += random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)

       return password


    def load_names(Names):
     with open(Names, 'r') as file:
        names = file.read().splitlines()
     return names

    def loginN(names):
       return random.choice(names)

    def load_surnames(Surname):
      with open(Surname, 'r') as file:
        surnames = file.read().splitlines()
      return surnames

    def loginS(surnames):
      return random.choice(surnames)

for i in range(3):
    names = Account.load_names('Names.txt')
    random_name = Account.loginN(names)

    surnames = Account.load_names('Surname.txt')
    random_surname = Account.loginS(surnames)
    print(f"Login: {random_name} {random_surname.lower()}")
    print(f"Password: {Account.password(16)}")
    print()

