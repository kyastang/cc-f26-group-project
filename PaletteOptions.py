# Start with an empty dictionary
palette_options = {}

# Copy all the color palettes here

# Give each person's palette a different variable name
# Add your palette to the main dictionary
# Give your palette a unique name

sarah_palette = {
        "bg": (15, 12, 28),
        "primary": (255, 0, 110),
        "secondary": (0, 245, 212),
        "accent": (254, 228, 64)
    }
palette_options["Neon"] = sarah_palette  # The name is Neon

# Get a list of all the palette names.
palette_names = list(palette_options)

# Add a random palette option.
palette_names.append("random")

