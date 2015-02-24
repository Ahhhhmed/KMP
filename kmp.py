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
        self.__failList.append({self.__pattern[0]: 1, 'lb': -1})

        for i in range(1, len(self.__pattern)):
            #Finding Longest Block (LB), starting from the LB of the last current character
            j = i - 1

            while True:
                #LB is length 0 (does not exist), returning to the beginning of the pattern
                if j == 0:
                    self.__failList.append({'lb': 0, self.__pattern[i]: i+1})
                    break

                #LB for some character can be extended by 1 and that makes LB for the current character
                if self.__pattern[self.__failList[j]['lb']] == self.__pattern[i-1]:
                    failState = self.__failList[j]['lb'] + 1
                    self.__failList.append({'lb':failState, self.__pattern[i]: i+1})
                    break

                #LB of LB, next possible LB to be extended
                j = self.__failList[j]['lb']

        self.__isCompiled = True
        assert len(self.__failList) == len(self.__pattern)

    def __nextState(self,state,letter):
        assert self.__isCompiled
        assert len(letter) == 1

        if letter in self.__failList[state]:
            return self.__failList[state][letter]

        if state == 0:
            return 0

        failState = self.__nextState(self.__failList[state]['lb'],letter)
        if failState != 0: self.__failList[state][letter] = failState
        return failState

    def Search(self, text):
        if type(text) is not str:
            raise TypeError("Type must be string")

        #If text is shorter then pattern, match can not exist
        if len(text) < len(self.__pattern):
            return None

        if not self.__isCompiled:
            self.__compile()

        #current index in text
        index = 0
        #current state of the machine
        state = 0

        while index < len(text):
            #Reading next character
            state = self.__nextState(state,text[index])
            if state == len(self.__pattern):
                return index - state
            index += 1
        return None


def Search(pattern, text):
    return KmpMachine(pattern).Search(text)