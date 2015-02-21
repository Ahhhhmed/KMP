__author__ = 'Nenad Vasic'
import kmp
import random

def randomWord():
    return ''.join(random.choice("abcd") for _ in range(random.randint(4,100)))
def randomSubstring(s):
    start = random.randint(0,len(s) - 2)
    end = random.randint(start + 1,len(s))
    return s[start:end]


def test():
    try:
        k = kmp.KmpMachine('')
        raise AssertionError
    except ValueError:
        pass

    try:
        k = kmp.KmpMachine(123)
        raise AssertionError
    except TypeError:
        pass

    k = kmp.KmpMachine('aab')
    assert k.Search('caaabbbac') != None

    for i in range(1000):
        s = randomWord()
        m = kmp.KmpMachine(randomSubstring(s))
        assert m.Search(s) != None


test()