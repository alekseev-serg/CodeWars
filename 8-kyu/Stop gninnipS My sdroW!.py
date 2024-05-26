sentence = 'of more dessap secapS name or in the only but five or a words a'


def spin_words(sentence):
    test_list = sentence.split()
    new_list = []
    for item in test_list:
        if len(item) > 4:
            new_list.append(item[::-1])
        else:
            new_list.append(item)
    words = " ".join(new_list)
    return words


print(spin_words(sentence))
