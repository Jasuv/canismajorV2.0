import pygame

def Write(text, xPos, yPos, size):

    basicFont = pygame.font.SysFont(None, 36, italic = True)

    msg = basicFont.render(text, True, (33,33,33))
    msgRect = msg.get_rect(center = (xPos, yPos))
    msgBox = pygame.Rect(((msgRect.x - 3),
                          (msgRect.y - 3),
                          (msgRect.width + 3),
                          (msgRect.height + 3)))
    
    msgBoxFill = pygame.Rect(((msgRect.x - 3),
                              (msgRect.y - 3),
                              (msgRect.width + 3),
                              (msgRect.height + 3)))

    #pygame.draw.rect(screen, (123,23,123), msgBox, 5) # FOR PUTTING A BORDER AROUND THE TEXT
    #pygame.draw.rect(screen, (234,234,234), msgBoxFill)

    screen.blit(msg,msgRect)
