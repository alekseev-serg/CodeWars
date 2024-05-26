def abbrev_name(name):
    return f"{name.split()[0][0].upper()}.{name.split()[1][0].upper()}"


# Другое решение
# def abbrev_name(name):
#     return '.'.join(item[0] for item in name.split()).upper()


print(abbrev_name("Sam Harris"))
