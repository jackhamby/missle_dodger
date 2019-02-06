import pygame, time
from random import *
 

screenWidth = 400
screenHeight = 300


def getRandomColor():
    return (randint(0, 255),randint(0, 255),randint(0, 255))

class Hero:
    
    def __init__(self, x_position, y_position):
        self.xPos = x_position
        self.yPos = y_position
        self.height = 10
        self.score = 0
        self.width = 10
        self.color = (0, 128, 255)
        self.flying = False

    def render(self):
        pygame.draw.rect(screen, self.color , pygame.Rect(self.xPos, self.yPos, self.width, self.height))
    
    def move(self, x, y, dir_x, dir_y):

        # Move right
        if (dir_x > 0):
            if (self.detect_wall(self.xPos + x)):
                self.detect_treasure(self.xPos + x, self.yPos)
                self.xPos += x

            else:
                return        
        # Move left
        elif(dir_x < 0):
            if (self.detect_wall(self.xPos - x)):
                self.detect_treasure(self.xPos - x, self.yPos)
                self.xPos -= x
            else:
                return

        # Move up
        if (dir_y > 0):
            if (self.detect_ground(self.yPos + y)):
                self.detect_treasure(self.xPos, self.yPos + y)               
                self.yPos += y
            else:
                return

        # Move down
        elif(dir_y < 0):
            if (self.detect_ground(self.yPos - y)): 
                self.detect_treasure(self.xPos, self.yPos - y)               
              
                self.yPos -= y
            else:
                return
        

    def fly(self):
        self.flying = True
        myHero.move(0, 2, 1, -1)
        #print("we're flying")
        self.flying = False

    def detect_treasure(self, x_position, y_position):
        # check top left corner
        if  x_position >= treasure.xPos and \
            x_position <= (treasure.xPos + treasure.width) and \
            y_position >= treasure.yPos and \
            y_position <= (treasure.yPos + treasure.height) :
            treasure.claim()

        # check top right corner
        elif (x_position + self.width) >= treasure.xPos and \
             (x_position + self.width) <= (treasure.xPos + treasure.width) and \
             y_position >= treasure.yPos and \
             y_position <= (treasure.yPos + treasure.height) :
             treasure.claim()

        # check bottom left corner
        elif x_position >= treasure.xPos and \
             x_position <= (treasure.xPos + treasure.width) and \
             (y_position + self.height) >= treasure.yPos and \
             (y_position + self.height) <= (treasure.yPos + treasure.height) :
             treasure.claim()


        # check bottom right corner
        elif (x_position + self.width) >= treasure.xPos and \
             (x_position + self.width) <= (treasure.xPos + treasure.width) and \
             (y_position + self.height) >= treasure.yPos and \
             (y_position + self.height) <= (treasure.yPos + treasure.height) :
             treasure.claim()

    def detect_wall(self, x_position):
        if (x_position >= (screenWidth - self.width) or x_position < 0 ):
            return False
        else:
            return True

    def detect_ground(self, y_position):
        if (y_position <= 0 or y_position >= (ground.yPos - self.height)):
            return False
        else:
            return True



class Missle:
    def __init__(self):
        self.height = 5
        self.width = 5
        self.speed = 0
        self.xPos = screenWidth - 5
        self.yPos = randint(0, ground.yPos - self.height)
        self.color = getRandomColor()
        self.isDead = False


    def fire(self, speed):
        self.speed = speed

    def move(self):
        print('moving!')
        if (not self.detect_wall(self.xPos - self.speed) ):
            pass
        elif( not self.detect_hero(self.xPos - self.speed) ):
            pass
        else:
            self.xPos = self.xPos - self.speed
            pygame.draw.rect(screen, self.color , pygame.Rect(self.xPos, self.yPos, self.width, self.height))
            

    def detect_wall(self, x_position):
            if (x_position >= (screenWidth - self.width) or x_position < 0 ):
                self.isDead = True
                print("missle dead")
                return False
            else:
                return True
    
    def detect_hero(self, x_position):
        print('missle at x:' + str(self.xPos) + ' y:' + str(self.yPos))

        if  x_position >= myHero.xPos and \
            x_position <= (myHero.xPos + myHero.width) and \
            self.yPos >= myHero.yPos and \
            self.yPos <= (myHero.yPos + myHero.height) :
            self.isDead = True
            print('hit hero')
            if (self.speed > 5):
                myHero.score += 500
            else:
                myHero.score += 100
            return False
            
        # check top right corner
        elif (x_position+ self.width) >= myHero.xPos and \
            (x_position + self.width) <= (myHero.xPos + myHero.width) and \
            self.yPos >= myHero.yPos and \
            self.yPos <= (myHero.yPos + myHero.height) :
            self.isDead = True
            print('hit hero')
            if (self.speed > 5):
                myHero.score += 500
            else:
                myHero.score += 100

            return False

        # check bottom left corner
        elif x_position>= myHero.xPos and \
            x_position <= (myHero.xPos + myHero.width) and \
            (self.yPos + self.height) >= myHero.yPos and \
            (self.yPos + self.height) <= (myHero.yPos + myHero.height) :
            self.isDead = True
            print('hit hero')
            if (self.speed > 5):
                myHero.score += 500
            else:
                myHero.score += 100

            return False


        # check bottom right corner
        elif (x_position + self.width) >= myHero.xPos and \
            (x_position+ self.width) <= (myHero.xPos + myHero.width) and \
            (self.yPos + self.height) >= myHero.yPos and \
            (self.yPos + self.height) <= (myHero.yPos + myHero.height) :
            print('hit hero')
            self.isDead = True
            if (self.speed > 5):
                myHero.score += 500
            else:
                myHero.score += 100
            return False

        else:
            return True






class Treasure:

    def __init__(self):
        self.height = 15
        self.width = 15
        self.xPos = randint(0, screenWidth)
        self.yPos = randint(0, ground.yPos - self.height)
        self.color = getRandomColor()
        self.claimed = False

    def render(self):
            pygame.draw.rect(screen, self.color , pygame.Rect(self.xPos, self.yPos, self.width, self.height))

    def claim(self):
        self.xPos = randint(0, screenWidth)
        self.yPos = randint(0, ground.yPos - self.height)
        self.color = getRandomColor()





class Ground:

    def __init__(self):
        self.xPos = 0
        self.yPos = screenHeight/2
        self.width = screenWidth
        self.height = screenHeight/2
        self.color = (255, 0, 0)

    def render(self):
        pygame.draw.rect(screen, self.color , pygame.Rect(self.xPos, self.yPos, self.width, self.height))



def flush():
    screen.fill((0, 0, 0))

def gravity():
    if (not myHero.flying and myHero.detect_ground(myHero.yPos + 1)):
        #print('gravitying')
        myHero.move(0, 1, 1, 1) 
    else:
        return  

pygame.init()
screen = pygame.display.set_mode((screenWidth,screenHeight))
done = False


ground = Ground()
myHero = Hero(50, 50)
treasure = Treasure()
missle = Missle()
missle.fire(5)
myfont = pygame.font.SysFont("monospace", 15)

#missle.fire(randint(0, 10))



while not done:

    keys = pygame.key.get_pressed()
    # if keys[pygame.K_w]:
    #     myHero.move(0, 1, 1, -1)
    if keys[pygame.K_s]:
        myHero.move(0, 1, 1, 1)
    if keys[pygame.K_a]:
        myHero.move(1, 0, -1, 1)
    if keys[pygame.K_d]:
        myHero.move(1, 0, 1, 1)
    if keys[pygame.K_SPACE]:
        myHero.fly()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
   
    flush()

    
    
    gravity()
    myHero.render()
    ground.render()
    treasure.render()
    label = myfont.render(str(myHero.score), 1, (255,255,0))
    screen.blit(label, (0, 0))

    if (not missle.isDead):
        missle.move()
    else:
        print('making new missle')
        missle = Missle()
        missle.fire(randint(0, 10))

    pygame.display.flip()