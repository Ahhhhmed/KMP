__author__ = 'Nenad Vasic'


class KmpMachine:
    def __init__(self, pattern):
        if type(pattern) is not str:
            raise TypeError("Type must be string")
        if pattern == '':
            raise ValueError("Empty string not allowed")
        self.__pattern = pattern
        self.__isCompiled = False
        self.__failList = []

    def __compile(self):
        if self.__isCompiled:
            return None
        assert (self.__failList == [])

        #first two elements have fixed values
        self.__failList.append(-1)
        if (len(self.__pattern) > 1):
            self.__failList.append(0)

        for i in range(2, len(self.__pattern)):
            #Finding Longest Block (LB), starting from the LB of the last current character
            j = i - 1

            while True:
                #LB is length 0 (does not exist), returning to the beginning of the pattern
                if j == 0:
                    self.__failList.append(0)
                    break

                #LB for some character can be extended by 1 and that makes LB for the current character
                if self.__pattern[self.__failList[j]] == self.__pattern[i-1]:
                    self.__failList.append(self.__failList[j] + 1)
                    break

                #LB of LB, next possible LB to be extended
                j = self.__failList[j]

        self.__isCompiled = True
        assert len(self.__failList) == len(self.__pattern)

    def Search(self, text):
        if not self.__isCompiled:
            self.__compile()

        #current index in text
        index = 0
        #current state of the machine
        state = 0

        while index < len(text):
            #read 1 character to get to state 0
            if state == -1:
                state = 0
                index += 1
            #Extending partial match
            elif text[index] == self.__pattern[state]:
                state += 1
                index += 1
                if state == len(self.__pattern):
                    return index
            #Falling back according to the __failList
            else:
                state = self.__failList[state]  # if match == 0 is should be 0, not -1
        return None


def Search(pattern, text):
    return KmpMachine(pattern).Search(text)