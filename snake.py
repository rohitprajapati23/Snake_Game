import pygame
import time
import random

pygame.init()

# Window dimensions
window_width = 600
window_height = 400

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (0, 0, 0)
green = (0, 255, 0)
blue = (97, 56, 84)

# Snake block size
block_size = 10
snake_speed = 15

# Font style
font_style = pygame.font.SysFont(None, 50)

# Initialize the window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

# Snake initial position and length
snake_block = 10
snake_speed = 15
snake_list = []
snake_length = 1

# Initial position of snake
snake_x = window_width / 2
snake_y = window_height / 2
snake_x_change = 0
snake_y_change = 0

# Position of food
food_x = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
food_y = round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0

# Function to display snake on screen
def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, black, [x[0], x[1], snake_block, snake_block])

# Display message on screen
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [window_width / 6, window_height / 3])

# Main game loop
game_over = False
game_close = False

while not game_over:
    while game_close == True:
        window.fill(blue)
        message("Press Q to exit & R to Restart", red)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                    game_close = False
                if event.key == pygame.K_c:
                    snake_x = window_width / 2
                    snake_y = window_height / 2
                    snake_length = 1
                    snake_list = []
                    snake_x_change = 0
                    snake_y_change = 0
                    food_x = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
                    food_y = round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0
                    game_close = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -snake_block
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = snake_block
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_y_change = -snake_block
                snake_x_change = 0
            elif event.key == pygame.K_DOWN:
                snake_y_change = snake_block
                snake_x_change = 0

    if snake_x >= window_width or snake_x < 0 or snake_y >= window_height or snake_y < 0:
        game_close = True
    snake_x += snake_x_change
    snake_y += snake_y_change
    window.fill(blue)
    pygame.draw.rect(window, green, [food_x, food_y, snake_block, snake_block])
    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    for x in snake_list[:-1]:
        if x == snake_head:
            game_close = True

    snake(block_size, snake_list)

    pygame.display.update()

    if snake_x == food_x and snake_y == food_y:
        food_x = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
        food_y = round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0
        snake_length += 1

    clock.tick(snake_speed)

pygame.quit()
quit()
