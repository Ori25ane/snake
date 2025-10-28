
from pyray import *

init_windows=(800,450,"Mon jeu")
set_target_fps(60)

while not window_should_close():
    begin_drawing()
    clear_background(GRAY)
    draw_text("Hello Raylib!",190, 200, 20, LIGHTGRAY)
    
    end_drawing()

for i in range ():
    draw_rectangle(20,20,20,20,RED)

close_window()

snake=[[1+i,1+j],[2+i,1+j],[3+i,1+j]]

while not window_should_close():