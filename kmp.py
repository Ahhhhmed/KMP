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

    def Compile(self):
        if self.__isCompiled:
            return None
        assert (self.__failList == [])

        self.__failList.append(-1)
        if (len(self.__pattern) > 1):
            self.__failList.append(0)

        for i in range(2, len(self.__pattern)):
            j = i - 1

            while True:
                if j == 0:
                    self.__failList.append(0)
                    break

                if self.__pattern[self.__failList[j]] == self.__pattern[i-1]:
                    self.__failList.append(self.__failList[j] + 1)
                    break

                j = self.__failList[j]

        self.__isCompiled = True
        assert len(self.__failList) == len(self.__pattern)

    def Search(self, text):
        if not self.__isCompiled:
            self.Compile()

        index = 0
        match = 0

        while index + match < len(text):
            if text[index + match] == self.__pattern[match]:
                match += 1
                if match == len(self.__pattern):
                    return index
            else:
                index = index + match - self.__failList[match]
                match = max(self.__failList[match], 0)  # if match == 0 is should be 0, not -1
        return None


def Search(pattern, text):
    return KmpMachine(pattern).Search(text)