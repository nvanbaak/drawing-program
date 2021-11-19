# nvb / 18 Nov 2021
# DrawingProgramIterator code

from drawing_program import DrawingProgram

class DrawingProgramIterator:
    def __init__(self, dp):

        if isinstance(dp, DrawingProgram):
            self.__dp = dp
        else:
            raise TypeError("Not a DrawingProgram object!")
        self.__index = 0

    def __iter__(self):
        pass