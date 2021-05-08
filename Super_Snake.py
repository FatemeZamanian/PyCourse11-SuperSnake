
import pygame
import random
class Apple:
    def __init__(self):
        self.r=8
        self.x=random.randint(40,width-40)
        self.y=random.randint(40,height-40)
        self.color=(255,0,0)
    def show(self):
        # pygame.draw.circle(disp,self.color,[self.x,self.y],self.r)
        apl=pygame.image.load('apple.png')
        disp.blit(apl,(self.x,self.y))

class Bomb:
    def __init__(self):
        self.r=9
        self.x=random.randint(40,width-40)
        self.y=random.randint(40,height-40)
        self.color=(0,0,0)
    def show(self):
        #pygame.draw.circle(disp,self.color,[self.x,self.y],self.r)
        bmb=pygame.image.load('bomb.png')
        disp.blit(bmb,(self.x,self.y))


class Pear:
    def __init__(self):
        self.r=10
        self.x=random.randint(20,width-20)
        self.y=random.randint(20,height-20)
        self.color=(255,255,153)
    def show(self):
        #pygame.draw.circle(disp,self.color,[self.x,self.y],self.r)
        pr=pygame.image.load('pear.png')
        disp.blit(pr,(self.x,self.y))
        

class Snake:
    def __init__(self):
        self.w=16
        self.h=16
        self.x=width/2
        self.y=height/2
        self.color=(255,0,0)
        self.color3=(255,204,0)
        self.color2=(255,102,0)
        self.score=0
        self.x_change=0
        self.y_change=0
        self.speed=16
        self.body=[]

    def show(self):
        pygame.draw.rect(disp,self.color,[self.x,self.y,self.w,self.h])
        i=0
        for x in self.body:
            i+=1
            if i%2==0:
                pygame.draw.rect(disp,self.color3,[x['x'],x['y'],self.w,self.h])
            else:
                pygame.draw.rect(disp,self.color2,[x['x'],x['y'],self.w,self.h])
                

    def move(self):
        self.body.append({'x':self.x,'y':self.y})
        if len(self.body)>self.score:
            self.body.remove(self.body[0])
        if self.x_change==-1:
            self.x-=self.speed
        elif self.x_change==1:
            self.x+=self.speed
        elif self.y_change==-1:
            self.y-=self.speed
        elif self.y_change==1:
            self.y+=self.speed
        


    def eat_apple(self):
        if apple.x-apple.r <= self.x <= apple.x+apple.r and apple.y-apple.r <= self.y <= apple.y+apple.r:
            return True
        else:
            return False

    def eat_pear(self):
        if pear.x-pear.r <= self.x <= pear.x+pear.r and pear.y-pear.r <= self.y <= pear.y+pear.r:
            return True
        else:
            return False

    def eat_bomb(self):
        if bomb.x-bomb.r <= self.x <= bomb.x+bomb.r and bomb.y-bomb.r <= self.y <= bomb.y+bomb.r:
            return True
        else:
            return False

    def lose(self):
        if self.x>=width or self.x<=0 or self.y>=height or self.y<=0 or self.score<0:
            return True
        else:
            return False
            



if __name__=='__main__':
    bg=pygame.image.load('green_background.jpg')
    pygame.font.init()
    font=pygame.font.SysFont('comicsansms',35)
    width=400
    height=400
    disp=pygame.display.set_mode((width,height))
    clock=pygame.time.Clock()
    apple=Apple()
    snake=Snake()
    pear=Pear()
    bomb=Bomb()
    
    while True:
        
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP or event.key==pygame.K_w:
                    snake.y_change=-1
                    snake.x_change=0
                if event.key==pygame.K_DOWN or event.key==pygame.K_s:
                    snake.y_change=1
                    snake.x_change=0
                if event.key==pygame.K_LEFT or event.key==pygame.K_a:
                    snake.x_change=-1
                    snake.y_change=0
                if event.key==pygame.K_RIGHT or event.key==pygame.K_d:
                    snake.y_change=0
                    snake.x_change=1
        disp.blit(bg,(0,0))
        txt_score=font.render('Score: '+str(snake.score),True,(255,215,0))
        disp.blit(txt_score,(150,0))
        snake.show()
        apple.show()
        pear.show()
        bomb.show()
        snake.move()
        res_apple=snake.eat_apple()
        if res_apple==True:
            apple=Apple()
            snake.score+=1

        res_pear=snake.eat_pear()
        if res_pear==True:
            pear=Pear()
            snake.score+=2

        res_bomb=snake.eat_bomb()
        if res_bomb==True:
            bomb=Bomb()
            snake.score -=1
            
        if snake.lose()==True:
            disp=pygame.display.set_mode((300,200))
            img_lose=pygame.image.load('gameover.jpg')
            disp.blit(img_lose,(0,0))

        clock.tick((snake.score/3)+1)
        pygame.display.update()
