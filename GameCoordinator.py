
from GameLogic.Validator import Validator
from GameLogic.Evaluator import Evaluator
from GameLogic.EvaluatedCombination import EvaluatedCombination
from GameLogic.Attempts import Attempts
from Players.HumanPlayer import HumanPlayer

class GameCoordinator():

    def __init__(self, lengthOfGuess, numberOfColors, masterCombination, maxNumberOfAttempts):
        self.__gameIsRunning = False
        self.__player = HumanPlayer()
        self.__masterCombination = masterCombination
        self.__validator = Validator(lengthOfGuess, numberOfColors)
        self.__validator.checkCombination(self.__masterCombination)
        self.__evaluator = Evaluator(self.__masterCombination)
        self.__attempts = Attempts()
        self.__maxNumberOfAttempts = maxNumberOfAttempts


    def playGame(self):
        if not self.__gameIsRunning:
            self.__attempts.clearAttempts()
            self.__gameIsRunning = True
            print("Started a new MindMaster Game.")
            print("Setup is "+ str(self.__validator) +", you have a maximum number of "+ str(self.__maxNumberOfAttempts) +" attempts.")
            while self.__gameIsRunning:
                if self.__attempts.getNumberOfAttempts() < self.__maxNumberOfAttempts:
                    self.__playRound()
                else:
                    self.__gameIsRunning = False
                    print("You lost the game.")
                    print("You have reached the maximum number of "+ str(self.__attempts.getNumberOfAttempts()) +" tries.")



    def __playRound(self):
        gameIsFinished = self.__getAndProcessCombination()
        if gameIsFinished:
            self.__gameIsRunning = False
            print("You won the game.")
            print("The MasterCombination was: "+ str(self.__masterCombination) +". You needed "+ str(self.__attempts.getNumberOfAttempts()) +" of "+ str(self.__maxNumberOfAttempts) +" tries.")
        else:
            print(str(self.__attempts.getLastAttempt()) +" {"+ str(self.__attempts.getNumberOfAttempts()) +"/"+ str(self.__maxNumberOfAttempts) +"}")


    def __getAndProcessCombination(self):
        newCombination = self.__getNewUserCombination()
        evaluation = self.__evaluator.evaluateCombination(newCombination)
        self.__attempts.addEvaluatedCombination(EvaluatedCombination(newCombination, evaluation))
        return evaluation.gameFinished


    def __getNewUserCombination(self):
        while(True):
            try:
                userCmbi = self.__player.readInputIn()
                self.__validator.checkCombination(userCmbi)
                break
            except ValueError as e :
                print(str(e) +". Combination not valid, do it again. ")
        return userCmbi
