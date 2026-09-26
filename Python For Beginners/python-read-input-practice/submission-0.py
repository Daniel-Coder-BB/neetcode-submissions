def add_two_numbers() -> int:
    numbers_list = input().split(",")
    sum = 0
    for number in numbers_list:
        sum += int(number)
    return sum    



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
