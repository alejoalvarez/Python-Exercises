# This is a basic example for validate if a word or sentence is palindrome


def run():
    word = str(input("Enter the word: ")).lower().replace(' ', '')
    if word[::] == word[::-1]:
        print('Is palindrome')
    else:
        print('It is no palindrome')


if __name__ == '__main__':
   run()
