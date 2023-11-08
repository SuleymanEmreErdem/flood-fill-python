import pygame
import numpy as np

screen = pygame.display.set_mode((400, 400))

maze_arr = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                     [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
                     [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
                     [1, 0, 1, 1, 0, 1, 0, 1, 0, 1], #1's are wall, 0's are road 
                     [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
                     [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
                     [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

flood_arr = np.where(maze_arr==1, -1, maze_arr)

def display_maze():
    pygame.font.init()
    myfont = pygame.font.SysFont('Arial', 30)
    for i, x in enumerate(flood_arr):
        for j, y in enumerate(x):
            if y == -1:
                pygame.draw.rect(screen, 'black', (j*40, i*40, 40, 40))
            else:
                rect = pygame.draw.rect(screen, 'white', (j*40, i*40, 40, 40))
                textsurface = myfont.render(str(flood_arr[i][j]), False, (0, 0, 0))
                screen.blit(textsurface, (rect.x+5, rect.y))

def flood(x, y):
    search = 1
    flood_arr[x][y] = 1

    while np.where(flood_arr == 0)[0].size != 0:
        find = np.where(flood_arr == search)
        for i, j in zip(*find):
            if flood_arr[i-1][j] == 0:
                flood_arr[i-1][j] = search + 1
            if flood_arr[i+1][j] == 0:
                flood_arr[i+1][j] = search + 1
            if flood_arr[i][j-1] == 0:
                flood_arr[i][j-1] = search + 1
            if flood_arr[i][j+1] == 0:
                flood_arr[i][j+1] = search + 1
        search += 1


if __name__ == '__main__':
    print(maze_arr)
    flood(1, 1) #parameter selects the start point
    print(flood_arr)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        display_maze()

        pygame.display.flip()

    pygame.quit()
