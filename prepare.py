def prepare_str(string):
    return string.replace(' ', '').replace('!', '').replace('?', '').replace(',', '').replace('.', '').replace('/',
                                                                                                               '') + '.py'

while True:
    fileName = input('Enter file name: ')
    open('8-kyu/' + prepare_str(fileName), 'w').close()
