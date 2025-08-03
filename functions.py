import pygame
from datetime import datetime

def scale_image(img,factor):
    size=round(img.get_width()*factor),round(img.get_height()*factor)
    return pygame.transform.scale(img,size)

def blit_rotate_center(WIN,image,top_left,angle):
    rotated_image=pygame.transform.rotate(image,angle)
    new_rect=rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    WIN.blit(rotated_image,new_rect.topleft)

def blit_text_center(win,font,text):
    render=font.render(text,1,(250,250,250))
    win.blit(render,(win.get_width()/2-render.get_width()/2,win.get_height()/2-render.get_height()/2))

def record_result(winner, loser, boost_used):
    with open("results.txt", "a") as file:
        time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"Time: {time_str}\n")
        file.write(f"Winner: {winner}\n")
        file.write(f"Loser: {loser}\n")
        file.write(f"Boost Used: {'Yes' if boost_used else 'No'}\n")
        file.write("-" * 30 + "\n")