import sqlite3


def get_user(username):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    # Vulnerability: SQL injection
    query = "SELECT * FROM users WHERE username = '" + username + "'"

    cursor.execute(query)
    result = cursor.fetchone()

    connection.close()
    return result


def calculate_discount(price, discount):
    # Bug: no validation of discount range
    return price - (price * discount / 100)


def process_user(user):
    # Bug: assumes email always exists
    print("Processing:", user["email"])

    return True


def main():
    username = input("Enter username: ")
    print(get_user(username))

    print(calculate_discount(100, 150))

    process_user({"name": "Test User"})


if __name__ == "__main__":
    main()