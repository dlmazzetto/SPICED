"""Module Docstring:
   Order of things:
   1. imports
   2. CONSTANTS
   3. Classes
   4. Classless Functions
   5. if name == main statment

   Also: use pylint / black
"""

import random
# import constants
#this implies that there is a file called constants.py


class Recommender:
    """A Class to logically group all my recommendation functions.

       Analogy: Paragraph containing related sentences.

    """

    def __init__(self, items: list):
        self.items = items
        # design decision to pass the list as an argument here (during instantiation)

    def random_recommend(self, n: int = 3) -> list:  # type annotation
        """
        Function that returns n elements randomly from a given list.

        Arguments
        ----------
        items: list
        n : int

        Returns
        --------
        result: list
        """
        result = random.sample(self.items, k=n)
        result = [i.lower() for i in result]
        return result

    def nmf(self):
        """Coming in version 2.0!"""
        pass

    def cosim(self):
        """Coming in version 2.0!"""
        pass


if __name__ == "__main__":

    ITEMS = items = ["Movie A", "Movie B", "Movie C", "Movie D", "Movie E", "Movie F"]
    rec = Recommender(constants.items)
    result = rec.random_recommend(3)
    print(result)
