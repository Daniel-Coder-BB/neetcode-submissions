from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    frequency_counter = {}
    for char in word:
        if char in frequency_counter:
            frequency_counter[char] += 1
        else:
            frequency_counter[char] = 1    
    return frequency_counter        




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
