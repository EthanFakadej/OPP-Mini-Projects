class Movie:
    def __init__(self,title,rating):
        self.title = title
        # below is a non-public attribute
        self._rating = rating

    @property
    def rating(self): 
        return self._rating 
    
    @rating.setter
    def rating(self, new_rating):
        if 1.0 <= new_rating <= 5.0:
            self._rating = new_rating
        else: print("PLease enter a valid rating.")

my_movie = Movie("The Avenger (2012)", 2.7)
print(f"This movie has a rating of {my_movie.rating}, I think that it is overrated.")

my_movie.rating = 5.7
print(f"This movie has a current rating of {my_movie.rating}.")