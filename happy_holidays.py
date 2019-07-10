# importing all options from the graphics.py library
from graphics import *

# setting up the function
def main ():
    
# setting up Graphics window parameters - title, coordinate size and direction,
  # and background color   
    win = GraphWin("Happy Holidays!")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    win.setBackground("sky blue")

# SNOWMAN

 # Creating snowman body, from bottom up, using 3 circles
    snowA = Circle(Point(2.5, 1.5), 1.5)
    snowA.setFill ("white")
    snowA.setWidth(0)
    snowA.draw (win)

    snowB = Circle(Point(2.5, 3.5), 1)
    snowB.setFill ("white")
    snowB.setWidth(0)
    snowB.draw (win)

    snowC = Circle(Point(2.5, 5.0), 0.75)
    snowC.setFill ("white")
    snowC.setWidth(0)
    snowC.draw (win)

 # Creating the stove pipe hat, using two rectangles 
    hatBrim = Rectangle(Point(1.5, 5.5), Point(3.5, 5.75))
    hatBrim.setFill ("black")
    hatBrim.draw (win)

    hat = Rectangle(Point(1.9, 5.75), Point(3.1, 6.75))
    hat.setFill ("black")
    hat.draw (win)

 # Creating snowman's eyes - creating one circle and then cloning it
    leftEye = Circle(Point(2.125, 5), 0.15)
    leftEye.setFill ("black")
    leftEye.draw (win)

    rightEye = leftEye.clone()
    rightEye.move (0.75, 0)
    rightEye.draw (win)

 # Creating the nose as a small triangle, using the polygon shape
    nose = Polygon (Point(2.4, 4.9), Point(2.4, 4.7), Point(2.6, 4.8))
    nose.setFill ("orange")
      # noticed setWidth didn't have any effect, so added "setOutline" option
      # to match the Fill color.
    nose.setWidth(0) 
    nose.setOutline ("orange")
    nose.draw (win)

 # Creating the smiling mouth, using points, since the scale was small
    p1 = Point(2.5, 4.5)
    p1.draw (win)

    p2 = Point(2.3, 4.55)
    p2.draw (win)

    p3 = Point(2.7, 4.55)
    p3.draw (win)

    p4 = Point(2.1, 4.6)
    p4.draw (win)

    p5 = Point (2.9, 4.6)
    p5.draw (win)

 # Creating the buttons, again using circles that are cloned
 # Naming was shortened so I wouldn't have to type as much
    midB = Circle(Point(2.5, 3.5), 0.15)
    midB.setFill ("black")
    midB.draw (win)

    topB = midB.clone ()
    topB.move (0, -0.5)
    topB.draw (win)

    botB = midB.clone ()
    botB.move (0, 0.5)
    botB.draw (win)

#TREE
    
  # Created trunk with a single rectangle
    trunk = Rectangle(Point(7.2, 0), Point(7.8, 1))
    trunk.setFill ("brown")
    trunk.setWidth(0)
    trunk.draw (win)

  # Creating the tree via four Triangle/Polygons, from bottom up.
  # Had problem with polygons again not liking the "setWidth" option.
    treeA = Polygon(Point(5.5, 1), Point(9.5, 1), Point(7.5, 3))
    treeA.setFill ("green")
    treeA.setOutline("green")
    treeA.draw (win)

    treeB = Polygon(Point(6, 2.5), Point(9, 2.5), Point(7.5, 4.5))
    treeB.setFill ("green")
    treeB.setOutline("green")
    treeB.draw (win)

    treeC = Polygon(Point(6.5, 4), Point(8.5, 4), Point(7.5, 5.5))
    treeC.setFill ("green")
    treeC.setOutline("green")
    treeC.draw (win)

    treeD = Polygon(Point(6.75, 5), Point(8.25, 5), Point(7.5, 6.5))
    treeD.setFill ("green")
    treeD.setOutline("green")
    treeD.draw (win)

  # Creating Gold Ornaments, 8 in total. Cloned circles.
    # Couldn't think of a good way to track these without excessively long
    # names, so went generic to save typing time
    ornA = Circle(Point(5.6, 0.9), 0.15)
    ornA.setFill ("gold")
    ornA.draw (win)

    ornB = ornA.clone ()
    ornB.move (3.8, 0)
    ornB.draw (win)

    ornC = ornA.clone ()
    ornC.move (1.9, 2)
    ornC.draw (win)

    ornD = ornA.clone ()
    ornD.move (1, 1)
    ornD.draw (win)

    ornE = ornA.clone ()
    ornE.move (2.9, 1)
    ornE.draw (win)

    ornF = ornA.clone ()
    ornF.move (1, 3)
    ornF.draw (win)

    ornG = ornA.clone ()
    ornG.move (2.8, 3)
    ornG.draw (win)

    ornH = ornA.clone ()
    ornH.move (1.9, 4.5)
    ornH.draw (win)

  # Creating Red Ornaments, 6 in total. Cloned Circles again.
    decA = Circle(Point(6.1, 2.4), 0.15)
    decA.setFill ("red")
    decA.draw (win)
    
    decB = decA.clone ()
    decB.move (2.8, 0)
    decB.draw (win)
    
    decC = decA.clone ()
    decC.move (1.4, 1.8)
    decC.draw (win)
    
    decD = decA.clone ()
    decD.move (1.4, -1.1)
    decD.draw (win)
    
    decE = decA.clone ()
    decE.move (0.7, 2.5)
    decE.draw (win)

    decF = decA.clone ()
    decF.move (2, 2.5)
    decF.draw (win)

  # Creating 5-pointed star treetop decoration, using Polygon object.
  # Plotted out a zoomed-in portion around the top of the tree to get
    # accurate decimal placement.  Only a couple minor adjustments were needed.
  # Polygons really want to keep their border width, so had to add "setOutline"
    # to match the fill color again (as with nose and tree objects). 
    star = Polygon (Point(7.5, 6.75), Point(7.7, 6.55), Point(7.6, 6.85), Point(7.8, 7.05),
                     Point(7.55, 6.95), Point(7.5, 7.2), Point(7.45, 6.95), Point(7.2, 7.05),
                     Point(7.4, 6.85), Point(7.3, 6.55))
    star.setFill ("yellow")
    star.setOutline("yellow")
    star.move (0, -0.17)
    star.draw (win)
     
main()

    
