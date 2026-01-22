from random import randint

# Context Managers
# Allows us to do things and store them in groups
# Every manager can act differently but the general
# concept is that anything that happens inside a `with`
# statement will be lumped together, so anything inside a 
# glyph's undo manager, `⌘ Z` will apply to all of those actions

glyph = CurrentGlyph()

# Use a with statement to store and undo in the glyph object
with glyph.undo("SOMETHING COOL HAPPENED"):
    # Anything you do in this indent will be packaged into one undo called "SOMETHING COOL HAPPENED"
    # Loop through every contour in the glyph
    for contour in glyph.contours:
        # Loop through every point in the contour
        for point in contour.points:
            # Move that point horizontally
            point.x += randint(-100, 100)
    