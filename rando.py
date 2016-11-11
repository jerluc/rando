def get_random_number():
    # /dev/random is a special file on Mac and Linux that contains an
    # infinite amount of random characters
    with open('/dev/random') as r:
        # my_file.read(N) will read N characters from the file; here we
        # only want to read one character
        character = r.read(1)
        # the ord(c) function converts a single character to an integer
        as_int = ord(character)
        return as_int


def main():
    num = get_random_number()
    while True:
        guess = int(raw_input('What number am I thinking of? '))
        if guess == num:
            print('You got it!')
            break
        elif guess < num:
            print('Too low!')
        else:
            print('Too high!')

if __name__ == '__main__':
    main()
