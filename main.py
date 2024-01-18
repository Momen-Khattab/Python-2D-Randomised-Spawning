import pygame, sys, random, math
import matplotlib.pyplot as plt
import numpy as np

pygame.init()

# Graph Coordinates
Graph_Width = 850
Graph_Height = 700


Covid_distance = 30
Repeating_targets = 30

# Colors
WHITE = (255, 255, 255)
RED = (255, 40, 40)

# Initialize the screen
screen = pygame.display.set_mode((Graph_Width, Graph_Height))
pygame.display.set_caption('simple 2D Fitts’ Law experiment')

'''using the random Lib,
we creating the random target_sizes'''
def Target_pos():
    angle = random.uniform(0, 2 * math.pi)
    distance = random.uniform(Covid_distance, Graph_Width / 2 - 50)
    x = int(Graph_Width / 2 + distance * math.cos(angle))
    y = int(Graph_Height / 2 + distance * math.sin(angle))

    return x, y

'''
creating the list depending on the sizes that mentioned before.
so it creates a 30 elements from 10,
30 from size 30
30 from size 50
so, the sum is 90 iterations,
and then rearranging the Elements randomly
'''
target_sizes = [10] * Repeating_targets + [30] * Repeating_targets + [50] * Repeating_targets
random.shuffle(target_sizes)



def draw_target(x, y, target_size):
    pygame.draw.circle(screen, RED, (x, y), target_size)


#loop
Counter = 0

#saving the last pos
current_target_position = Target_pos()



#while our Counter still under the Target size, keep working
while Counter < len(target_sizes):

    ''' iterating over the events in the Pygame event queue.
    Pygame events are things like mouse movements, keyboard presses, '''
    for event in pygame.event.get():
        #if i closed the game window -> quit
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

            '''checking if the event type is a mouse button down event,
            indicating that the user has clicked the mouse'''
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #getting the pos of the Mouse
            mouse_x, mouse_y = pygame.mouse.get_pos()
            distance = math.sqrt((mouse_x - current_target_position[0])**2 + (mouse_y - current_target_position[1])**2)

            '''to know, if the user clicked correctly on the target or not,
             if the distance between the click and the target is less than
              or equal to the size of the current target.
              it means the user successfully clicked on the target'''
            if distance <= target_sizes[Counter]:
                Counter += 1
                current_target_position = Target_pos()

    screen.fill(WHITE)
    draw_target(current_target_position[0], current_target_position[1], target_sizes[Counter])
    pygame.display.flip()

pygame.quit()
sys.exit()

'''
to Draw a graph for both conditions showing the ID and the MT distribution
we need to use matplotlib, and to use matplotlib, we need to ID and the MT equations to plot them,
'''