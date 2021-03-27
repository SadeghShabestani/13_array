import random

number = int(input("Enter Number Array: "))

list = []

while True:
    result = random.randint(0,number)

    if result not in list:
        list.append(result)

    if len(list) == number:
        print(f"My List: {list}")
        break