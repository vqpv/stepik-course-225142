from string import punctuation


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_magic_word(message):
    lst = message.split()
    for i in lst:
        word = i.strip(punctuation)
        if is_prime(len(word)):
            print(word)
            return
    print(None)
