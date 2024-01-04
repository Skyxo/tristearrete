from random import randint

def setup():
    size(1920, 1080, P3D)
    fullScreen()
    fill(225, 0, 0)
    textAlign(CENTER)
    textSize(70)
    
x, y = 0, 0
sensx = True
sensy = True
speed = 5
speedh = randint(1, 5)

def draw():
    global x, y, sensx, sensy, speed, speedh
    
    background(0)
    lights()
    translate(width/2, height/2)
    sizex = width/2-260
    sizey = height/2-10
    
    for i in range(100):
        text("T triste ? Arrete", x, y, -i/10)
    
    if x >= sizex and x >= -sizex and sensx == True:
        sensx = False
        speedh = randint(1, 5)
    if x <= -sizex and x <= sizex and sensx == False:
        sensx = True
        speedh = randint(1, 5)
        
    if y >= sizey and y >= -sizey and sensy == True:
        sensy = False
    if y <= -sizey+40 and y <= sizey and sensy == False:
        sensy = True    
            
    if sensx:
        x+=speed
    else:
        x-=speed
    
    if sensy:
        y+=speedh
    else:
        y-=speedh
