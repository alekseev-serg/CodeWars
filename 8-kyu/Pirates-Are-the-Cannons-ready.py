def cannons_ready(gunners):
    values = []
    for v in gunners.values():
        values.append(v)
    if 'nay' in values:
        return 'Shiver me timbers!'
    else:
        return 'Fire'


a = {'Mike': 'aye', 'Joe': 'aye', 'Johnson': 'aye', 'Peter': 'aye'}
b = {'Mike': 'aye', 'Joe': 'nay', 'Johnson': 'aye', 'Peter': 'aye'}
c = {'Joe': 'nay', 'Johnson': 'nay', 'Peter': 'aye'}
d = {'Mike': 'nay', 'Joe': 'nay', 'Johnson': 'nay', 'Peter': 'nay'}

print(cannons_ready(a))
print(cannons_ready(b))
print(cannons_ready(c))
print(cannons_ready(d))


def cannons_ready_more(gunners):
    return 'Fire!' if 'nay' not in gunners.values() else 'Shiver me timbers!'

