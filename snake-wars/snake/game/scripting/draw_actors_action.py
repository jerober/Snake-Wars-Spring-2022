from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        scores = cast.get_actors("scores")
        food = cast.get_actor("foods", 0)
        snake_one = cast.get_actor("snakes", 0)
        segments_one = snake_one.get_segments()
        snake_two = cast.get_actor("snakes", 1)
        segments_two = snake_two.get_segments()
        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        self._video_service.draw_actor(food)
        self._video_service.draw_actors(segments_one)
        self._video_service.draw_actors(segments_two)
        self._video_service.draw_actors(scores)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()