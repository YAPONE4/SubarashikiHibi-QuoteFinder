import re
import os

def find_quote(quote, file):
    lines = file.readlines()
    for i in lines:
        str = i.lower()
        if re.search(quote, str) != None:
            print('Your quote has been found in file named: {}\n'.format(file.name))

def main():
    print('Please, enter quote you want to find: ')
    str = input().lower()
    str = re.sub('я', 'z', str)
    print(str)
    files = os.listdir('Script')
    for i in files:
        file = open('Script/{}'.format(i), mode = 'r', encoding = 'ANSI')
        find_quote(str, file)

if __name__ == '__main__':
    main()