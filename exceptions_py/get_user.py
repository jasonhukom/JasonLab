def main():
    print("Gets User Information Program")
    user_name = name("Name: ")
    user_phone = phone_num("Phone Number: ")
    user_email = email("Email Address: ")
    print(f''' 
Name: {user_name}
Phone Number: {user_phone}
Email Address: {user_email}   
    ''')

def name(prompt):
    while True:
        try:
            return str(input(f"\r{prompt}"))
        except ValueError:
            pass

def phone_num(prompt):
    while True:
        try:
            return int(input(f"\r{prompt}"))
        except ValueError:
            pass

def email(prompt):
    while True:
        email = input(f"\rprompt")
        email_type_list = []
        for i in range(len(email) - 1):
            email_type_list.append(email[i])
        if '@' and '.' not in email_type_list:
            pass
        else:
            return email


main()