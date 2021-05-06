
import pygame
import random
import time
class Apple:
    def __init__(self):
        self.r=8
        self.x=random.randint(5,width)
        self.y=random.randint(5,height)
        self.color=(255,0,0)
    def show(self):
        pygame.draw.circle(disp,self.color,[self.x,self.y],self.r)

class Bomb:
    def __init__(self):
        self.r=9
        self.x=random.randint(5,width)
        self.y=random.randint(5,height)
        self.color=(0,0,0)
    def show(self):
        pygame.draw.circle(disp,self.color,[self.x,self.y],self.r)


class Pear:
    def __init__(self):
        self.r=10
        self.x=random.randint(5,width)
        self.y=random.randint(5,height)
        self.color=(255,255,153)
    def show(self):
        pygame.draw.circle(disp,self.color,[self.x,self.y],self.r)

class Snake:
    def __init__(self):
        self.w=16
        self.h=16
        self.x=width/2
        self.y=height/2
        self.name='snake'
        self.color=(255,204,0)
        self.color2=(255,102,0)
        self.score=0
        self.x_change=0
        self.y_change=0
        self.speed=16
        self.body=[]
        global s
        s=0
    def show(self):
        pygame.draw.rect(disp,self.color,[self.x,self.y,self.w,self.h])
        self.move()
        global su,sl
        sl=16
        su=16
        for x in self.body:
            if self.y_change==1 and self.x_change==0:
                su-=self.h
                pygame.draw.rect(disp,self.color2,[x[0],x[1]+su,self.w,self.h])
            elif self.y_change==-1 and self.x_change==0:
                su+=self.h
                pygame.draw.rect(disp,self.color2,[x[0],x[1]+su,self.w,self.h])
            elif self.y_change==0 and self.x_change==1:
                sl-=self.w
                pygame.draw.rect(disp,self.color2,[x[0]+sl,x[1],self.w,self.h])
            elif self.y_change==0 and self.x_change==-1:
                sl+=self.w
                pygame.draw.rect(disp,self.color2,[x[0]+sl,x[1],self.w,self.h])
                

    def move(self):
        if self.x_change==-1:
            self.x-=self.speed
        elif self.x_change==1:
            self.x+=self.speed
        elif self.y_change==-1:
            self.y-=self.speed
        elif self.y_change==1:
            self.y+=self.speed
        for xx in self.body:
            if self.x_change==-1:
                xx[0]-=self.speed
            elif self.x_change==1:
                xx[0]+=self.speed
            elif self.y_change==-1:
                xx[1]-=self.speed
            elif self.y_change==1:
                xx[1]+=self.speed


    def eat_apple(self):
        if apple.x-apple.r <= self.x <= apple.x+apple.r and apple.y-apple.r <= self.y <= apple.y+apple.r:
            self.score+=1
            return True
        else:
            return False

    def eat_pear(self):
        if pear.x-pear.r <= self.x <= pear.x+pear.r and pear.y-pear.r <= self.y <= pear.y+pear.r:
            self.score+=2
            return True
        else:
            return False

    def eat_bomb(self):
        if bomb.x-bomb.r <= self.x <= bomb.x+bomb.r and bomb.y-bomb.r <= self.y <= bomb.y+bomb.r:
            self.score-=1
            return True
        else:
            return False

    def lose(self):
        
        # font=pygame.font.Font('freesansbold',35)
        if self.x+5>=width or self.x-5<=0 or self.y+5>=height or self.y-5<=0 or self.score<0:
            return True
        else:
            return False
            # disp.blit(img_lose,(0,0))
            # pygame.font.init()
            # font=pygame.font.SysFont('Comic Sans MS',35)
            # txt_lose=font.render('Game Over...!',True,(255,0,0))
            # disp.blit(txt_lose,(0,0))
        # if self.score<0:
        #     disp=pygame.display.set_mode((300,200))
        #     disp.blit(img_lose,(0,0))
        #     pygame.font.init()
        #     font=pygame.font.SysFont('Comic Sans MS',35)
        #     txt_lose=font.render('Game Over...!',True,(255,0,0))
        #     disp.blit(txt_lose,(0,0))




if __name__=='__main__':
    width=500
    height=500
    disp=pygame.display.set_mode((width,height))
    clock=pygame.time.Clock()
    apple=Apple()
    snake=Snake()
    pear=Pear()
    bomb=Bomb()
    pygame.font.init()
    font=pygame.font.SysFont('Comic Sans MS',35)
    
    while True:
        txt_score=font.render('Score : '+str(snake.score),True,(255,0,0),(0,0,0))
        disp.blit(txt_score,(100,0))
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
        disp.fill((0,0,128))
        snake_item=[]
        snake.show()
        apple.show()
        pear.show()
        bomb.show()
        res_apple=snake.eat_apple()
        if res_apple==True:
            apple=Apple()
            snake_item.append(snake.x)
            snake_item.append(snake.y)
            snake.body.append(snake_item)

        res_pear=snake.eat_pear()
        if res_pear==True:
            pear=Pear()
            snake_item.append(snake.x)
            snake_item.append(snake.y)
            snake.body.append(snake_item)
            snake_item=[]
            snake_item.append(snake.x)
            snake_item.append(snake.y)
            snake.body.append(snake_item)

        res_bomb=snake.eat_bomb()
        if res_bomb==True:
            bomb=Bomb()
            if snake.score>0:
                snake.body.remove(snake.body[len(snake.body)-1])
            else:
                snake.score -=1
            
        if snake.lose()==True:
            disp=pygame.display.set_mode((300,200))
        print(snake.body)
        clock.tick(5)
        pygame.display.update()
