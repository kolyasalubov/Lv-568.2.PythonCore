import pygame

pygame.font.init()

AQUAMARINE = (127, 255,	212)
GREEN = (1,	66,	37)
CHARTREUSE = (127, 255,	0)
LEMON_CREAM = (255, 250, 205)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((500, 550))

pygame.display.set_caption("Судоку")

x = 0
y = 0
dif = 500 / 9
val = 0

grid =[
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

font1 = pygame.font.SysFont("comicsans", 40)
font2 = pygame.font.SysFont("comicsans", 20)
def get_cord(pos):
    global x
    x = pos[0]//dif
    global y
    y = pos[1]//dif

def draw_box():
    for i in range(2):
        pygame.draw.line(screen, CHARTREUSE, (x * dif, (y + i)*dif), (x * dif + dif, (y + i)*dif), 7)
        pygame.draw.line(screen, CHARTREUSE, ((x + i) * dif, y * dif), ((x + i) * dif, y * dif + dif), 7)


def draw():
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:

                pygame.draw.rect(screen, AQUAMARINE, (i * dif, j * dif, dif + 1, dif + 1))

                text1 = font1.render(str(grid[i][j]), 1, GREEN)
                screen.blit(text1, (i * dif + 15, j * dif + 15))
    for i in range(10):
        if i % 3 == 0 :
            thick = 10
        else:
            thick = 1
        pygame.draw.line(screen, GREEN, (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(screen, GREEN, (i * dif, 0), (i * dif, 500), thick)

def draw_val(num):
    text1 = font1.render(str(num), 1, GREEN)
    screen.blit(text1, (x * dif + 15, y * dif + 15))

def raise_error():
    text2 = font1.render("Wrong !!! Not a valid Key", 1, BLACK)
    screen.blit(text2, (20, 520))
    pygame.display.update()

def valid(m, i, j, val):
    for it in range(9):
        if m[i][it]== val:
            return False
        if m[it][j]== val:
            return False
    it = i//3
    jt = j//3
    for i in range(it * 3, it * 3 + 3):
        for j in range (jt * 3, jt * 3 + 3):
            if m[i][j]== val:
                return False
    return True


run = True
flag1 = 0
rs = 0
error = 0

while run:


    screen.fill(LEMON_CREAM)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            get_cord(pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x-= 1
                flag1 = 1
            if event.key == pygame.K_RIGHT:
                x+= 1
                flag1 = 1
            if event.key == pygame.K_UP:
                y-= 1
                flag1 = 1
            if event.key == pygame.K_DOWN:
                y+= 1
                flag1 = 1
            if event.key == pygame.K_1:
                val = 1
            if event.key == pygame.K_2:
                val = 2
            if event.key == pygame.K_3:
                val = 3
            if event.key == pygame.K_4:
                val = 4
            if event.key == pygame.K_5:
                val = 5
            if event.key == pygame.K_6:
                val = 6
            if event.key == pygame.K_7:
                val = 7
            if event.key == pygame.K_8:
                val = 8
            if event.key == pygame.K_9:
                val = 9

            if event.key == pygame.K_d:
                rs = 0
                error = 0
                grid =[
                    [7, 8, 0, 4, 0, 0, 1, 2, 0],
                    [6, 0, 0, 0, 7, 5, 0, 0, 9],
                    [0, 0, 0, 6, 0, 1, 0, 7, 8],
                    [0, 0, 7, 0, 4, 0, 2, 6, 0],
                    [0, 0, 1, 0, 5, 0, 9, 3, 0],
                    [9, 0, 4, 0, 6, 0, 0, 0, 5],
                    [0, 7, 0, 3, 0, 0, 0, 1, 2],
                    [1, 2, 0, 0, 0, 7, 4, 0, 0],
                    [0, 4, 9, 2, 0, 6, 0, 0, 7]
                ]
    if val != 0:
        draw_val(val)

        if valid(grid, int(x), int(y), val):
            grid[int(x)][int(y)]= val
            flag1 = 0
        else:
            grid[int(x)][int(y)]= 0
            raise_error()
        val = 0

    if error == 1:
        raise_error1()
    if rs == 1:
        result()
    draw()
    if flag1 == 1:
        draw_box()

    pygame.display.update()

pygame.quit()
