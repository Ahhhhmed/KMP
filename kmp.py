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
        self.__failList.append({self.__pattern[0]: 1, 'other': -1})
        if (len(self.__pattern) > 1):
            self.__failList.append(dict(self.__failList[0]))
            self.__failList[-1]['other'] = 0
            self.__failList[-1][self.__pattern[1]] = 2

        for i in range(2, len(self.__pattern)):
            #Finding Longest Block (LB), starting from the LB of the last current character
            j = i - 1

            while True:
                #LB is length 0 (does not exist), returning to the beginning of the pattern
                if j == 0:
                    self.__failList.append(dict(self.__failList[0]))
                    self.__failList[-1]['other'] = 0
                    self.__failList[-1][self.__pattern[i]] = i+1
                    break

                #LB for some character can be extended by 1 and that makes LB for the current character
                if self.__pattern[self.__failList[j]['other']] == self.__pattern[i-1]:
                    failState = self.__failList[j]['other'] + 1
                    self.__failList.append(dict(self.__failList[failState]))
                    self.__failList[-1]['other'] = failState
                    self.__failList[-1][self.__pattern[i]] = i+1
                    break

                #LB of LB, next possible LB to be extended
                j = self.__failList[j]['other']

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
            elif text[index] in self.__failList[state]:
                state = self.__failList[state][text[index]]
                index += 1
                if state == len(self.__pattern):
                    return index
            #Falling back according to the __failList
            else:
                state =  -1
        return None


def Search(pattern, text):
    return KmpMachine(pattern).Search(text)