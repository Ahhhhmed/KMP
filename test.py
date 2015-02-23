__author__ = 'Nenad Vasic'
import kmp
import random
import time

def randomWord():
    return ''.join(random.choice("abcd") for _ in range(random.randint(4,100)))
def randomSubstring(s):
    start = random.randint(0,len(s) - 2)
    end = random.randint(start + 1,len(s))
    return s[start:end]

message = 'No message'

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

    k = kmp.KmpMachine('aabd')
    r = k.Search('caaabbbac')
    assert r == None

    r = kmp.Search('aabbbssaaabsseqw','aabbbssaaabssewrrea')
    assert r == None

    for i in range(10000):
        s = randomWord()
        sub = randomSubstring(s)
        m = kmp.KmpMachine(sub)
        message = 'Pattern: ' + sub + '\nText: ' + s
        assert m.Search(s) != None

start = time.time()

try:
    test()
except AssertionError:
    print(message)

end = time.time()
runtime = end-start
print('Runtime: ' + runtime.__repr__() + ' sec')