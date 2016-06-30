import Character
from OperationMinigame import *

class Doctor(Character.Character):
    className = 'Doctor'
    goal = 'perform your duties as a doctor and save those in need of medical attention.'
    abilityDefinition = 'successfully perform operations and save your patient.'
    minigameName = 'Operation' # or Culture Virus
    abilSuccess = 'You successfully perform the operation.' # or 'You successfully culture the bacteria'
    abilLoss = 'The operation fails.' # 'You fail to learn anything new.'
    image = 'doctor.png'

    def minigame(self, window, t):
        game = OperationMinigame(window)
        self.showEndScreen(window, game.You_Win, t)

    def showRules(self, window, t = 5):
        pygame.init()
        for i in range(t):
            window = pygame.display.set_mode([1200,800])
            pygame.display.set_caption("")
            window.fill([255,255,255])
            font = pygame.font.Font(None, 36)
            goal = 'Your objective is to ' + self.getAbilityDefinition()
            text1 = font.render(goal, 1, (0,0,0))
            countdown = font.render('Minigame starting in:     ' + str(t-i) , 1, (0,0,0))
            window.blit(text1, (10,10))
            window.blit(countdown, (10, 100))
            pygame.display.update()
            time.sleep(1)
            pygame.display.set_caption(self.minigameName)
        self.minigame(window, t)

    def showEndScreen(self, window, hasWon, t):
        if hasWon:
            words = self.getMinigameWinText()
            self.getPoints(1)
        else:
            words = self.getMinigameLossText()
        pygame.init()
        for i in range(t):
            window = pygame.display.set_mode([1200,800])
            pygame.display.set_caption("")
            window.fill((255,255,255))
            font = pygame.font.Font(None, 36)
            text = font.render(words, 1, (0,0,0))
            countdown = font.render('Returning to the main game in:     ' + str(t-i) , 1, (0,0,0))
            window.blit(text, (10,10))
            window.blit(countdown, (10, 100))
            pygame.display.update()
            time.sleep(1)

#s = pygame.display.set_mode([1,1])
#a = Doctor(1)
#a.showRules(s)