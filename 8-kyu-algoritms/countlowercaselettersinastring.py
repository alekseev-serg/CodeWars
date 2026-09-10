"""
Your task is simply to count the total number of lowercase letters in a string.

Examples
"abc" ===> 3

"abcABC123" ===> 3

"abcABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~" ===> 3

"" ===> 0;

"ABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~" ===> 0

"abcdefghijklmnopqrstuvwxyz" ===> 26

"""

def count_lowercaseletters(s):
    i = 0
    for item in s:
        if item.islower():
            i+=1
    return i

print(count_lowercaseletters("abcdefghijklmnopqrstuvwxyz"))