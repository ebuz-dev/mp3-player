from tkinter import *
import pygame
import os

player = Tk()

player.title("MP3 Player")
player.geometry("260x420")

os.chdir("C:/Users/Ebuz/Python Projects/mp3player/Playlist")
songlist = os.listdir()

playlist = Listbox(player,highlightcolor="blue",selectmode = SINGLE)

for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos = pos + 1

pygame.init()
pygame.mixer.init()

def Play():
    pygame.mixer.music.load((playlist.get(ACTIVE)))
    songName.set(playlist.get(ACTIVE))
    pygame.mixer.music.play()

def ExitPlayer():
    pygame.mixer.music.stop()

def Pause():  
    pygame.mixer.music.pause()
    
def UnPause():  
    pygame.mixer.music.unpause()


buttons = Frame(player)
buttons.pack(side="top")

button1 = Button(player,width=5,height=3, text="PLAY",command=Play)
button2 = Button(player, width=5,height=3, text="STOP", command=ExitPlayer) 
button3 = Button(player, width=5,height=3, text="PAUSE", command=Pause)
button4 = Button(player, width=5,height=3, text="UNPAUSE", command=UnPause)


PlayButton = Button(buttons, width=5, height=3, text="PLAY", command=Play)
PlayButton.pack(side="left")


StopButton = Button(buttons, width=5, height=3, text="STOP", command=ExitPlayer)
StopButton.pack(side="left")

PauseButton = Button(buttons, width=5, height=3, text="Pause", command=Pause)
PauseButton.pack(side="left")

UnpauseButton = Button(buttons, width=5, height=3, text="Unpause", command=UnPause)
UnpauseButton.pack(side="left")

songName = StringVar()
songtitle = Label(player,textvariable=songName)


songtitle.pack()
playlist.pack(fill="both", expand="yes")



player.mainloop()