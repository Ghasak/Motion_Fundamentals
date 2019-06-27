import sys, pygame, random, time
pygame.init()

size = width, height = 1380, 720
screen = pygame.display.set_mode(size)

done = False

Black=0,0,0
White=255,255,255

Time = 0
Second = 0
Minute = 0
Hour = 0
Day = 0


Clock = pygame.time.Clock()


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Fonts
    Font = pygame.font.SysFont("Trebuchet MS", 25)

    # Day
    DayFont = Font.render("Days:" + str(Day).zfill(2), 1, Black)
    DayFontR = DayFont.get_rect()
    DayFontR.center = (975, 20)
    # Hour
    HourFont = Font.render("Hours:" + str(Hour).zfill(2), 1, Black)
    HourFontR = HourFont.get_rect()
    HourFontR.center = (1075, 20)
    # Minute
    MinuteFont = Font.render("Minutes:" + str(Minute).zfill(2), 1, Black)
    MinuteFontR = MinuteFont.get_rect()
    MinuteFontR.center = (1190, 20)
    # Second
    SecondFont = Font.render("Seconds:" + (str(Second).zfill(2)), 1, Black)
    SecondFontR = SecondFont.get_rect()
    SecondFontR.center = (1317, 20)

    screen.fill(White)

    #Timer
#    while Time==0: this caused the crash !
    time.sleep(1)
    Second += 1
    screen.blit(SecondFont, SecondFontR)
    screen.blit(MinuteFont, MinuteFontR)
    screen.blit(HourFont, HourFontR)
    screen.blit(DayFont, DayFontR)

    if Second == 60:
        Second = 0
        Minute=Minute+1
    if Minute == 60:
        Minute = 0
        Second = 0
        Hour=Hour+1
    if Hour==24:
        Hour=0
        Second = 0
        Minutes=0
        Day=Day+1

    pygame.display.flip()

    Clock.tick(60)

pygame.quit()
