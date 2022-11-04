import numpy as np

class GreeterBot():

    def __init__(self):
        return
        # pass


    def set_seed(self, id_seed):
        """
        Set the seed of NumPy's random number generator

        Args:
            - id_seed, int: seed to use in NumPy's random number generator
        """
        np.random.seed(id_seed)


    def get_greeting(self, greet_id=-1):
        """
        Method to get a greeting.

        Args:
            - greet_id, int: Numerical ID of the greeting to be returned. If not within the range
            (0, number of greetings) a random greeting is selected
        Returns:
            - greeting, string: the greeting text
        """

        greetings = ["Hi!", "Hello", "Heyy", "Bonjour"]
        num_greets = len(greetings)
        if greet_id not in range(0,num_greets):
            greet_id = np.random.randint(0,num_greets)
            print(np.random.randint(0,num_greets))
        greeting = greetings[greet_id]
        return greeting

    def get_info(self):
        """
        Provides more information about the class in the form of a video walkthrough
        """
        walkthrough_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        print(f'For more information on how to use this GreeterBot, watch the tutorial at {walkthrough_url}')