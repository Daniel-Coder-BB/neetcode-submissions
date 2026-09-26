from typing import List

def read_integers() -> List[int]:
    number_list = []
    split_string = input().split(",")
    for number in split_string:
        number_list.append(int(number))
    return number_list    


# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
