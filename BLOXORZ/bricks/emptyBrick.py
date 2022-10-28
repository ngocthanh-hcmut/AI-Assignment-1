import bricks.brick as br
import globalVariable as const

class EmptyBrick(br.Brick):
    
    def __init__(self, positionX, positionY, screen):
        br.Brick.__init__(self, positionX, positionY, screen)
        self.color = const.EMPTY_BRICK_COLOR