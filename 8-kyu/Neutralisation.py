# "--++--", "++--++"
# 000000
# ("-+-+-+", "-+-+-+"), "-+-+-+")
def neutralise(s1, s2):
    if s1 == s2:
        return s1
    else:
        string = ''
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                string += s1[i]
            else:
                string += '0'
        return string


print(neutralise("+++--+---", "++----++-"))


def neutralise_more(s1, s2):
    return ''.join('0' if i != j else i for i, j in zip(s1, s2))
