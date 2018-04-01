import pygame,sys,time,random,math,numpy
from pygame.locals import *
pygame.init()

black = 0,0,0
white = 255,255,255
SCREEN_H = 670
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 640
x = 0
y = 0
x1 = SCREEN_WIDTH
y1 = 0
box_height = 41
box_width = 52
box_x=0
box_y=SCREEN_HEIGHT/2
scoreBox_x = SCREEN_WIDTH-20
scoreBox_y = 0
enemy_height = 37
enemy_width = 41
enemyMove = 20
bullet_width = 27
bullet_height = 23
stageEnemies=[]
textWidth = 300
textHeight = 30
text_x = 0
text_y = 645
scoreText_x = 0
scoreValue_x = 90
levelText_x = 180
levelValue_x = 270
bossLifeScoreText_x = SCREEN_WIDTH - 150
bossLifeValueText_x = SCREEN_WIDTH - 30
boss_width = 99
boss_height = 97
scratch_width = 50
scratch_height = 50
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_H))
pygame.display.set_caption("my first game dude")
bg = pygame.image.load("background.jpg")
psipsinel = pygame.image.load("psipsinel2.png")
#magissa = pygame.image.load("hogatha_witch.png")
stageEnemies.append(psipsinel)
#stageEnemies.append(magissa)
clock = pygame.time.Clock()
score = 0
font = pygame.font.Font(None,40)
moveSpeed = 10
rounds=0
enemiesList=[]
enemiesPassed = 0
LEVEL_ENEMIES = 20
createBullets = False
printBullet=False
level = 1
bulletsList=[]
end=False
azraelCount = 0 
azraelBossMove_y = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
scratch_attack = False
azraelLife = 15


class Mario(object):
    def __init__(self):
        self.image = pygame.image.load("mario2.png")
        self.rect = pygame.Rect(0, SCREEN_HEIGHT/2, box_width, box_height)
        self.x = 0
        self.y= SCREEN_HEIGHT/2
        self.moveSpeed=20
    
    def handleKeys(self):
        global createBullets, end
        if key(pygame.K_LEFT) and self.x >= self.moveSpeed:
            self.x-= self.moveSpeed
            self.rect.x -= self.moveSpeed
        if key(pygame.K_RIGHT) and self.x + box_width <SCREEN_WIDTH - min(self.moveSpeed, box_width): 
            self.x+= self.moveSpeed
            self.rect.x += self.moveSpeed
        if key(pygame.K_UP) and self.y >= self.moveSpeed:
            self.y-=self.moveSpeed
            self.rect.y -= self.moveSpeed
        if key(pygame.K_DOWN) and self.y + box_height <SCREEN_HEIGHT :
            self.y+=self.moveSpeed
            self.rect.y += self.moveSpeed
        if pygame.key.get_pressed()[pygame.K_q]:
            sys.exit(0)
        for event in pygame.event.get():#for not continuous pressing
            if event.type == pygame.KEYDOWN and not end:
                if event.key == pygame.K_SPACE and len(bulletsList)<level:
                    createBullets=True
            

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def getRect(self):
        return self.rect


class Boss(object):
    def __init__(self):
        self.image = pygame.image.load("Azrael2.png")
        self.rect = pygame.Rect(SCREEN_WIDTH, SCREEN_HEIGHT/2, boss_width, boss_height)
        self.x = SCREEN_WIDTH
        self.y= SCREEN_HEIGHT/2
        self.moveSpeed_x = 10
        self.moveSpeed_y = 10

    def move(self, kinhsh):
        if self.x > SCREEN_WIDTH - boss_width:
            self.x -= self.moveSpeed_x
            self.rect.x -= self.moveSpeed_x

        self.y += kinhsh*self.moveSpeed_y
        self.rect.y += kinhsh*self.moveSpeed_y

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def getRect(self):
        return self.rect

    def lifespan(self, life):
        life -= 1
        return life

    def __del__(self):
        pass

class BossAttack(object):
    def __init__(self, x ,y):
        self.image= pygame.image.load("nixia2.png")
        self.rect = pygame.Rect(x, y, scratch_width, scratch_height)
        self.x = x
        self.y=y
        self.moveSpeed = 60
        
    def move(self):
        self.x -= self.moveSpeed
        self.rect.x -= self.moveSpeed

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def getRect(self):
        return self.rect

    def __del__(self):
        pass

    def getX(self):
        return self.x

class Bullets(object):
    def __init__(self, x ,y):
        self.image= pygame.image.load("bullet2.png")
        self.rect = pygame.Rect(x, y, bullet_width, bullet_height)
        self.x=x
        self.y=y
        self.moveSpeed = 50

    def move(self):
        self.x += self.moveSpeed
        self.rect.x += self.moveSpeed

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def getRect(self):
        return self.rect

    def __del__(self):
        pass

    def getX(self):
        return self.x




def key(key):
    global end
    if not end:
        return pygame.key.get_pressed()[key]
    else:
        return 0

def moveEnemies(enemiesList):
    for each in enemiesList:
        each[0]-=enemyMove
    return enemiesList

def spawnEnemies():
    global enemiesList
    if (len(enemiesList)<10):
        enemies = pygame.Rect(SCREEN_WIDTH-enemy_width,random.randrange(0, SCREEN_HEIGHT-enemy_height), enemy_width, enemy_height)
        enemiesList.append(enemies)
    

def deadEnemy(enemiesList):
    for i in range(len(enemiesList)) :
        if enemiesList[i][0]<0:
            return i

def enemyHit(box, enemiesList):
    return box.collidelistall(enemiesList)

def heroLevel(score):
    if score < 100:
        return 1
    elif score < 220:
        return 2
    elif score < 360:
        return 3 
    elif score < 640:
        return 4
    elif score < 1700:
        return 5
    elif score < 7800:
        return 6
    else:
        return 7


mario = Mario()
boss = Boss()


while 1:
    rounds+=1
   
    
    if pygame.event.get(pygame.QUIT): pygame.quit(); sys.exit(0)
    screen.blit(bg, (0, 0))
    x1 -= 5
    x -= 5
    screen.blit(bg, (x,y))
    screen.blit(bg, (x1,y1))
    if x <= -SCREEN_WIDTH:
        x = SCREEN_WIDTH
    if x1 <= -SCREEN_WIDTH:
        x1 = SCREEN_WIDTH
    mario.handleKeys()
    mario.draw(screen)
    pygame.draw.rect(screen, white, (text_x, text_y, SCREEN_WIDTH, textHeight))
    scoreText = font.render("Score: ", 1, black)
    screen.blit(scoreText, (text_x, text_y))
    if not end:
        scoreValue = font.render(str(score), 1, black)
    else:
        scoreValue = font.render("End", 1, black)
    screen.blit(scoreValue, (scoreValue_x, text_y))
    levelText = font.render("Level: ", 1, black)
    screen.blit(levelText, (levelText_x, text_y))
    levelValue = font.render (str(level), 1, black)
    screen.blit(levelValue, (levelValue_x, text_y))
    if (rounds%20==0 and enemiesPassed <= LEVEL_ENEMIES):
        spawnEnemies()
        enemiesPassed+=1
    if createBullets:
        bullet=Bullets(mario.get_x()+box_width, mario.get_y()+15)
        bulletsList.append(bullet)
        createBullets = False
    if len(bulletsList)>0: 
        for bullet in bulletsList:
            bullet.draw()
            bullet.move()
            bulletHit = enemyHit(bullet.getRect(), enemiesList)
            if bulletHit:
                del enemiesList[bulletHit[0]]
                bulletsList.remove(bullet)
                score += 10
            elif (bullet.getX() + bullet_width > SCREEN_WIDTH):
                bulletsList.remove(bullet)


    if enemiesPassed > LEVEL_ENEMIES and not end:
        boss.draw(screen)
        bossLifeText = font.render("Azrael: ", 1, black)
        screen.blit(bossLifeText, (bossLifeScoreText_x, text_y))
        bossLifeValue = font.render (str(azraelLife), 1, black)
        screen.blit(bossLifeValue, (bossLifeValueText_x, text_y))
        if rounds%3==0:
            boss.move(azraelBossMove_y[azraelCount%len(azraelBossMove_y)])
            azraelCount+=1
        if rounds%20 == 0 and boss.get_x() <= SCREEN_WIDTH - boss_width:
            scratch_attack = True
            bossattack = BossAttack(boss.get_x(), boss.get_y())
        if scratch_attack:
            bossattack.move()
            bossattack.draw()
            scratchHit = bossattack.getRect().colliderect(mario.getRect())
            if scratchHit:
                score -= 40
                del bossattack
                scratch_attack = False
            elif len(bulletsList)>0: 
                for bullet in bulletsList:
                    scratchBulletHit = bossattack.getRect().colliderect(bullet.getRect())
                    azraelBulletHit = boss.getRect().colliderect(bullet.getRect())
                    if scratchBulletHit:
                        score += 5
                        del bossattack
                        scratch_attack = False
                        bulletsList.remove(bullet)
                    elif azraelBulletHit:
                        azraelLife = boss.lifespan(azraelLife)
                        scratch_attack = False
                        

    for each in enemiesList:
        screen.blit(stageEnemies[0],each)
    moveEnemies(enemiesList)
    dead=deadEnemy(enemiesList)
    if dead!=None:
        del enemiesList[dead]
    hit = enemyHit(mario.getRect(), enemiesList)
    if hit:
        del enemiesList[hit[0]]
        score-=20
    

    level = heroLevel(score)

    if score < 0:
        end = True
        loseText = font.render("You loooooose", 1, black)
        screen.blit(loseText, (SCREEN_WIDTH/3, SCREEN_HEIGHT/2))

    if azraelLife == 0:
        end = True
        winText = font.render("You WOOOOON", 1, black)
        screen.blit(winText, (SCREEN_WIDTH/3, SCREEN_HEIGHT/2))
        
            
    

    pygame.display.update()
    clock.tick(60)
