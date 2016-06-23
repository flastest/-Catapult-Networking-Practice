import Character
import pygame, clock, random

class Burglar(Character.Character):

    className = 'Burglar'
    goal = 'Steal as much as you can, while evading detection.'
    abilityDefinition = 'Pick the lock that stands in your way.'
    minigameName = 'Lockpick'
    abilSuccess = 'You successfully pick the lock.'
    abilLoss = 'You fail to pick the lock.'
    image = 'Robber.png'

    def minigame(self):
        minigameWon = False
        minigameLost = False
        startTime = time.clock()