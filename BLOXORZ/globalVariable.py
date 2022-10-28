import pygame

# graphic infomation
BACKGROUND_COLOR = pygame.Color(47, 53, 66)

NORMAL_BRICK_COLOR = pygame.Color(87, 96, 111)
WEAK_BRICK_COLOR = pygame.Color(255, 127, 80)
BRICK_EDGE_COLOR = pygame.Color(47, 53, 66)
EMPTY_BRICK_COLOR = pygame.Color(0, 0, 0)
DESTINATION_BRICK_COLOR = pygame.Color(199, 236, 238)

PRISM_COLOR = [pygame.Color(30, 144, 255), pygame.Color(46, 213, 115), pygame.Color(83, 82, 237), pygame.Color(255, 107, 129), pygame.Color(0, 148, 50), pygame.Color(255, 195, 18), pygame.Color(27, 20, 100), pygame.Color(165, 94, 234)]

# object size infomation
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

BRICK_SIZE = 40

SQUARE_PRISM_WIDTH = 10
SQUARE_PRISM_HEIGHT = 20

CUBIC_SIZE = 10

MAP_WIDTH = BRICK_SIZE * 30
MAP_HEIGHT = BRICK_SIZE * 20

DNA_LENGTH = 30
POPULATION = 100

# initial information

INITIAL_BASE_BRICKS = [[3, 3]]
MOVE_TIME = 0.25 # seconds
NUMBER_TO_MUTATE = 10
NUMBER_OF_GEN_TO_MUTATE = 10