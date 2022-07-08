import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def get_is_game_over(self):
        return self._is_game_over

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_food_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_food_collision(self, cast):
        """Updates the score nd moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        food = cast.get_actor("foods", 0)
        score_one = cast.get_actor("scores", 0)
        snake_one = cast.get_actor("snakes", 0)
        head_one = snake_one.get_head()
        score_two = cast.get_actor("scores", 1)
        snake_two = cast.get_actor("snakes", 1)
        head_two = snake_two.get_head()
        
        if head_one.get_position().get_y() + 5 == food.get_position().get_y() or head_one.get_position().get_y() - 5 == food.get_position().get_y():
            if head_one.get_position().get_x() == food.get_position().get_x():
                points = food.get_points()
                score_one.add_points(points)
                print(f'Head: {head_one.get_position().get_y()} Food: {food.get_position().get_y()}')
                food.reset()

        if head_two.get_position().get_y() + 5 == food.get_position().get_y() or head_two.get_position().get_y() - 5 == food.get_position().get_y():
            if head_two.get_position().get_x() == food.get_position().get_x():
                points = food.get_points()
                score_two.add_points(points)
                food.reset()
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snake_one = cast.get_actor("snakes", 0)
        snake_two = cast.get_actor("snakes", 1)
        head_one = snake_one.get_segments()[0]
        head_two = snake_two.get_segments()[0]
        segments_one = snake_one.get_segments()[1:]
        segments_two = snake_two.get_segments()[1:]
        
        for segment in segments_two:
            if head_one.get_position().equals(segment.get_position()):
                self._is_game_over = True

        for segment in segments_one:
            if head_two.get_position().equals(segment.get_position()):
                self._is_game_over = True
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            snake_one = cast.get_actor("snakes", 0)
            snake_two = cast.get_actor("snakes", 1)
            segments_one = snake_one.get_segments()[1:]
            segments_two = snake_two.get_segments()[1:]
            head_one = snake_one.get_segments()[0]
            head_two = snake_two.get_segments()[0]
            food = cast.get_actor("foods", 0)

            snake_one.kill_snake()
            snake_two.kill_snake()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            head_one.set_color(constants.WHITE)
            for segment in segments_one:
                segment.set_color(constants.WHITE)

            head_two.set_color(constants.WHITE)
            for segment in segments_two:
                segment.set_color(constants.WHITE)
            food.set_color(constants.WHITE)