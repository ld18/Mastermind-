
class Validator():
    def __init__(self, lengthOfGuess, numberOfColors):
        self.__lengthOfGuess = lengthOfGuess
        self.__numberOfColors = numberOfColors
        self.__checkInitialParameter()


    def __checkInitialParameter(self):
        if not isinstance(self.__lengthOfGuess, int):
            raise ValueError('__lengthOfGuess is not a list')
        if not isinstance(self.__numberOfColors, int):
            raise ValueError('__numberOfColors is not a list')
        if self.__numberOfColors <= 0:
            raise ValueError('__numberOfColors is not valid (' + str(self.__numberOfColors) + ")")
        if self.__lengthOfGuess <= 0:
            raise ValueError('__lengthOfGuess is not valid (' + str(self.__lengthOfGuess) + ")")
        if self.__lengthOfGuess > self.__numberOfColors:
            raise ValueError('__numberOfColors is not valid (' + str(self.__lengthOfGuess) + ", " + str(self.__numberOfColors) + ")")


    def checkCombination(self, colorCombination):
        if not isinstance(colorCombination, list):
            raise ValueError('colorCombination is not a list')
        if len(colorCombination) < 1:
            raise ValueError('colorCombination is not valid ('+ str(colorCombination) +")")
        if len(colorCombination) != self.__lengthOfGuess:
            raise ValueError('colorCombination is not valid (' + str(colorCombination) +", " + str(self.__lengthOfGuess) + ")")
        for color in colorCombination:
            if not 0 <= color < self.__numberOfColors:
                raise ValueError('colorCombination is not valid (' + str(colorCombination) +", " + str(self.__numberOfColors) + ")")
        if len(colorCombination) != len(set(colorCombination)):
            raise ValueError('colorCombination is not valid ('+ str(colorCombination) +")")


    def checkEvaluation(self, rightColorWrongPlace, rightColorRightPlace):
        if not isinstance(rightColorWrongPlace, int):
            raise ValueError('rightColorWrongPlace is not a list')
        if not isinstance(rightColorRightPlace, int):
            raise ValueError('rightColorRightPlace is not a list')
        if not 0 <= rightColorWrongPlace <= self.__lengthOfGuess:
            raise ValueError('rightColorWrongPlace is not valid (' + str(rightColorWrongPlace) +", " + str(self.__lengthOfGuess) + ")")
        if not 0 <= rightColorRightPlace <= self.__lengthOfGuess:
            raise ValueError('rightColorRightPlace is not valid (' + str(rightColorRightPlace) +", " + str(self.__lengthOfGuess) + ")")
        if not 0 <= (rightColorWrongPlace + rightColorRightPlace) <= self.__lengthOfGuess:
            raise ValueError('rightColorRightPlace and rightColorWrongPlace are not valid (' + str(rightColorWrongPlace) +", " + str(rightColorRightPlace) +", " + str(self.__lengthOfGuess) + ")")


    def __str__(self):
        representation = "Validator: Number of colors =" + str(self.__numberOfColors) + ", Length of guess: " + str(self.__lengthOfGuess)
        return representation
