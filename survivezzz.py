from Tkinter import *
import pygame
import random
import tkMessageBox
from PIL import Image, ImageDraw

game_board = [
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
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

zombie0 = pygame.mixer.Sound("audio/zombies0.wav")
zombie0.set_volume(0.5)

zombie1 = pygame.mixer.Sound("audio/zombies1.wav")
zombie1.set_volume(0.5)

zombie2 = pygame.mixer.Sound("audio/zombies2.wav")
zombie2.set_volume(0.5)

zombie3 = pygame.mixer.Sound("audio/zombies3.wav")
zombie3.set_volume(0.5)

root = Tk()

def new():
    c.delete(ALL)

def keypress(event):
    global x,y,x1,y1,player
    key = event.keysym
    test_wally = ((y/float(H))*100)
    test_wally = int(test_wally/5)
    test_wallx = ((x/float(W))*100)
    test_wallx = int(test_wallx/5)
    if key == "Up" and y>5:
        y -= 10
        y1 -= 10
        test_wally = ((y/float(H))*100)
        test_wally = int(test_wally/5)
        if game_board[test_wally][test_wallx] == 1:
            y += 10
            y1 += 10
    elif key ==  "Down" and y1<H-5:
        y += 10
        y1 += 10
        test_wally = ((y1/float(H))*100)
        test_wally = int(test_wally/5)
        if game_board[test_wally][test_wallx] == 1:
            y -= 10
            y1 -= 10
    elif key == "Left" and x>5:
        x -= 10
        x1 -= 10
        test_wallx = ((x/float(W))*100)
        test_wallx = int(test_wallx/5)
        if game_board[test_wally][test_wallx] == 1:
            x += 10
            x1 += 10
    elif key == "Right" and x1<W-5:
        x+=10
        x1 += 10
        test_wallx = ((x1/float(W))*100)
        test_wallx = int(test_wallx/5)
        if game_board[test_wally][test_wallx] == 1:
            x -= 10
            x1 -= 10
    c.coords(player,x,y,x1,y1)

class zombie():
    def __init__(self, e, l):
        self.energy = e
        self.life = l
        self.x = random.randint(0,W/2)
        self.y = random.randint(0,H/2)
        self.body = c.create_oval(self.x-diff,self.y-diff,self.x+diff,self.y+diff,outline = "black", fill = "darkgreen")

    def movement(self):
        if x > self.x:
            self.x+=self.energy
        elif x1 < self.x:
            self.x-=self.energy
        if y > self.y:
            self.y+=self.energy
        elif y1 < self.y:
            self.y-=self.energy
        c.coords(self.body,self.x-diff,self.y-diff,self.x+diff,self.y+diff)

    def kill_check(self):
        global player_life
        if x-2 <  self.x and x1+2 > self.x and y-2 < self.y and y1+2 > self.y:
            player_life -= 1
            life()
            print(player_life)

def zombie_main():
    z0.movement()
    z1.movement()
    z0.kill_check()
    z1.kill_check()
    root.after(100,zombie_main)

def life():
    global player_life
    if player_life == 0:
        tkMessageBox.showwarning("SURVIVEZZZ","!!!!!GAME OVER !!!!!")
        root.destroy()


W = root.winfo_screenwidth()
H = root.winfo_screenheight()
W = W/2
H = H/2

picbackground = Image.open("pictures/background.gif")
picwall = Image.open("pictures/wall.gif")

picbackground = picbackground.resize((W,H))
picbackground.save("pictures/background1.gif", "GIF", colormode="color")

picwall = picwall.resize((W/20,H/20))
picwall.save("pictures/wall1.gif", "GIF", colormode="color")

c = Canvas(root,width= W,height=H)

picbackground = PhotoImage(file="pictures/background.gif")
picheart = PhotoImage (file="pictures/heart.gif")
picdead = PhotoImage (file="pictures/dead_heart.gif")
imgwall =  PhotoImage(file="pictures/wall1.gif")
imgbackground = PhotoImage(file="pictures/background1.gif")

c.create_image(0,0,anchor=NW, image=picbackground)

c.create_image(0,0,anchor=NW,image=imgbackground)
for i in range(20):
    for j in range(20):
        if game_board[i][j] == 1:
            c.create_image(j*W/20,i*H/20,anchor=NW,image=imgwall)

x = W/100
y = H/100
player_life = 5

if x <=y:
    diff = x
else:
    diff = y

x=y=10-diff
x1=y1=10+diff
life()

player = c.create_oval(x,y,x1,y1,outline = "black", fill = "firebrick")
z0 = zombie(diff/2, 3)
z1 = zombie(diff/3,6)

zombie_main()

c.bind("<Key>",keypress)
c.focus_set()
c.grid(row=0,column=0)

root.mainloop()
