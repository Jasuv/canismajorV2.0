def Battle(atkr, dfndr):
    
    global enemiesKilled

    music.pause()
    sound.pause()
    battle.play(battleMusic, -1)

    basicFont = pygame.font.SysFont(None, 66, italic = True)
    

    atkrCopy = pygame.transform.scale(atkr.image, (320, 320))
    aHealthBar = []
    for i in range(0, atkr.stats['health']):
        aHealthBar.append(pygame.draw.rect(screen, (255,25,25), (i + 630, 500, 5, 20)))

    dfndrCopy = pygame.transform.scale(pygame.image.load('graphics/right2.png').convert_alpha(), (320, 320))
    dHealthBar = []
    for i in range(0, dfndr.stats['health']):
        dHealthBar.append(pygame.draw.rect(screen, (255,25,25), (i + 100, 500, 5, 20)))


    dfndrTimer = 0

    atkrTimer = 333

    winTimer = 400
    winText = False

    messageTimer = 200
    dfndrText = False

    fight = True
    while fight:

        atkPwr = 30

        villageSound.stop()
        
        screen.fill((255,131,123))

        for event in pygame.event.get():

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    battle.stop()
                    music.unpause()
                    sound.unpause()
                    fight = False

            # MOUSE EVENT DETECTION
            mx, my = pygame.mouse.get_pos()

            left, middle, right = pygame.mouse.get_pressed()

            rightClicking = False
            leftCLicking = False

            if dfndrTimer <= 0:
                btlAtk.display_enabled()
            else:
                btlAtk.display_disabled()
                
            if event.type == pygame.MOUSEBUTTONDOWN:

                if left:

                    leftClicking = True

                    print('left button clicked')

                    if btlAtk.clicked == True:

                        if dfndrTimer <= 0:

                            hitChance = random.randint(1,100)

                            if hitChance >= 13:
                                
                                dfndrText = True

                                try:
                                    print('attack successful')
                                    for i in range(atkPwr):
                                        aHealthBar.pop()
                                except:
                                    dfndrText = False
                                    winText = True
                                    enemiesKilled += 1

                            else:
                                print('Attack MISSED!')

                            dfndrTimer = 200
                            
              ##############################################################

                            if atkrTimer <= 0:
                                choices = ['atk', 'heal', 'escape']
                                choice = random.choice(choices)
                                if choice == 'atk':
                                    hitChance = random.randint(1, 100)
                                    if hitChance > 66 and hitChance < 99:
                                        print(choice)
                                    else:
                                        print(choice, 'misses')
                                elif choice == 'heal':
                                    print(choice)
                                elif choice == 'escape':
                                    print(choice)

                            atkrTimer = 333

                        else:
                            btlAtk.display_disabled()
                            print('wait for atk cooldown')

                        if btlDfn.clicked == True:
                            print('Defense Bubble Initiated')

                if middle:
                    print('middle button clicked')

                if right:
                    rightClicking = True
                    print('right button clicked')

            if event.type == pygame.MOUSEBUTTONUP:

                if left:
                    leftClicking = False

                if right:
                    rightClicking = False


        if dfndrText == True:######## PUT INTO SINGLE MULTI-USE FUNCTION??

            if messageTimer >= 0:
                messageToScreen(f"{dfndr.stats['name']} attacks!", 500, 600, 24)
                messageToScreen(f"Juggler takes {atkPwr} damage!", 500, 650, 24)

            else:
                messageTimer = 300
                dfndrText = False

            messageTimer -= 1
            #debug(messageTimer)

        if winText == True:######## PUT INTO SINGLE MULTI-USE FUNCTION??

            if winTimer >= 0:
                messageToScreen(f"Battle Over, {atkr} defeated!.", 500, 600, 24)

            else:
                battle.stop()
                music.unpause()
                sound.unpause()
                fight = False

            winTimer -= 2
            #debug(winTimer)


        aHealthDisplay = basicFont.render(str(len(aHealthBar)), False, (255,255,255))
        aHealthDisplayRect = aHealthDisplay.get_rect(center = atkr.rect.center)
        for hp in range(len(aHealthBar)):
            pygame.draw.rect(screen, (255,25,25), aHealthBar[hp])
        #screen.blit(aHealthDisplay, aHealthDisplayRect)

        dHealthDisplay = basicFont.render(str(len(dHealthBar)), False, (255,255,255))
        dHealthDisplayRect = dHealthDisplay.get_rect(center = dfndr.rect.center)
        for hp in range(len(dHealthBar)):
            pygame.draw.rect(screen, (255,25,25), dHealthBar[hp])
        #screen.blit(dHealthDisplay, dHealthDisplayRect)


        screen.blit(dfndrCopy,(w-800,h/4,10,10))
        screen.blit(atkrCopy, (w-300,h/4-30,10,10))


        btlAtk.draw()
        btlAtk.checkClick()

        btlDfn.draw()
        btlDfn.checkClick()

        btlInv.draw()
        btlInv.checkClick()


        # ATTACK TIMER TO LIMIT PLAYER ATK INPUT
        dfndrTimer -= 1
        #debug(dfndrTimer)
        if dfndrTimer <= 0:
            dfndrTimer = 0


        # ENEMY ATTACK LOGIC
        atkrTimer -= 1
        #messageToScreen(str(atkrTimer), atkr.rect.x, atkr.rect.y-30, 36) # SAME AS DEBUG()
        if atkrTimer <= 0:
            atkrTimer = 0

        if atkr.stats['health'] <= 0:
            print(f'battle over...{dfndr} defeated.')
            battle.stop()
            music.unpause()
            sound.unpause()
            fight = False


        pygame.display.update()

        clock.tick(60)

bossBeat = 0
stage2 = False
stage3 = False

def bossBattle(atkr, dfndr):

    global bossBeat, stage2, stage3, enemiesKilled

    music.pause()
    sound.pause()

    basicFont = pygame.font.SysFont(None, 66, italic = True)
    

    atkrCopy = pygame.transform.scale(atkr.image, (320, 320))
    atkrRect = atkrCopy.get_rect()
    aHealthBar = []
    for i in range(0, atkr.stats['health']):
        aHealthBar.append(pygame.draw.rect(screen, (255,25,25), (i + 630, 500, 5, 20)))

    dfndrCopy = pygame.transform.scale(pygame.image.load('graphics/right2.png').convert_alpha(), (320, 320))
    dfndrRect = dfndrCopy.get_rect()
    dHealthBar = []
    for i in range(0, dfndr.stats['health']):
        dHealthBar.append(pygame.draw.rect(screen, (255,25,25), (i + 100, 500, 5, 20)))


    dfndrTimer = 222

    atkrTimer = 333

    messageTimer = 300

    winTimer = 500
    winText = False
    winBox = pygame.Surface((500,250))
    winBoxRect = winBox.get_rect(topleft = (270,500))
    winBox.fill((123,123,132))


    atkText = False
    gameOver = False
    
    fight = True
    while fight:

        atkPwr = 30
        
        screen.fill((255,255,255))

        if dfndrTimer <= 0:
            btlAtk.display_enabled()
        else:
            btlAtk.display_disabled()

        for event in pygame.event.get():

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    boss.stop()
                    music.unpause()
                    sound.unpause()
                    enemiesKilled -= 1
                    fight = False

            # MOUSE EVENT DETECTION
            mx, my = pygame.mouse.get_pos()

            left, middle, right = pygame.mouse.get_pressed()

            rightClicking = False
            leftCLicking = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                if left:

                    leftClicking = True

                    print('left button clicked')

                    if btlAtk.clicked == True:

                        if dfndrTimer <= 0:

                            hitChance = random.randint(1,100)

                            if hitChance >= 13:
                                
                                atkText = True

                                try:
                                    print('attack successful')
                                    for i in range(atkPwr):
                                        aHealthBar.pop()
                                except:
                                    if stage2 == True:
                                        stage3 = True
                                        winText = True
                                    else:
                                        stage2 = True
                                        winText = True

                            else:
                                print('Attack MISSED!')

                            dfndrTimer = 150
                            

                            ##################

                            if atkrTimer <= 0:
                                choices = ['atk', 'heal', 'escape']
                                choice = random.choice(choices)
                                if choice == 'atk':
                                    hitChance = random.randint(1, 100)
                                    if hitChance > 66 and hitChance < 99:
                                        if dfndr.stats['health'] > 0:
                                            print(choice)
                                            for i in range(atkPwr):
                                                aHealthBar.pop()
                                        else:
                                            gameOver = True
                                    else:
                                        print(choice, 'misses')
                                elif choice == 'heal':
                                    print(choice)
                                elif choice == 'escape':
                                    print(choice)

                            atkrTimer = 333

                        else:
                            print('wait for atk cooldown')

                        if btlDfn.clicked == True:
                            print('Defense Bubble Initiated')

                if middle:
                    print('middle button clicked')

                if right:
                    rightClicking = True
                    print('right button clicked')

            if event.type == pygame.MOUSEBUTTONUP:

                if left:
                    leftClicking = False

                if right:
                    rightClicking = False


        if atkText == True:######## PUT INTO SINGLE MULTI-USE FUNCTION??

            if messageTimer >= 0:
                messageToScreen(f"{dfndr.stats['name']} attacks!", 500, 600, 24)
                messageToScreen(f"{atkr.stats['name']} takes {atkPwr} damage!", 500, 650, 24)

            else:
                messageTimer = 300
                atkText = False

            messageTimer -= 1
            #debug(messageTimer)

        if winText == True: ######## PUT INTO SINGLE MULTI-USE FUNCTION??
            if stage3 == True:
                enemiesKilled = 0
                Credits()
                fight = False
            
            elif winTimer >= 0:
                screen.blit(winBox, winBoxRect)
                messageToScreen(f"Battle Over,", 550, 600, 24)
                messageToScreen(f"{atkr} defeated!.", 550, 650, 24)

            elif stage2 == True:
                boss.stop()
                music.unpause()
                sound.unpause()
                bossLoading2()
                bossBattle(demonLion, sirius)

            

            winTimer -= 2
            #debug(winTimer)


        aHealthDisplay = basicFont.render(str(len(aHealthBar)), True, (255,50,50))
        for hp in range(len(aHealthBar)):
            pygame.draw.rect(screen, (255,25,25), aHealthBar[hp])
        aHealthDisplayRect = aHealthDisplay.get_rect(left = atkrRect.left)
        #screen.blit(aHealthDisplay, aHealthDisplayRect)

        dHealthDisplay = basicFont.render(str(len(dHealthBar)), True, (255,50,50))
        for hp in range(len(dHealthBar)):
            pygame.draw.rect(screen, (255,25,25), dHealthBar[hp])
        dHealthDisplayRect = dHealthDisplay.get_rect(right = dfndrRect.right)
        #screen.blit(dHealthDisplay, dHealthDisplayRect)


        screen.blit(dfndrCopy,(w-800,h/4,10,10))
        screen.blit(atkrCopy, (w-300,h/4-30,10,10))


        btlAtk.draw()
        btlAtk.checkClick()

        btlDfn.draw()
        btlDfn.checkClick()

        btlInv.draw()
        btlInv.checkClick()


        # ATTACK TIMER TO LIMIT PLAYER ATK INPUT
        dfndrTimer -= 1
        #debug(dfndrTimer)
        if dfndrTimer <= 0:
            dfndrTimer = 0


        # ENEMY ATTACK LOGIC
        atkrTimer -= 1
        #messageToScreen(str(atkrTimer), atkr.rect.x, atkr.rect.y-30, 36) # SAME AS DEBUG()
        if atkrTimer <= 0:
            atkrTimer = 0


        pygame.display.update()

        clock.tick(60)
