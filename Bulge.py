import Draw

Draw.setCanvasSize(600,600)

#Grid- using a 2D list
numBoxes=15
grid=[[0 for j in range(numBoxes)] for i in range(numBoxes)]
size=40

#Drawing the checker-board
for row in range(numBoxes):
    for col in range(numBoxes):
        xCord=col*size 
        yCord=row*size
        blackBoxes=(row+col)%2==0 #where on the 2D list will there be black boxes
        whiteBoxes=(row+col)%2==1 #where on the 2D list will there be white boxes
        
        if blackBoxes: #Draw the black squares 
            Draw.setColor(Draw.BLACK)
            Draw.filledRect(xCord, yCord, size, size)
      
        ##Drawing the small boxes in the big boxes. The quantrans start from 1 at the top left corner going counter-clockwise
        #white small boxes and black small boxes in quandrant 2 and 4
        if ((row<7 and col<7 and row+col>=6) or (row>7 and col>7 and row+col<=22)):
            if blackBoxes and row>=2 and col>=2 and row<13 and col<13: 
                Draw.setColor(Draw.WHITE)
            elif whiteBoxes and row>=1 and col>=1 and row<14 and col<14:
                Draw.setColor(Draw.BLACK)
            Draw.filledRect(xCord+2, yCord+30, 8, 8)
            Draw.filledRect(xCord+30, yCord+2, 8, 8)
            
        #white small boxes and black small boxes in quandrant 1 and 3
        if ((row<7 and col>7 and abs(row-col)<=8) or (row>7 and col<7 and abs(row-col)<=8)):
            if blackBoxes and row>=2 and col>=2 and row<13 and col<13: 
                Draw.setColor(Draw.WHITE)
            elif whiteBoxes and row>=1 and col>=1 and row<14 and col<14:
                Draw.setColor(Draw.BLACK)            
            Draw.filledRect(xCord+30, yCord+30, 8, 8)
            Draw.filledRect(xCord+2, yCord+2, 8, 8)
          
        #black small boxes and white small boxes in center left
        if row==7 and col>=1 and col<7:
            if blackBoxes: 
                Draw.setColor(Draw.WHITE)
            else:
                Draw.setColor(Draw.BLACK)               
            Draw.filledRect(xCord+30, yCord+2, 8, 8)
            Draw.filledRect(xCord+30, yCord+30, 8, 8)

        #black small boxes and white small boxes in center right
        if row==7 and col>=8 and col<14:
            if blackBoxes: 
                Draw.setColor(Draw.WHITE)
            else:
                Draw.setColor(Draw.BLACK)
            Draw.filledRect(xCord+2, yCord+2, 8, 8)
            Draw.filledRect(xCord+2, yCord+30, 8, 8)
                
        #black small boxes and white small boxes in center up
        if col==7 and row>=1 and row<7:
            if blackBoxes: 
                Draw.setColor(Draw.WHITE)
            else:
                Draw.setColor(Draw.BLACK)
            Draw.filledRect(xCord+2, yCord+30, 8, 8)
            Draw.filledRect(xCord+30, yCord+30, 8, 8) 

        #black small boxes and white small boxes in center down
        if col==7 and row>=8 and row<=13:
            if blackBoxes: 
                Draw.setColor(Draw.WHITE)
            else:
                Draw.setColor(Draw.BLACK)            
            Draw.filledRect(xCord+2, yCord+2, 8, 8)
            Draw.filledRect(xCord+30, yCord+2, 8, 8)
            
Draw.show()