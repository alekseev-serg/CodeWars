def prepare_str(string):
    return string.replace(' ', '-').replace('!', '').replace('?', '').replace(',', '').replace('.', '').replace('/', '')


print(prepare_str('How good are you really?') + '.py')


def two_sort_more(lst):
    return '***'.join(min(lst))
