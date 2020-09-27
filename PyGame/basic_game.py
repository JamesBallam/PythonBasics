"""First simple PyGame application."""
import pygame


# Initialize the PyGame library
pygame.init()

# Create a screen of 800x600 pixels
screen = pygame.display.set_mode((800, 600))

# Construct a game clock
clock = pygame.time.Clock()

# Specify a frame rate of 60Hz
fps = 60

# Fill the screen with black
screen.fill((0, 0, 0))

# Draw some blue lines coming in from the top-left to bottom
for i in range(800):
    pygame.draw.line(
        screen,                     # Canvas
        (0, 0, i % 256),            # Color
        (0, 0),                     # Start
        (i, 599))                   # End

# Draw some red lines coming in from the top-right to bottom
for i in range(800):
    pygame.draw.line(
        screen,                     # Canvas
        (i % 256, 0, 0),            # Color
        (799, 0),                   # Start
        (i, 599))                   # End

# Draw some yellow lines coming in from the middle to top
for i in range(800):
    pygame.draw.line(
        screen,                     # Canvas
        (i % 256, i % 256, 0),      # Color
        (399, 299),                 # Start
        (i, 0))                     # End

# Draw a black circle in the middle
pygame.draw.circle(
    screen,                         # Canvas
    (0, 0, 0),                      # Color
    (399, 299),                     # Center
    40)                             # Radius

# Main game loop to keep things running
while True:
    # Tick the game clock
    clock.tick(fps)

    # Process game events
    for event in pygame.event.get():
        # Handle mouse-button up
        if event.type == pygame.MOUSEBUTTONUP:
            # Get coordinate of mouse
            pos = pygame.mouse.get_pos()

            # Draw grey circle on screen and print coordinates to console
            pygame.draw.circle(
                screen,             # Canvas
                (64, 64, 64),       # Color
                pos,                # Center
                30)                 # Radius
            print(f"Click at {pos}")
        if event.type == pygame.QUIT:
            quit()

    # Update the screen to display the new content
    pygame.display.update()
