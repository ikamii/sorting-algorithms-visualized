import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Bubble Sort Visualization')

# Colors
black = (0, 0, 0)
blue = (50, 100, 255)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)
grey = (200, 200, 200)

# Array settings
n = 100
array = [random.randint(10, height - 100) for _ in range(n)]
array_color = [blue] * n
array_width = max(width // n, 1)

# Frame rate control
clock = pygame.time.Clock()
frame_rate = 30  # Initial frame rate

# Sorting control
is_paused = True

# Function to draw the array
def draw_array(array, array_color):
    screen.fill(black)
    for i in range(len(array)):
        pygame.draw.rect(screen, array_color[i], (i * array_width, height - array[i], array_width, array[i]))
    pygame.display.flip()

# Bubble sort function with visualization
def bubble_sort(array):
    global frame_rate, is_paused
    n = len(array)
    i, j = 0, 0
    while i < n:
        if not is_paused:
            if j < n - i - 1:
                array_color[j] = red
                array_color[j + 1] = green
                draw_array(array, array_color)
                clock.tick(frame_rate)
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                array_color[j] = blue
                array_color[j + 1] = blue
                j += 1
            else:
                j = 0
                i += 1
        handle_events()

def handle_events():
    global frame_rate, is_paused
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_paused = not is_paused
            elif event.key == pygame.K_UP:
                frame_rate += 10
            elif event.key == pygame.K_DOWN:
                frame_rate = max(5, frame_rate - 10)
            elif event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

# Main loop
running = True
while running:
    handle_events()
    if not is_paused:
        bubble_sort(array)
    else:
        draw_array(array, array_color)
        pygame.display.flip()

pygame.quit()