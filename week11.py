# validators.py

class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter age: "))
    if age < 0 or age > 120:
        raise InvalidAgeError("Invalid age")
    print("Valid age")

except InvalidAgeError as e:
    print(e)

except ValueError:
    print("Enter numbers only")