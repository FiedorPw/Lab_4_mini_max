class Player:
    """A class that represents a player in a game"""
    def __init__(self, char: str, been_checked = False) -> None:
        """
        Initializes a player.

        Parameters:
            char: a single-character string to represent the player in textual representations of game state
        """
        self.been_checked = been_checked
        if len(char) != 1:
            raise ValueError('Character that represents player should be of length 1')

        self.char = char

    def __str__(self) -> str:
        """
        Returns:
            Printable text represenation of the game's state
        """
        return str(self.char)