import sys
import pygame
import random
import time
from pygame.locals import *
pygame.init()
tract = 0
themostpowerfulvaluever = 0
qb = 0
color = (0,0,0)
uhhsf = 0
runmode = 0
while True:
    uwu = input("difficulty? (0 : cursed lmao, 1 : easy, 2 : normal, 3 : hard, 4 : extreme, 5 : insane, RUN) : ")
    if uwu == "RUN" :
        a = 120
        light_img = pygame.image.load("heart1.png")
        man_img = pygame.image.load("extract.png")
        sj_sound = pygame.mixer.Sound("mus_hereweare.ogg")
        u = 20
        uwu = int(1)
        uhhsf = random.randint(0,9)
        color= (255,255,255)
        runmode = 1
        break
    uwu = int(uwu)
    if uwu > 5 or uwu < 0:
        print("error")
    if uwu == 0:
        a = int(input("spear speed : "))
        light_img = pygame.image.load("spear.png")
        man_img = pygame.image.load("light.png")
        sj_sound = pygame.mixer.Sound("5.51 Final Trial.mp3")
        u = 30
        uhhsf = int(input("hp : "))
        uwu = 0
        break
    if uwu == 1:
        a = 85
        light_img = pygame.image.load("light.png")
        man_img = pygame.image.load("man.png")
        sj_sound = pygame.mixer.Sound("mad.mp3")
        u = 20
        break
    elif uwu == 2:
        a = 110
        light_img = pygame.image.load("arrow.png")
        man_img = pygame.image.load("frisk1.png")
        sj_sound = pygame.mixer.Sound("un.mp3")
        u = 30
        break
    elif uwu == 3:
        a = 160
        light_img = pygame.image.load("spear.png")
        man_img = pygame.image.load("frisk1.png")
        swe = random.randint(0, 1)
        if swe == 1:
            sj_sound = pygame.mixer.Sound("asgore.ogg")
        else :
            sj_sound = pygame.mixer.Sound("spamton_neo_mix_ex_wip.ogg")
        u = 33
        break
    elif uwu == 4:
        a = 220
        light_img = pygame.image.load("bone.png")
        man_img = pygame.image.load("ftft.png")
        swe = random.randint(0, 1)
        if swe == 1:
            sj_sound = pygame.mixer.Sound("MEGALOVANIA_music.mp3")
            
        else:
            sj_sound = pygame.mixer.Sound("ink.mp3")
        u = 42
        
        break
    elif uwu == 5:
        a = 255
        light_img = pygame.image.load("hope.png")
        man_img = pygame.image.load("ftft.png")
        sj_sound = pygame.mixer.Sound("hope.mp3")
        u = 45
        break
pov = pygame.mixer.Sound("raining.ogg")
guard_img = pygame.image.load("guard3.png")
SCREEN = pygame.display.set_mode((600, 600))
CLOCK = pygame.time.Clock()
sysfont = pygame.font.SysFont(None, 72)
sysfont1 = pygame.font.SysFont(None, 30)
sysfont2 = pygame.font.SysFont(None, 25)
heart_img = pygame.image.load("heart1.png")
extract = pygame.image.load("extract.png")
extract23 = pygame.image.load("extract23.png")
time_img = pygame.image.load("time.png")
bomb = pygame.image.load("bomb.png")
if(uwu == 0):
    heart_img = pygame.image.load("extract.png")
    bomb = pygame.image.load("frisk1.png")
    time_img = pygame.image.load("light.png")
#light_img = pygame.image.load("arrow.png")
#man_img = pygame.image.load("ftft.png")
sj_sound.play(-1)
l_size = light_img.get_size()
m_size = man_img.get_size()
p_size = extract.get_size()
time_size = time_img.get_size()
heart_size = heart_img.get_size()
att_size = bomb.get_size()
extract2_size = extract23.get_size()
score = 0

demon_x = []
demon_y = []
p_x = []
p_y = []
m_x, m_y = 250, 480
l_x = []
l_y = []
h_x = []
time_x = []
time_y = []
att_x = []
att_y = []
extract2_x = []
extract2_y = []
spo = 0
wing = 4 + uwu
for i in range( uwu + 3):
    
    h_x.append(spo)
    spo+=55
spo -=55
game_over = False
#a

cnt = 0
pygame.display.set_caption('Spear dodging simulator')
pygame.display.set_icon(light_img)
while True:
    if game_over:
        break
    ###summoning codes
    fms = random.randint(1, 12000)
    if fms >= 11992:
        extract2_x.append(random.randint(1, 580))
        extract2_y.append(0)
    fms = random.randint(1, 1000)
    if fms == 120:
        att_x.append(random.randint(1, 600))
        att_y.append(0)
    themostpowerfulvaluever +=1
    if themostpowerfulvaluever > 200:
        kkk = random.randint(1, 600)
        if kkk == 1:
            p_x.append(random.randint(0, 600))
            p_y.append(0)
            themostpowerfulvaluever = 0
    fms = random.randint(1, 600)
    if fms == 1:
        if len(time_x) < 1:
        
            time_x.append(random.randint(0, 600))
            time_y.append(0)
    fms = random.randint(1, 1000)
    if fms == 100:
        demon_x.append(random.randint(0,600))
        demon_y.append(0)
    ###
    SCREEN.fill(color)
    for event in pygame.event.get() :
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    cnt += 1
    if cnt >= u:
        cnt = 0
        l_x.append(random.randint(0, 600))
        l_y.append(0)
    for i in range(len(l_x)):
        l_y[i] += wing
        SCREEN.blit(light_img, (l_x[i], l_y[i]))
        if l_y[i] >= 550:
            l_x.remove(l_x[i])
            l_y.remove(l_y[i])
            score+=1
            break
    
    key_event = pygame.key.get_pressed()
    if key_event[pygame.K_LEFT]:
        if m_x > 0:
            m_x -= 5
        else:
            m_x +=5
    if key_event[pygame.K_RIGHT]:
        if m_x < 530:
            m_x += 5
        else:
            m_x-= 5
    #time bomb code
    for i in range(len(time_x)):
        if time_x[i] + time_size[0] >= m_x and m_x + m_size [0] >= time_x[i]:
            if time_y[i] - time_size[1] >= m_y:
                score-=3
                time_x.remove(time_x[i])
                time_y.remove(time_y[i])
                wing = 0
                firey = sysfont.render("Time Attack!", True, (255,200,190))
                SCREEN.blit(firey, (160, 250))
                pygame.display.update()
                time.sleep(3)
                pygame.display.update()
                wing = 4 + uwu
                
    SCREEN.blit(man_img, (m_x, m_y))
    #protection img script
    if(qb==1):
        if(uwu==1):
            SCREEN.blit(guard_img, (m_x-30, m_y-18))
        elif(uwu==2 or uwu==3):
            SCREEN.blit(guard_img, (m_x-17, m_y-34))
        elif(uwu==4 or uwu==5):
            SCREEN.blit(guard_img, (m_x-29, m_y-13))
        else:
            SCREEN.blit(guard_img, (m_x, m_y))
    d = sysfont1.render("score = %d" % score, True, (255, 255, 255))
    SCREEN.blit(d, (0, 550))
    # this is dah extract code
    for i in range(len(p_x)):
        if p_x[i] + p_size[0] >= m_x and m_x + m_size [0] >= p_x[i]:
            if p_y[i] - p_size[1] >= m_y:
                score+=7+(uwu*2)
                if qb == 1:
                    spo += 55
                    h_x.append(spo)
                    tract += 1
                    l_x.clear()
                    l_y.clear()
                    qb = 1
                    p_x.remove(p_x[i])
                    p_y.remove(p_y[i])
                else :
                    sj_sound.stop()
                    pov.stop()
                    pov.play(-1)
                    spo += 55
                    h_x.append(spo)
                    tract += 1
                    l_x.clear()
                    l_y.clear()
                    qb = 1
                    p_x.remove(p_x[i])
                    p_y.remove(p_y[i])
    #extract23 code
    for i in range(len(extract2_x)):
        if(i>=len(extract2_x)):
           break
        SCREEN.blit(extract23, (extract2_x[i], extract2_y[i]))
        if extract2_y[i] >= 550:
            extract2_x.remove(extract2_x[i])
            extract2_y.remove(extract2_y[i])
            break
            
        if extract2_x[i] + extract2_size[0] >= m_x and m_x + m_size [0] >= extract2_x[i]:
            if extract2_y[i] - extract2_size[1] >= m_y:
                for p in range(random.randint(1,3)):
                    spo += 55
                    h_x.append(spo)
                    score+=random.randint(2,4)
                extract2_x.remove(extract2_x[i])
                extract2_y.remove(extract2_y[i])
    #hp
    for i in range(len(demon_x)):
        if(i>=len(demon_x)):
           break
        demon_y[i] += 6
        SCREEN.blit(heart_img, (demon_x[i], demon_y[i]))
        if demon_y[i] >= 550:
            demon_x.remove(demon_x[i])
            demon_y.remove(demon_y[i])
            break
            
        if demon_x[i] + heart_size[0] >= m_x and m_x + m_size [0] >= demon_x[i]:
            if demon_y[i] - heart_size[1] >= m_y:
                spo += 55
                h_x.append(spo)
                score+=5
                demon_x.remove(demon_x[i])
                demon_y.remove(demon_y[i])
    #bomb script
    for i in range(len(att_x)):
        if att_x[i] + att_size[0] >= m_x and m_x + m_size [0] >= att_x[i]:
            if att_y[i] - att_size[1] >= m_y:
                score-=35
                if len(h_x) <= 3:
                    msg = sysfont.render("Game Over!", True, (255,0,0))
                    if(runmode ==1):
                        msg = sysfont.render("I SAID YOU TO RUN", True, (255,0,0))
                    SCREEN.blit(msg, (160, 250))
                    game_over = True
                    h_x.clear()
                    
                else:
                    if qb == 1:
                        pov.stop()
                        sj_sound.play(-1)
                        qb = 0
                        spo -= 55
                        h_x.pop()
                        att_x.clear()
                        att_y.clear()
                    else:
                        spo -= 55*3
                        for i in range(3):
                            h_x.pop()
                        att_x.clear()
                        att_y.clear()
                    
                    break
                
                game_over = True
    #spear or bullets                
    for i in range(len(l_x)):
        if l_x[i] + l_size[0] >= m_x and m_x + m_size [0] >= l_x[i]:
            if l_y[i] - l_size[1] >= m_y:
                score-=3
                if len(h_x) == 1:
                    msg = sysfont.render("Game Over!", True, (255,0,0))
                    if(runmode ==1):
                        msg = sysfont.render("I SAID YOU TO RUN", True, (255,0,0))
                    SCREEN.blit(msg, (160, 250))
                    game_over = True
                    h_x.pop()
                    
                else:
                    if qb == 1:
                        pov.stop()
                        sj_sound.play(-1)
                        qb = 0
                        l_x.remove(l_x[i])
                        l_y.remove(l_y[i])
                    else:
                        spo -= 55
                        h_x.pop()
                        l_x.remove(l_x[i])
                        l_y.remove(l_y[i])
                    
                    break
                
                game_over = True
                
    for i in range(len(h_x)):
        SCREEN.blit(heart_img, (h_x[i], 40))
    for i in range(len(time_x)):
        time_y[i] += 10
        SCREEN.blit(time_img, (time_x[i], time_y[i]))
        if time_y[i] >= 550:
            time_x.remove(time_x[i])
            time_y.remove(time_y[i])
            break
    for i in range(len(p_x)):
        
        p_y[i] += 7
        SCREEN.blit(extract, (p_x[i], p_y[i]))
        if p_y[i] >= 550:
            p_x.remove(p_x[i])
            p_y.remove(p_y[i])
            score+=1
            break
    #time bomb appearance
    for i in range(len(att_x)):
        att_y[i] += 8
        SCREEN.blit(bomb, (att_x[i],att_y[i]))
        if att_y[i] >= 550:
            att_x.remove(att_x[i])
            att_y.remove(att_y[i])
            break
    for i in range(len(extract2_x)):
        extract2_y[i] += 6
        SCREEN.blit(extract23, (extract2_x[i], extract2_y[i]))
        if extract2_y[i] >= 550:
            extract2_x.remove(extract2_x[i])
            extract2_y.remove(extract2_y[i])
            break
    heart_msg = sysfont2.render("hp : %d" % len(h_x), True, (255,0,0))
    SCREEN.blit(heart_msg, (4, 86))
    pygame.display.update()
    CLOCK.tick(a)
f = open("leaderboard.txt", "a")
meteor = time.time()
meteoroid = time.localtime(meteor)
if meteoroid.tm_hour > 12:
    sfsd = []
    sfsd.append(str(meteoroid.tm_hour - 12))
    sfsd.append("p.m.")
    sfsd = ' '.join(sfsd)
else:
    sfsd = []
    sfsd.append(str(meteoroid.tm_hour))
    sfsd.append("a.m.")
    sfsd = ' '.join(sfsd)
f.write("\n%dy/%d/%d %s:%d, difficultly : %d, record : %d\nextracts collected : %d\n" % (meteoroid.tm_year, meteoroid.tm_mon, meteoroid.tm_mday, sfsd, meteoroid.tm_min, uwu, score, tract))
f.close()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
