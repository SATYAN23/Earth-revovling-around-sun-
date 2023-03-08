import os
import math as m
import pygame
from datetime import datetime
import time
import pyautogui
width, height = pyautogui.size()
pygame.init()


os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %((73.15*width)/100, (46.67*height)/100)
i_icon = os.getcwd() + '.\p.png'
icon = pygame.image.load(i_icon)
pygame.display.set_icon(icon)
speed =0

def main():
    global speed
    color = (0, 255, 255)

    width = 500
    height = 500
    r = 200
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("earth-moon-relation")
    font = pygame.font.SysFont("Segoe UI", 25)
    clock = pygame.time.Clock()
    cpt = win.get_rect().center


    speed = (2*3.14*r)/(100/25)
    speed =  str(speed)
    print("velocity of moon around sun : " + speed)
    
        
    run = True
    while run:
        clock.tick(100/25)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False    
        


        #circle and spline lines
                

        
        i=0
        while i >=0:
              for i in range(0, 360):
                  win.fill((255, 255, 255))


                  S = "velocity of moon" +  " : "  + str(speed) + "units" 
                  draw3 = font.render(S, True, (0, 255,0))
                  win.blit(draw3,(180,10))

        
                  pygame.draw.circle(win, (71, 186,53),[r+50 +r*m.sin(m.radians(i)),r+50+r*m.cos(m.radians(i))],12,12)

                  pygame.draw.circle(win, (0, 255,0),[250,250],200,2)
                  pygame.draw.circle(win, (71, 186,53),[cpt[0],cpt[1]],25,25)

                  pygame.draw.line(win, (0, 255,0), (250,50), (250,450))
                  pygame.draw.line(win, (0, 255,0), (50,250), (450,250))

                  pygame.draw.line(win,(0, 255,0), (r + 50 + r * m.cos(m.radians(135)),r + 50 +  r * m.sin(m.radians(135))),
                         (r + 50 -r * m.cos(m.radians(135)) ,r +50 - r * m.sin(m.radians(135))))

                  pygame.draw.line(win,(0, 255,0), (r + 50 - r * m.cos(m.radians(45)),r +50 - r * m.sin(m.radians(45))),
                         (r + 50+r * m.cos(m.radians(45)) ,r + 50+ r * m.cos(m.radians(45))))
                  pygame.display.update()

            
        draw3 = font.render(str(speed), True, color)
        win.blit(draw3,(cpt[0] - 3 + r * m.cos(m.radians(30)), cpt[1] - 12 - r * m.sin(m.radians(30)))) 
        pygame.display.update()
        
    pygame.quit()
      
if __name__ == "__main__":
    main() 
















                
