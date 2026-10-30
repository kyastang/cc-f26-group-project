# Copy all the tile functions in here

def draw_sarah_tile(t, x, y, size, rotation, palette, tile_type="center"):
  """
  Draws a parameterized geometric tile centered at (x, y).

  Parameters:
  - t: Turtle object
  - x, y (float/int): Center coordinates of the tile
  - size (float/int): Width and height of the tile bounding box
  - rotation (int): Orientation angle (0, 90, 180, 270)
  - palette (dict): RGB tuples with keys 'bg', 'primary', 'secondary', 'accent'
  - tile_type (str): "center", "border", or "corner" (defaults to "center")
  """

  # ==========================================
  # TURTLE SETUP
  # ==========================================
  t.penup()
  t.jumpto(x, y)
  t.setheading(rotation)

  # Useful relative dimension constants (derived from size)
  half = size / 2
  quarter = size / 4

  # ==========================================
  # BASE BACKGROUND
  # All tile variations share a clean backdrop
  # ==========================================
  # Move to the bottom-left corner relative to orientation
  t.forward(-half)
  t.left(90)
  t.forward(-half)
  t.right(90)

  t.pencolor(palette["bg"])
  t.fillcolor(palette["bg"])
  t.pensize(2)
  t.pendown()
  t.begin_fill()
  for _ in range(4):
      t.forward(size)
      t.left(90)
  t.end_fill()
  t.penup()

  # Return turtle to the true center of the tile
  t.jumpto(x, y)
  t.setheading(rotation)

  ######################### YOUR CHANGES START HERE ###########################

  # ==========================================
  # CONDITIONAL GEOMETRY (Based on tile_type)
  # ==========================================

  # ------------------------------------------
  # OPTION 1: CORNER TILE
  # ------------------------------------------
  if tile_type == "corner":

    ############## This part is my own drawing #######################
    ################## Change it to your design ######################
      t.pencolor(palette["accent"])
      t.pensize(3)
      t.forward(quarter)
      t.right(90)
      t.forward(quarter)
      t.left(180)

      t.pendown()
      t.forward(half)
      t.left(90)
      t.forward(half)
      t.penup()

      t.jumpto(x, y)
      t.setheading(rotation)
      t.color(palette["primary"], palette["primary"])
      t.forward(quarter + quarter / 2)
      t.left(90)
      t.forward(quarter)

      t.pendown()
      t.begin_fill()
      t.circle(quarter / 2)
      t.end_fill()
      t.left(90)
      t.forward(quarter / 2)
      t.color(palette["secondary"])
      t.dot(quarter / 4)
      t.penup()

  # ------------------------------------------
  # OPTION 2: BORDER TILE
  # ------------------------------------------
  elif tile_type == "border":

    ############## This part is my own drawing #######################
    ################## Change it to your design ######################
      t.color(palette["primary"], palette["primary"])
      t.forward(-half)
      t.left(90)
      t.forward(quarter)
      t.right(90)

      t.pendown()
      t.begin_fill()
      for _ in range(2):
          t.forward(size)
          t.left(90)
          t.forward(quarter)
          t.left(90)
      t.end_fill()
      t.penup()

      t.jumpto(x, y)
      t.setheading(rotation)
      t.pencolor(palette["accent"])
      t.pensize(3)
      t.forward(-half)
      t.pendown()
      t.forward(size)
      t.penup()

  # ------------------------------------------
  # OPTION 3: CENTER TILE
  # ------------------------------------------
  else:

    ############## This part is my own drawing #######################
    ################## Change it to your design ######################

      t.pencolor(palette["secondary"])
      t.jumpto(x, y)
      t.setheading(rotation + 45)
      t.forward(quarter * 1.2)
      t.left(90)
      t.forward(quarter * 1.2)
      t.pendown()
      for i in range(4):
          t.left(90)
          t.forward(half * 1.2)
      t.left(45)
      t.penup()

      t.forward(half * 0.9)

      t.color(palette["accent"])
      t.pendown()
      for i in range(5):
        t.left(144)
        t.forward(half * 0.2)
      t.penup()


      t.color(palette["primary"], palette["primary"])
      t.setheading(rotation + 60)
      for i in range(4):
        t.jumpto(x, y)
        t.pendown()
        t.begin_fill()
        for j in range(3):
            t.forward(quarter * 1.4)
            t.left(120)
        t.end_fill()
        t.penup()
        t.left(90)

      t.jumpto(x, y)
      t.setheading(rotation)
      t.pencolor(palette["accent"])
      t.pensize(2)

      for _ in range(8):
          t.pendown()
          t.forward(quarter * 0.9)
          t.penup()
          t.jumpto(x, y)
          t.right(45)




  # ==========================================
  # DRAW BORDER (OPTIONAL IF YOU WANT A BORDER)
  # ==========================================

  ############## This part is my own drawing #######################
  ################## Change it to your design ######################
  t.pencolor(palette["secondary"])
  t.pensize(2)

  # Go to the corner
  t.penup()
  t.jumpto(x, y)
  t.setheading(rotation)
  t.forward(-half)
  t.left(90)
  t.forward(-half)
  t.right(90)

  # Draw the border
  t.pendown()
  for _ in range(4):
      t.forward(size)
      t.left(90)
  t.penup()

  ######################### YOUR CHANGES END HERE #############################

  # ==========================================
  # TURTLE TEARDOWN
  # Reset pen, heading, and state for the next user
  # ==========================================
  t.penup()
  t.setheading(0)
  t.pencolor((0, 0, 0))


# This line at the end makes a list with everyone's functions
tile_functions = [draw_sarah_tile]
