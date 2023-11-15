s = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]

for item in s:
    if item.lower() == "needle":
        print(s.index(item))