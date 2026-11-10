from ColabTurtlePlus.Turtle import *
import numpy as np

# Import your own code from TileFunctions.py and PaletteOptions.py
from TileFunctions import *
from PaletteOptions import *

# Create one function to handle everything
def generate_poster():
    
    title_text = input("Enter a title for the poster: ")
    
    nrows = int(input("Enter the grid height: "))
    while nrows < 3 or nrows > 8:
      print("The grid height must be between 3 and 8.")
      nrows = int(input("Enter the grid height: "))
    
    ncols = int(input("Enter the grid width: "))
    while ncols < 3 or ncols > 8:
      print("The grid width must be between 3 and 8.")
      ncols = int(input("Enter the grid width: "))
    
    print(f"The available color palettes are: {palette_names}")
    p_name = input("Enter the name of the color palette you wish to use: ")
    while p_name not in palette_names:
      print(f"Invalid palette name. The available color palettes are: {palette_names}")
      p_name = input("Enter the name of the color palette you wish to use: ")
    
    if p_name == "random":
      print("Now generating a random color palette...")
      palette = {}
      for key in ["bg", "primary", "secondary", "accent"]:
        r = np.random.randint(256)
        g = np.random.randint(256)
        b = np.random.randint(256)
        palette[key] = (r, g, b)
    else:
      palette = palette_options[p_name]
  
    # Setting up the poster size
    screen_width = 1000
    screen_height = 500
    horizontal_spacing = 20
    vertical_spacing_above = 20
    vertical_spacing_below = 180
  
    # Figure out how many tiles will fit
    size_horiz = (screen_width - horizontal_spacing * 2) / ncols
    size_vert = (screen_height - vertical_spacing_above - vertical_spacing_below) / nrows
  
    # Needs to fit both horizontally and vertically so choose the smaller size
    size = min(size_horiz, size_vert)  
  
    # Starting from the top right (x_offset and y_offst are both positive)
    y_offset = screen_height / 2 - vertical_spacing_above - size / 2
    x_offset = size * (ncols - 1) / 2
    
    # Set up the screen
    clearscreen()
    setup(screen_width, screen_height)
  
    # Initialize an invisible turtle
    t = Turtle()
    t.hideturtle()
    t.speed(0)  # Turn off animation
  
    # Draw the grid
    for row in range(nrows):
      # Move DOWN for the next row
      y = y_offset - size * row
    
      for col in range(ncols):
        # Move to the LEFT for the next column
        x = x_offset - size * col
    
        # Randomly choose which person's tile to draw
        make_tile = tile_functions[np.random.randint(len(tile_functions))]
  
        # Figure out tile_type and rotation
        if row == 0:
          if col == 0:
            tile_type = "corner"
            rotation = 0
          elif col == ncols - 1:
            tile_type = "corner"
            rotation = 90
          else:
            tile_type = "border"  # horizontal
            rotation = np.random.randint(2) * 180
        elif row == nrows - 1:
          if col == 0:
            tile_type = "corner"
            rotation = 270
          elif col == ncols - 1:
            tile_type = "corner"
            rotation = 180
          else:
            tile_type = "border"  # horizontal
            rotation = np.random.randint(2) * 180
        else:
          if col == 0 or col == ncols - 1:
            tile_type = "border"  # vertical
            rotation = 90 + np.random.randint(2) * 180
          else:
            tile_type = "center"
            rotation = np.random.randint(4) * 90
  
        # Call the tile function to draw the tile
        make_tile(t, x, y, size, rotation, palette, tile_type)
    
    # Write the title and credits below the grid
    t.jumpto(0, -screen_height / 2 + vertical_spacing_below - 30)
    t.pencolor(palette["primary"])
    t.write(title_text, align="center", font=(20, "Arial", "bold"))
    t.setheading(270)
    t.forward(30)
    t.write("By Sarah Chase", align="center", font=(20, "Arial", "bold"))
    
    # Draw the color palette colors
    t.jumpto(-245, -190)
    for v in palette.values():
      t.color(v, v)
      t.setheading(90)
      t.pendown()
      t.begin_fill()
      t.forward(40)
      t.right(90)
      t.forward(100)
      t.right(90)
      t.forward(40)
      t.right(90)
      t.forward(100)
      t.end_fill()
      t.penup()
      t.right(180)
      t.forward(50)
      t.right(90)
      t.forward(20)
    
      # Write the RGB values
      t.write(v, align="center")
      t.setheading(0)
      t.forward(80)
      t.left(90)
      t.forward(20)
  
    # Show the final image
    t.done()

  # Save the poster as an SVG file
saveSVG("/content/poster.svg")

