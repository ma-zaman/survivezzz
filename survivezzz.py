from Tkinter import *
import tkFont
import pygame
import random
import tkMessageBox
from PIL import Image

level1 = [
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]


level2 = [
            [0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0],
            [0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,1],
            [0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,1,0,0],
            [0,0,0,1,0,0,0,0,1,0,1,0,0,1,0,0,1,0,1,0],
            [0,0,0,1,0,0,1,0,1,0,1,0,0,0,0,1,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,0],
            [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            [0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0],
            [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            [0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0],
            [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            [0,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,0],
            [0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0],
            [0,0,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,0,0],
            [0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
            [1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1],
            [1,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,1],
            [1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1]]

pygame.mixer.init()

pygame.mixer.music.load("audio/bg_music.mp3")
pygame.mixer.music.set_volume(0.25)
pygame.mixer.music.play(-1)

player0 = pygame.mixer.Sound("audio/cry1.wav")
player0.set_volume(0.75)

player1 = pygame.mixer.Sound("audio/cry2.wav")
player1.set_volume(0.75)

zombie0 = pygame.mixer.Sound("audio/zombies0.wav")
zombie0.set_volume(0.75)

zombie1 = pygame.mixer.Sound("audio/zombies1.wav")
zombie1.set_volume(0.75)

zombie2 = pygame.mixer.Sound("audio/zombies2.wav")
zombie2.set_volume(0.75)

zombie3 = pygame.mixer.Sound("audio/zombies3.wav")
zombie3.set_volume(0.75)

explosion1 = pygame.mixer.Sound("audio/explosion1.wav")
explosion1.set_volume(0.6)

pistol1 = pygame.mixer.Sound("audio/pistol1.wav")
pistol1.set_volume(0.75)

reload1 = pygame.mixer.Sound("audio/reload.wav")
reload1.set_volume(0.75)

def new():
    c.delete(ALL)

def helpp():
    global imghand,value,helptitle,titley,c1,keystxt,upkeytxt,downkeytxt,leftkeytxt,rightkeytxt,shootkeytxt,reloadkeytxt,bombkeytxt,root
    titley = 45
    helproot = Toplevel()
    helproot.title('Help')
    print dir(Toplevel)
    c1 = Canvas(helproot,width= 400,height=500,bg='PeachPuff2')
    c1.mainloop()
    imghand = PhotoImage(file="pictures/hand.gif")
    c1.create_image(200,250,anchor=CENTER,image=imghand)
    helptitle = c1.create_text(200,titley,text='SURVIVEZZZ',anchor=CENTER,font='Helvetica 24 bold')
    keystxt = c1.create_text(200,titley+50,text='KEYS',anchor=CENTER,font='Helvetica 20 bold')
    upkeytxt = c1.create_text(200,titley+75,text='Up  --->  z, w, up',anchor=CENTER,font='Helvetica 12 bold')
    downkeytxt = c1.create_text(200,titley+100,text='Down  --->  s, down',anchor=CENTER,font='Helvetica 12 bold')
    leftkeytxt = c1.create_text(200,titley+125,text='Left  --->  q, a, left',anchor=CENTER,font='Helvetica 12 bold')
    rightkeytxt = c1.create_text(200,titley+150,text='Right  --->  d, right',anchor=CENTER,font='Helvetica 12 bold')
    shootkeytxt = c1.create_text(200,titley+175,text='Shoot  --->  space',anchor=CENTER,font='Helvetica 12 bold')
    reloadkeytxt = c1.create_text(200,titley+200,text='Reload  --->  r',anchor=CENTER,font='Helvetica 12 bold')
    bombkeytxt = c1.create_text(200,titley+225,text='Bomb  --->  b',anchor=CENTER,font='Helvetica 12 bold')
    value = StringVar()
    value.set(1)
    scale = Scale(helproot,from_=1,to=10,orient=VERTICAL,showvalue=0,length=500,variable=value,command=help_scroll)
    scale.grid(row=0,column=1)
    c1.grid(row=0,column=0)
    c1.focus_set()

    helproot.mainloop()
    helproot.destroy()

def help_scroll(valu):
    global imghand,value,helptitle,titley,c1,keystxt,upkeytxt,downkeytxt,leftkeytxt,rightkeytxt,shootkeytxt,reloadkeytxt,bombkeytxt,root
    if value<=valu:
        titley -= 25
        c1.delete(helptitle)
        c1.delete(keystxt)
        c1.delete(upkeytxt)
        c1.delete(downkeytxt)
        c1.delete(leftkeytxt)
        c1.delete(rightkeytxt)
        c1.delete(shootkeytxt)
        c1.delete(reloadkeytxt)
        c1.delete(bombkeytxt)
        helptitle = c1.create_text(200,titley,text='SURVIVEZZZ',anchor=CENTER,font='Helvetica 24 bold')
        keystxt = c1.create_text(200,titley+50,text='KEYS',anchor=CENTER,font='Helvetica 12 bold')
        upkeytxt = c1.create_text(200,titley+75,text='Up  --->  z, w, up',anchor=CENTER,font='Helvetica 12 bold')
        downkeytxt = c1.create_text(200,titley+100,text='Down  --->  s, down',anchor=CENTER,font='Helvetica 12 bold')
        leftkeytxt = c1.create_text(200,titley+125,text='Left  --->  q, a, left',anchor=CENTER,font='Helvetica 12 bold')
        rightkeytxt = c1.create_text(200,titley+150,text='Right  --->  d, right',anchor=CENTER,font='Helvetica 12 bold')
        shootkeytxt = c1.create_text(200,titley+175,text='Shoot  --->  space',anchor=CENTER,font='Helvetica 12 bold')
        reloadkeytxt = c1.create_text(200,titley+200,text='Reload  --->  r',anchor=CENTER,font='Helvetica 12 bold')
        bombkeytxt = c1.create_text(200,titley+225,text='Bomb  --->  b',anchor=CENTER,font='Helvetica 12 bold')
        value = valu
    else:
        titley += 25
        c1.delete(helptitle)
        c1.delete(keystxt)
        c1.delete(upkeytxt)
        c1.delete(downkeytxt)
        c1.delete(leftkeytxt)
        c1.delete(rightkeytxt)
        c1.delete(shootkeytxt)
        c1.delete(reloadkeytxt)
        c1.delete(bombkeytxt)
        helptitle = c1.create_text(200,titley,text='SURVIVEZZZ',anchor=CENTER,font='Helvetica 24 bold')
        keystxt = c1.create_text(200,titley+50,text='KEYS',anchor=CENTER,font='Helvetica 12 bold')
        upkeytxt = c1.create_text(200,titley+75,text='Up  --->  z, w, up',anchor=CENTER,font='Helvetica 12 bold')
        downkeytxt = c1.create_text(200,titley+100,text='Down  --->  s, down',anchor=CENTER,font='Helvetica 12 bold')
        leftkeytxt = c1.create_text(200,titley+125,text='Left  --->  q, a, left',anchor=CENTER,font='Helvetica 12 bold')
        rightkeytxt = c1.create_text(200,titley+150,text='Right  --->  d, right',anchor=CENTER,font='Helvetica 12 bold')
        shootkeytxt = c1.create_text(200,titley+175,text='Shoot  --->  space',anchor=CENTER,font='Helvetica 12 bold')
        reloadkeytxt = c1.create_text(200,titley+200,text='Reload  --->  r',anchor=CENTER,font='Helvetica 12 bold')
        bombkeytxt = c1.create_text(200,titley+225,text='Bomb  --->  b',anchor=CENTER,font='Helvetica 12 bold')
        value = valu

def keypress(event):
    global x,y,x1,y1,player,bullet_number,direction,n,bullet1,bullet2,bullet3,bullet4,bullet5,bomb_number,bomb1,bomb2,bomb3,bomb4,bomb5
    key = event.keysym
    player_wally = ((y/float(h))*100)
    player_wally = int(player_wally/5)
    player_wallx = ((x/float(w))*100)
    player_wallx = int(player_wallx/5)
    if (key == "Up" or key == 'z' or key == 'w') and y>5:
        direction = 'N'
        y -= 5
        y1 -= 5
        player_wally = ((y/float(h))*100)
        player_wally = int(player_wally/5)
        if game_board[player_wally][player_wallx] == 1:
            y += 5
            y1 += 5
        c.coords(gun,x+diff,y-10,x1,y1)

    elif (key ==  "Down" or key == 's') and y1<h-5:
        direction = 'S'
        y += 5
        y1 += 5
        player_wally = ((y1/float(h))*100)
        player_wally = int(player_wally/5)
        if game_board[player_wally][player_wallx] == 1:
            y -= 5
            y1 -= 5
        c.coords(gun,x+diff,y+diff,x1,y1+10)

    elif (key == "Left" or key == 'q' or key == 'a') and x>5:
        direction = 'W'
        x -= 5
        x1 -= 5
        player_wallx = ((x/float(w))*100)
        player_wallx = int(player_wallx/5)
        if game_board[player_wally][player_wallx] == 1:
            x += 5
            x1 += 5
        c.coords(gun,x1-diff,y+diff,x-10,y1)

    elif (key == "Right" or key == 'd') and x1<w-5:
        direction = 'E'
        x+=5
        x1 += 5
        player_wallx = ((x1/float(w))*100)
        player_wallx = int(player_wallx/5)
        if game_board[player_wally][player_wallx] == 1:
            x -= 5
            x1 -= 5
        c.coords(gun,x+diff,y+diff,x1+10,y1)

    elif key == "space":
        if bullet_number == 0:
            pistol1.play()
            bullet1 = bullets(direction)
            bullet1.movement()
            bullet_number += 1

        elif bullet_number == 1:
            pistol1.play()
            bullet2 = bullets(direction)
            bullet2.movement()
            bullet_number += 1

        elif bullet_number == 2:
            pistol1.play()
            bullet3 = bullets(direction)
            bullet3.movement()
            bullet_number += 1

        elif bullet_number == 3:
            pistol1.play()
            bullet4 = bullets(direction)
            bullet4.movement()
            bullet_number += 1

        elif bullet_number == 4:
            pistol1.play()
            bullet5 = bullets(direction)
            bullet5.movement()
            bullet_number += 1

        else:
            reload1.play()
            bullet_number = 0
            bullet1.destroy()
            bullet2.destroy()
            bullet3.destroy()
            bullet4.destroy()
            bullet5.destroy()

    elif key == "R" or key == "r":
        reload1.play()
        if bullet_number == 1:
            bullet1.destroy()

        elif bullet_number == 2:
            bullet1.destroy()
            bullet2.destroy()

        elif bullet_number == 3:
            bullet1.destroy()
            bullet2.destroy()
            bullet3.destroy()

        elif bullet_number == 4:
            bullet1.destroy()
            bullet2.destroy()
            bullet3.destroy()
            bullet4.destroy()

        elif bullet_number == 5:
            bullet1.destroy()
            bullet2.destroy()
            bullet3.destroy()
            bullet4.destroy()
            bullet5.destroy()
        bullet_number = 0

    elif key == "B" or key == "b":
        if bomb_number == 0:
            bomb1 = bombs()
            bomb_number += 1

    c.coords(player,x,y,x1,y1)

class bombs():
    def __init__(self):
        self.x = x1-diff
        self.y = y1-diff
        self.time = 3
        self.body = c.create_rectangle(self.x-2.5,self.y-2.5,self.x+2.5,self.y+2.5,width=1,fill='navy')

    def countdown(self):
        global explosion_view,bomb_number
        if self.time>0:
            self.time -= 1
        else:
            explosion1.play()
            c.delete(self.body)
            explosion_view = c.create_oval(self.x-15,self.y-15,self.x+15,self.y+15,width=1,fill='orange')
            bomb1.explosion_check()
            bomb_number -= 1
            root.after(250,bomb_delete)

    def explosion_check(self):
        global player_life
        try:
            for i in range(Kill+1):
                nbr_zombie[i].explosion_check(self.x,self.y)
        except:
            pass

        if self.x-15<x1 and self.x+15>x and self.y-15<y1 and self.y+15>y:
            player_life -= 3
            if player_life<0:
                player_life=0
            collision_player()

def bomb_main():
    global n,bomb1,bomb2,bomb3,bomb4,bomb5
    if bomb_number == 1:
        bomb1.countdown()

    root.after(1000,bomb_main)

def bomb_delete():
    global explosion_view
    c.delete(explosion_view)

class bullets():
    def __init__(self, d):
        self.direction = d
        if self.direction == 'N':
            difx = (x1-x+diff)/2
            self.x = x+diff+difx
            self.y = y-10
            self.y1 = y1
            self.body = c.create_line(self.x,self.y,self.x,self.y1,width=1,fill='red')

        elif self.direction == 'S':
            difx = (x1-x+diff)/2
            self.x = x+diff+difx
            self.y = y+diff
            self.y1 = y1+10
            self.body = c.create_line(self.x,self.y,self.x,self.y1,width=1,fill='red')

        elif self.direction == 'E':
            dify = (y1-y+diff)/2
            self.y = y+diff+dify
            self.x = x+diff
            self.x1 = x1+10
            self.body = c.create_line(self.x,self.y,self.x1,self.y,width=1,fill='red')

        elif self.direction == 'W':
            dify = (y1-y+diff)/2
            self.y = y+diff+dify
            self.x = x-10
            self.x1 = x1
            self.body = c.create_line(self.x,self.y,self.x1,self.y,width=1,fill='red')

    def movement(self):
        if self.direction == 'N':
            self.y-=5
            self.y1-=5
            c.coords(self.body,self.x,self.y,self.x,self.y1)

        elif self.direction == 'S':
            self.y+=5
            self.y1+=5
            c.coords(self.body,self.x,self.y,self.x,self.y1)

        elif self.direction == 'E':
            self.x+=5
            self.x1+=5
            c.coords(self.body,self.x,self.y,self.x1,self.y)

        elif self.direction == 'W':
            self.x-=5
            self.x1-=5
            c.coords(self.body,self.x,self.y,self.x1,self.y)

    def collision_check(self):
        try:
            for i in range(Kill+1):
                nbr_zombie[i].collision_check(self.x,self.y,self.direction)
        except:
            pass

    def destroy(self):
        c.delete(self.body)

def bullet_main():
    global n,bullet1,bullet2,bullet3,bullet4,bullet5
    if bullet_number == 1:
        bullet1.movement()
        bullet1.collision_check()

    elif bullet_number == 2:
        bullet1.movement()
        bullet2.movement()
        bullet1.collision_check()
        bullet2.collision_check()

    elif bullet_number == 3:
        bullet1.movement()
        bullet2.movement()
        bullet3.movement()
        bullet1.collision_check()
        bullet2.collision_check()
        bullet3.collision_check()

    elif bullet_number == 4:
        bullet1.movement()
        bullet2.movement()
        bullet3.movement()
        bullet4.movement()
        bullet1.collision_check()
        bullet2.collision_check()
        bullet3.collision_check()
        bullet4.collision_check()

    elif bullet_number == 5:
        bullet1.movement()
        bullet2.movement()
        bullet3.movement()
        bullet4.movement()
        bullet5.movement()
        bullet1.collision_check()
        bullet2.collision_check()
        bullet3.collision_check()
        bullet4.collision_check()
        bullet5.collision_check()

    root.after(10,bullet_main)


class zombie():
    global Kill,Label_kill
    def __init__(self, e, l, n):
        self.energy = e
        self.life = l
        self.number = n

    def __del__(self):
        pass

    def create_zombie(self):
        self.x = random.randint(2,19)
        self.y = random.randint(2,19)
        while game_board[self.y][self.x] == 1:
            self.x = random.randint(2,19)
            self.y = random.randint(2,19)
        self.x = ((self.x*5)/100.0)*float(w)
        self.y = ((self.y*5)/100.0)*float(h)
        if self.number < Kill:
            self.body = c.create_oval(self.x-diff,self.y-diff,self.x+diff,self.y+diff,outline = "red", fill = "darkgreen")
        else:
            self.body = c.create_oval(self.x-diff,self.y-diff,self.x+diff,self.y+diff,outline = "black", fill = "darkgreen")

    def movement(self):
        z_wally = ((self.y/float(h))*100)
        z_wally = int(z_wally/5)
        z_wallx = ((self.x/float(w))*100)
        z_wallx = int(z_wallx/5)
        if x > self.x:
            self.x+=self.energy
            z_wallx = (((self.x+diff)/float(w))*100)
            z_wallx = int(z_wallx/5)
            if game_board[z_wally][z_wallx] == 1:
                self.x-=self.energy

        elif x1 < self.x:
            self.x-=self.energy
            z_wallx = (((self.x-diff)/float(w))*100)
            z_wallx = int(z_wallx/5)
            if game_board[z_wally][z_wallx] == 1:
                self.x+=self.energy

        if y > self.y:
            self.y+=self.energy
            z_wally = (((self.y+diff)/float(h))*100)
            z_wally = int(z_wally/5)
            if game_board[z_wally][z_wallx] == 1:
                self.y-=self.energy

        elif y1 < self.y:
            self.y-=self.energy
            z_wally = (((self.y-diff)/float(h))*100)
            z_wally = int(z_wally/5)
            if game_board[z_wally][z_wallx] == 1:
                self.y+=self.energy

        c.coords(self.body,self.x-diff,self.y-diff,self.x+diff,self.y+diff)

    def kill_check(self):
        global player_life
        if x-2 <  self.x and x1+2 > self.x and y-2 < self.y and y1+2 > self.y:
            player_life -= 1
            collision_player()

    def collision_check(self,x,y,direction):
        global Kill,Label_kill,z0,z1,dead_z,game_board,level2
        if self.x-2.5 <= x <= self.x+2.5 and self.y-2.5 <= y <= self.y+2.5:
            if direction == 'N' or direction == 'S':
                c.create_oval(self.x-1,self.y-2.5,self.x+1,self.y+2.5,outline='brown',fill='red')
            else:
                c.create_oval(self.x-2.5,self.y-1,self.x+2.5,self.y+1,outline='brown',fill='red')
            sound = random.randint(0,3)
            if sound == 0:
                zombie0.play()
            elif sound == 1:
                zombie1.play()
            elif sound == 2:
                zombie2.play()
            else:
                zombie3.play()
            self.life -= 1
            if self.life == 0:
                c.delete(self.body)
                Kill+=1
                Label_kill.destroy()
                Label_kill = Label(root, text = "Kill :%02d" %Kill, fg ='firebrick', bg ='PeachPuff2')
                Label_kill.grid(row=1,column=0,sticky=W)
                try:
                    del(self.x,self.y,self.life,self.enegy,self.number,self.body)
                    del nbr_zombie[self.number]
                    nbr_zombie[self.number].__del__()
                except:
                    pass
                if Kill == 30:
                    Wave = 'II'
                    Label_wave = Label(root, text = "Wave : %s" %Wave, fg ='firebrick', bg ='PeachPuff2')
                    Label_wave.grid(row=1,column=0)
                    game_board = level2
                    for i in range(20):
                        for j in range(20):
                            if game_board[i][j] == 1:
                                c.create_image(j*w/20,i*h/20,anchor=NW,image=imgwall)

    def explosion_check(self,x,y):
        global Kill,Label_kill,z0,z1,dead_z,explosion_view,game_board,level2
        if self.x >= x-15 and x+15 >= self.x and self.y >= y-15 and  y+15 >= self.y:
            c.create_oval(self.x-2.5,self.y-2.5,self.x+2.5,self.y+2.5,outline='brown',fill='red')
            self.life -= 3
            if self.life < 0:
                self.life = 0
            sound = random.randint(0,3)
            if sound == 0:
                zombie0.play()
            elif sound == 1:
                zombie1.play()
            elif sound == 2:
                zombie2.play()
            else:
                zombie3.play()
            if self.life == 0:
                c.delete(self.body)
                Kill+=1
                Label_kill.destroy()
                Label_kill = Label(root, text = "Kill :%02d" %Kill, fg ='firebrick', bg ='PeachPuff2')
                Label_kill.grid(row=1,column=0,sticky=W)
                try:
                    del(self.x,self.y,self.life,self.enegy,self.number,self.body)
                    del nbr_zombie[self.number]
                    nbr_zombie[self.number].__del__()
                except:
                    pass
                if Kill == 10:
                    game_board = level2
                    for i in range(20):
                        for j in range(20):
                            if game_board[i][j] == 1:
                                c.create_image(j*w/20,i*h/20,anchor=NW,image=imgwall)


def zombie_main():
    global z0,z1
    for i in range(Kill+1):
        try:
            nbr_zombie[i].movement()
            nbr_zombie[i].kill_check()
        except:
            z0 = zombie(diff/10.0,1,0)
            z1 = zombie(diff/9.6,1,1)
            z2 = zombie(diff/9.2,1,2)
            z3 = zombie(diff/8.8,2,3)
            z4 = zombie(diff/8.4,2,4)
            z5 = zombie(diff/8.0,2,5)
            z6 = zombie(diff/7.6,3,6)
            z7 = zombie(diff/7.2,3,7)
            z8 = zombie(diff/6.8,3,8)
            z9 = zombie(diff/6.4,4,9)
            z10 = zombie(diff/6.0,8,10)
            z11 = zombie(diff/5.6,8,11)
            z12 = zombie(diff/5.2,8,12)
            z13 = zombie(diff/4.8,8,13)
            z14 = zombie(diff/4.4,9,14)
            z15 = zombie(diff/4.0,9,15)
            z16 = zombie(diff/3.6,9,16)
            z17 = zombie(diff/3.2,9,17)
            z18 = zombie(diff/2.8,9,18)
            z19 = zombie(diff/2.4,10,19)
            z20 = zombie(diff/2.0,10,20)
            z21 = zombie(diff/1.6,10,21)
            z22 = zombie(diff/1.4,10,22)
            z23 = zombie(diff/1.0,11,23)
            z24 = zombie(diff/0.6,11,24)
            z25 = zombie(diff/0.2,11,25)
            z26 = zombie(diff,11,26)
            z27 = zombie(diff*1.2,12,27)
            z28 = zombie(diff*1.4,15,28)
            z29 = zombie(diff*1.5,15,29)
            z30 = zombie(diff*2,20,30)
            nbr_zombie[i].create_zombie()

    root.after(100,zombie_main)

def collision_player():
    global player_life,Label_lives
    cry = random.randint(0,1)
    if cry == 0:
        player0.play()
    else:
        player1.play()
    Label_lives.destroy()
    Label_lives = Label(root, text = "Lives :%02d" %player_life, fg ='firebrick', bg ='PeachPuff2')
    Label_lives.grid(row=1,column=0,sticky=E)
    if player_life == 0:
        tkMessageBox.showwarning("SURVIVEZZZ","!!!!!GAME OVER !!!!!")
        root.quit()

root = Tk()
root.title('SURVIVEZZZ')

root.config(bg='PeachPuff2')

w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w/2
h = h/2
Kill = 0
Round = 1
game_board = level1
game_pause = False

picbackground = Image.open("pictures/bg.gif")
picwall = Image.open("pictures/wall.gif")

picbackground = picbackground.resize((w,h))
picbackground.save("pictures/bg1.gif", "GIF", colormode="color")

picwall = picwall.resize((w/20,h/20))
picwall.save("pictures/wall1.gif", "GIF", colormode="color")

c = Canvas(root,width= w,height=h,bg='PeachPuff2')

#imgheart = PhotoImage (file="pictures/heart.gif")
#imgdead = PhotoImage (file="pictures/dead_heart.gif")
imgwall =  PhotoImage(file="pictures/wall1.gif")
imgbackground = PhotoImage(file="pictures/bg1.gif")
imghand = PhotoImage(file="pictures/hand.gif")
imgblood = PhotoImage(file="pictures/blood.gif")

c.create_image(0,0,anchor=NW,image=imgbackground)
for i in range(20):
    for j in range(20):
        if game_board[i][j] == 1:
            c.create_image(j*w/20,i*h/20,anchor=NW,image=imgwall)

x = w/100
y = h/100
player_life = 5
bullet_number = 0
bomb_number = 0
Wave = 'I'
direction = 'E'

if x <=y:
    diff = x
else:
    diff = y

x=y=10-diff
x1=y1=10+diff

gun = c.create_rectangle(x+diff,y+diff,x1+10,y1,outline = "black", fill = "black")
player = c.create_oval(x,y,x1,y1,outline = "black", fill = "firebrick")

z0 = zombie(diff/10.0,1,0)
z1 = zombie(diff/9.6,1,1)
z2 = zombie(diff/9.2,1,2)
z3 = zombie(diff/8.8,2,3)
z4 = zombie(diff/8.4,2,4)
z5 = zombie(diff/8.0,2,5)
z6 = zombie(diff/7.6,3,6)
z7 = zombie(diff/7.2,3,7)
z8 = zombie(diff/6.8,3,8)
z9 = zombie(diff/6.4,4,9)
z10 = zombie(diff/6.0,8,10)
z11 = zombie(diff/5.6,8,11)
z12 = zombie(diff/5.2,8,12)
z13 = zombie(diff/4.8,8,13)
z14 = zombie(diff/4.4,9,14)
z15 = zombie(diff/4.0,9,15)
z16 = zombie(diff/3.6,9,16)
z17 = zombie(diff/3.2,9,17)
z18 = zombie(diff/2.8,9,18)
z19 = zombie(diff/2.4,10,19)
z20 = zombie(diff/2.0,10,20)
z21 = zombie(diff/1.6,10,21)
z22 = zombie(diff/1.4,10,22)
z23 = zombie(diff/1.0,11,23)
z24 = zombie(diff/0.6,11,24)
z25 = zombie(diff/0.2,11,25)
z26 = zombie(diff,11,26)
z27 = zombie(diff*1.2,12,27)
z28 = zombie(diff*1.4,15,28)
z29 = zombie(diff*1.5,15,29)
z30 = zombie(diff*2,20,30)

z0.create_zombie()

nbr_zombie = [z0,z1,z2,z3,z4,z5,z6,z7,z8,z9,z10,z11,z12,z13,z14,z15,z16,z17,z18,z19,z20,z21,z22,z23,z24,z25,z26,z27,z28,z29,z30]

zombie_main()
bullet_main()
bomb_main()

c.bind("<Key>",keypress)
c.focus_set()
c.grid(row=0,column=0)

Label_kill = Label(root, text = "Kill :%02d" %Kill, fg ='firebrick', bg ='PeachPuff2')
Label_kill.grid(row=1,column=0,sticky=W)

Label_wave = Label(root, text = "Wave : %s" %Wave, fg ='firebrick', bg ='PeachPuff2')
Label_wave.grid(row=1,column=0)

Label_lives = Label(root, text = "Lives :%02d" %player_life, fg ='firebrick', bg ='PeachPuff2')
Label_lives.grid(row=1,column=0,sticky=E)

menu = Menu(root)
menufile = Menu(menu,tearoff=0)
menuhelp = Menu(menu,tearoff=0)

menufile.add_command(label="New game",command=new)
menu.add_cascade(label="File", menu=menufile)

menu.add_command(label="Help",command=helpp)

root.config(menu=menu)

root.protocol("WM_DELETE_WINDOW",root.quit)

root.mainloop()
root.destroy()
