import json


def load_users():
    """
    Loads user data from the JSON file.
    Returns a list of users or None if loading fails.
    """
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error:'users.json' not found")
    except json.JSONDecodeError:
        print("Error: JSON is invalid or corrupt")
    return None


def filter_users_by_name(name):
    """
    Filters users by name and prints matches.
    """
    users = load_users()
    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    if filtered_users:
        for user in filtered_users:
            print(user)
    else:
        print("No users found with the name: {name}")


def filter_users_by_age(age):
    """
    Filters users by age and prints matches.
    """
    users = load_users()
    filtered_users = [user for user in users if user["age"] == age]

    if filtered_users:
        for user in filtered_users:
            print(user)
    else:
        print("No users found with the age: {age}")


def filter_users_by_email(email):
    """
    Filters users by email and prints matches.
    """
    users = load_users()
    filtered_users = [user for user in users if user["email"] == email]

    if filtered_users:
        for user in filtered_users:
            print(user)
    else:
        print("No users found with the email: {email}")


if __name__ == "__main__":
    while True:
        filter_option = input("What would you like to filter by? (By name, by age or by email?). Enter 'exit' to quit: ").strip().lower()
    
        if filter_option == "name":
            name_to_search = input("Enter a name to filter users: ").strip()
            filter_users_by_name(name_to_search)
        elif filter_option == "age":
            try:
                age_to_search = int(input("Enter an age to filter users: ").strip())
                filter_users_by_age(age_to_search)
            except ValueError:
                print("Error: age must be a number.")
        elif filter_option == "email":
            email_to_search = input("Enter an email to filter users: ").strip()
            filter_users_by_email(email_to_search)
        elif filter_option == "exit":
            print("Exit the program")
            break
        else:
            print("Error: Please enter 'name', 'age' or 'email'; enter 'exit' to quit")

