import Draw
import math

Draw.setCanvasSize(800,600)

#Background
UGLYYELLOW= Draw.color(205,205,66)
Draw.setBackground(UGLYYELLOW)
Draw.show()

#How many Ovals
numAcrossOvals=24
numDownOvals=8

#color of ovals
BLUE=Draw.color(11,104,245)
Draw.setColor(BLUE)

def _rotatePoint(x, y, angle):
    r = math.sqrt(x*x + y*y)
    theta = math.atan2(y, x)
    theta += angle
    newx = math.cos(theta) * r
    newy = math.sin(theta) * r
    return newx, newy

# draw a filled partial oval
def filledPartialOval(x, y, wide, high, degStart, degEnd, rot):
    coords=[]
    rot=math.radians(rot)    
    for angle in range(degStart, degEnd+1, 1):
        rad=math.radians(angle)
        newx=math.cos(rad)*wide/2
        newy=math.sin(rad)*high/2       
        newx, newy = _rotatePoint(newx, newy, rot)
        coords+=[x+newx, y-newy]
    Draw.filledPolygon(coords)
        
##Looping through the ovals        
#There are three rollers. Each roller has 8 ovals across. Each roller has: The END oval: the oval all the way to the left and all the way to the right. The BETWEEN oval: the oval second from the left, third from the left, second from the right, and third from the right. The MIDDLE oval: the forth oval from the left and the forth from the right.
for row in range(numDownOvals):
    xCord = 20 #Will start each row with the first oval 20 pixels to the left
    for col in range(numAcrossOvals):
       
        #to divide the positions of the ovals to detemine the width
        if col%8==7 or col%8==0: #END ovals
            w = 8 
        elif col%8==3 or col%8==4: #MIDDLE ovals
            w = 24 
        else: #BETWEEN ovals
            w = 16 
        
        yCord=(row)*75+15 #where to start the y-cordoorinate of the oval. row(which oval is it up to) * 75 (50 is the hight and plus 25 so thers is space between each oval) + 15 (start with each col 20 pixels down)
        
        
        ##Drawing and filling the ovals and half ovals
        #Color the half black ovals and then the white half ovals for the first and last roller
        if col <= 7 or col >=16:
            Draw.setColor(Draw.BLACK)
        else:
            Draw.setColor(Draw.WHITE)
        filledPartialOval(xCord+w/2, yCord+25, w+6, 56, 90, 270, 0)
        
        #Color the half white ovals and then the black half ovals for the second roller
        if col <= 7 or col >=16:
            Draw.setColor(Draw.WHITE)
        else:
            Draw.setColor(Draw.BLACK)
        filledPartialOval(xCord+w/2, yCord+25, w+6, 56, 90, 270, 180) 
        
        #Color the filled oval
        Draw.setColor(BLUE)
        Draw.filledOval(xCord, yCord, w, 50) #xCord and the yCord and the width. The height is always 50. 
        
        xCord+=w*2 #Start the next oval based on the x-coordinate, 2 times the width that it just drew in the column before.


Draw.show()