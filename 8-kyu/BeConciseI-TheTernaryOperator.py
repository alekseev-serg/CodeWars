def describe_age(age):return"You're a(n) "+("kid"*(age<13)or"teenager"*(age<18)or"adult"*(age<65)or"elderly")


# def describe_age(a):
#     return f"You're a(n) {a<13 and 'kid' or a<18 and 'teenager' or a<65 and 'adult' or 'elderly'}"
#
# describe_age=lambda n:"You're a(n) "+"kid teenager adult elderly".split()[(n>12)+(n>17)+(n>64)]
#
# def describe_age(a):return f"You're a(n) {'kid'if a<=12 else'teenager'if a<=17 else'adult'if a<=64 else'elderly'}"