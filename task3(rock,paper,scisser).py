import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
WIDTH, HEIGHT = 1530, 820
window_size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("My Animation")

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
# Define a font
FONT = pygame.font.Font(None, 42)

# Load images for rock, paper, and scissors
rock_image = pygame.image.load('rock.png')
paper_image = pygame.image.load('paper.png')
scissors_image = pygame.image.load('scissors.png')

def game():
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)

    user = None
    while user not in choices:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    user = "rock"
                elif event.key == pygame.K_p:
                    user = "paper"
                elif event.key == pygame.K_s:
                    user = "scissors"

        screen.fill((255, 255, 255 )) 
        text_surface = FONT.render("Press 'R' for rock, 'P' for paper, 'S' for scissors", True, BLACK)
        screen.blit(text_surface, (2 + 450, HEIGHT // 2 - 350))
        pygame.display.flip()

    # Wait for a short delay
    pygame.time.delay(500)

    # Display the user's choice
    if user == "rock":
        screen.blit(rock_image, (WIDTH // 2 - 200, HEIGHT // 2 - 50))
    elif user == "paper":
        screen.blit(paper_image, (WIDTH // 2 - 200, HEIGHT // 2 - 50))
    elif user == "scissors":
        screen.blit(scissors_image, (WIDTH // 2 - 200, HEIGHT // 2 - 50))
    pygame.display.flip()

    # Wait for a short delay
    pygame.time.delay(1000)
    
    # Display "Computer is thinking..."
    text_surface = FONT.render("Computer is thinking...", True, BLACK)
    screen.blit(text_surface, (WIDTH // 2 + 350, HEIGHT // 2 - 200))
    pygame.display.flip()
    pygame.time.delay(2000)  # wait for 1 second
    
    # Display the computer's choice
    if computer == "rock":
        screen.blit(rock_image, (WIDTH // 2 + 50, HEIGHT // 2 - 50))
        text_surface = FONT.render("Computer chose: Rock", True, BLACK)
        screen.blit(text_surface, (WIDTH // 2 + 50, HEIGHT // 2 - 100))
    elif computer == "paper":
        screen.blit(paper_image, (WIDTH // 2 +50, HEIGHT // 2 - 50))
        text_surface = FONT.render("Computer chose: Paper", True, BLACK)
        screen.blit(text_surface, (WIDTH // 2 + 50, HEIGHT // 2 - 100))
    elif computer == "scissors":
        screen.blit(scissors_image, (WIDTH // 2 + 50, HEIGHT // 2 - 50))
        text_surface = FONT.render("Computer chose: Scissors", True, BLACK)
        screen.blit(text_surface, (WIDTH // 2 + 50, HEIGHT // 2 - 100))
    pygame.display.flip()

    # Wait for a short delay
    pygame.time.delay(1000)

    # Determine the winner
    if user == computer:
        result = "It's a tie!"
    elif user == "rock":
        if computer == "scissors":
            result = "Rock smashes scissors! You win!"
        else:
            result = "Paper covers rock! You lose."
    elif user == "paper":
        if computer == "rock":
            result = "Paper covers rock! You win!"
        else:
            result = "Scissors cuts paper! You lose."
    elif user == "scissors":
        if computer == "paper":
            result = "Scissors cuts paper! You win!"
        else:
            result = "Rock smashes scissors! You lose."

    # Display the result
    screen.fill(YELLOW)
    text_surface = FONT.render(result, True, BLACK)
    screen.blit(text_surface, (WIDTH // 2 - 80, HEIGHT // 2 - 100))
    pygame.display.flip()

    # Wait for a short delay
    pygame.time.delay(2000)

start_game = False
# ...

# Load images for rock, paper, and scissors
rock_image = pygame.image.load('rock.png')
paper_image = pygame.image.load('paper.png')
scissors_image = pygame.image.load('scissors.png')

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_game = True

    # Fill the screen with black
    screen.fill(WHITE)

    # Add rock, paper, and scissors images in the background
    screen.blit(rock_image, (WIDTH // 2 - 250, HEIGHT // 2 - 150))
    screen.blit(paper_image, (WIDTH // 2 - 50, HEIGHT // 2 - 150))
    screen.blit(scissors_image, (WIDTH // 2 + 150, HEIGHT // 2 - 150))

    if not start_game:
        # Add a time delay to display the start button for a few seconds
        pygame.time.delay(1000)
    else:
        game()

    # Update the display
    pygame.display.flip()
    start_time = pygame.time.get_ticks()
    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_game = True

    # Fill the screen with black
        screen.fill(WHITE)
    # Add title
        title_surface = FONT.render("LOADING........ ", True, BLACK)
        screen.blit(title_surface, (WIDTH // 2 + 450, HEIGHT // 2 + 250))
        title_surface = FONT.render("LOADING ROCK, PAPER, SCISSOR GAME ", True, BLACK)
        screen.blit(title_surface, (WIDTH // 2 - 250, HEIGHT // 2 - 350))
    
        current_time = pygame.time.get_ticks()
        current_time = pygame.time.get_ticks()
        if current_time - start_time < 1000:  # 2 seconds
            screen.blit(rock_image, (WIDTH // 2 - 250, HEIGHT // 2 - 150))
        elif current_time - start_time < 2000:  # 4 seconds
            screen.blit(paper_image, (WIDTH // 2 - 50, HEIGHT // 2 - 150))
        elif current_time - start_time < 3000:  # 6 seconds
            screen.blit(scissors_image, (WIDTH // 2 + 150, HEIGHT // 2 - 150))
            
        if not start_game and current_time - start_time >= 3000:  # 6 seconds
            start_game = True

        if start_game:
            angle = 0
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
        
                screen.fill(WHITE)
        
                # Calculate the x and y coordinates of the dot
                x = WIDTH // 2 + int(50 * math.cos(math.radians(angle)))
                y = HEIGHT // 2 + int(50 * math.sin(math.radians(angle)))
        
                # Draw the dot
                pygame.draw.circle(screen, RED, (x, y), 6)
                

                # Add text "Press Enter key to start"
                text_surface = FONT.render("Press Enter key to start", True, BLACK)
                screen.blit(text_surface, (WIDTH // 2 - 150, HEIGHT // 2 - 350))
                
                # Update the display
                pygame.display.flip()
        
                # Increase the angle for the next frame
                angle += 1
        
                #  Add a delay to control the speed
                pygame.time.delay(2)
        
                # If the angle is 360 degrees, reset it to 0
                if angle >= 360:
                    angle = 0
        
                # If the user presses a key, exit the loop and start the game
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN]:
                    break
    
            game()
          
        # Update the display
        pygame.display.flip()