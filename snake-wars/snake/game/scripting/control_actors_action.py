import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        snake1 = cast.get_actor("snakes", 0)
        snake2 = cast.get_actor("snakes", 1)

        # left
        if self._keyboard_service.is_key_down('a'):
            snake1.turn_head(Point(-constants.CELL_SIZE,0))
            snake1.grow_tail(1)
        # right
        if self._keyboard_service.is_key_down('d'):
            snake1.turn_head(Point(constants.CELL_SIZE, 0))
            snake1.grow_tail(1)
        # up
        if self._keyboard_service.is_key_down('w'):
            snake1.turn_head(Point(0, -constants.CELL_SIZE))
            snake1.grow_tail(1)
        # down
        if self._keyboard_service.is_key_down('s'):             
            snake1.turn_head(Point(0, constants.CELL_SIZE))
            snake1.grow_tail(1)

        # left
        if self._keyboard_service.is_key_down('j'):
            snake2.turn_head(Point(-constants.CELL_SIZE,0))
            snake2.grow_tail(1)

        # right
        if self._keyboard_service.is_key_down('l'):
            snake2.turn_head(Point(constants.CELL_SIZE, 0))
            snake2.grow_tail(1)
        
        # up
        if self._keyboard_service.is_key_down('i'):
            snake2.turn_head(Point(0, -constants.CELL_SIZE))
            snake2.grow_tail(1)
        
        # down
        if self._keyboard_service.is_key_down('k'):            
            snake2.turn_head(Point(0, constants.CELL_SIZE))
            snake2.grow_tail(1)
