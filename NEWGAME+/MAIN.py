
### Necessary imports
import pygame, json, turtle
from random import randint, choice
from sys import exit
from time import time
from debug import debug
from gamePkg.dice import diceRoll
from gamePkg.entityclass import Entity
from gamePkg.loadingfunc import Loading
from gamePkg.messagefunc import Write
from gamePkg.weaponclass import Weapon, WEAPONS

### Initialization and base variable constants
pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)

CLOCK = pygame.time.Clock()

WIDTH = 1024
HEIGHT = 768

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('This is a template'.upper())

### Player Instance
SIRIUS = Entity(100,100)

###

'''
BGI = pygame.transform.scale(pygame.image.load('graphics/DalleVillage.png'), (1024, 768))
BGIrect = BGI.get_rect()
'''

### Main game func/loop
def MAIN():

    #WINDOW.blit(BGI, BGIrect)

    ### func to show screen prompt (under construction)
    def Prompt(w, h, coords):
    
        prompt = pygame.Surface((w, h))
        prompt.fill((255,255,255))
        promptRect = prompt.get_rect(center = coords)

        promptTimer = 200

        prompting = False

        while promptTimer >= 1:

            WINDOW.blit(prompt, promptRect)

    ### Converts integer id tag to corresponding class instance
    for item in list(SIRIUS.stats['items']):
        if item == 0:
            SIRIUS.stats['items'].remove(item)
            SIRIUS.stats['items'].append(WEAPONS[0])
        if item == 1:
            SIRIUS.stats['items'].remove(item)
            SIRIUS.stats['items'].append(WEAPONS[1])

    print(SIRIUS.stats['items'])

    RUN = True

    while RUN:

        WINDOW.fill((50,50,255))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                data = {
                    'lvl': SIRIUS.stats['level'],
                    'xp': SIRIUS.stats['exp'],
                    '$': SIRIUS.stats['$$$'],
                    'hp': SIRIUS.stats['health'],
                    'mgc': [spell.tag for spell in SIRIUS.stats['magic']],
                    'inv': [item.tag for item in SIRIUS.stats['items']],
                    'eqp': {},
                    }

                with open('gameSave.txt', 'w') as gameSave:
                    json.dump(data, gameSave)

                print('FILE SAVED')

                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    print('LEFT')

                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    print('RIGHT')

                elif event.key == pygame.K_g:
                    SIRIUS.stats['items'].append(WEAPONS[0])
                    print(SIRIUS.stats['items'])

                elif event.key == pygame.K_SPACE:
                    #SIRIUS.stats['items'].pop() if len(SIRIUS.stats['items']) > 0 else print('no items in inventory')
                    #print(SIRIUS.stats['items'])
                    #Loading()
                    diceRoll(20)

            if event.type == pygame.KEYUP:

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    print('LEFT RELEASED')

                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    print('RIGHT RELEASED')


        SIRIUS.update()
        pygame.display.update()

        '''for sprite in sorted(allSprites, key = lambda sprite: sprite.rect.bottom):
        pygame.display.get_surface().blit(sprite.image, sprite.rect)'''

### Call to MAIN func to run game
MAIN() if __name__ == '__main__' else print('Not Main')
