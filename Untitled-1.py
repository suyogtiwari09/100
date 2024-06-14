class MovieReview:
    def __init__(self, movie, story, actors, music):
        self.movie_name = movie
        self.story_rating = story
        self.actor_rating = actors
        self.music_rating = music
        self.avg = int((self.story_rating + self.actor_rating + self.music_rating)/3)
        self.myrating = {
            "Movie Name" : self.movie_name,
            "Story rating": self.story_rating,
            "Actor Rating": self.actor_rating,
            "Music Rating": self.music_rating,
            "Avg Rating": self.avg
        }
    def add_movie_ratings(self, movie_list):
         movie_list.append(self.myrating)
  
  
    def avg_star_ratings(self, movie_list):
        for movie in movie_list:
            if(movie["Avg Rating"] == 1 ):
                print("Thanks for the response, You rated Movie with   *")
                print(movie)

            elif(movie["Avg Rating"] == 2 ):
                print("Thanks for the response, You rated Movie with   * * ")
                print(movie)

            elif(movie["Avg Rating"] == 3 ):
                print("Thanks for the response, You rated Movie with   * * *")
                print(movie)

            elif(movie["Avg Rating"] == 4 ):
                print("Thanks for the response, You rated Movie with   * * * *")
                print(movie)

            if(movie["Avg Rating"] == 5 ):
                print("Thanks for the response, You rated Movie with   * * * * *")
                print(movie)
    def add_movie_ratings(self,movie_list):
        movie_list.append(self.myrating)
    def get_star(self, movie_list):
        for movie in movie_list:
            if(movie["Avg Rating"]==1):
                print("thanks for the response, You rated Movie with *")
                print(movie)

            elif(movie["Avg rating"]==2):
                print("thanks for the response, You rated Movie with **")
                print(movie)

            else:
                print("thanks for the response, You rated Movie with ***")
                print(movie)
moviereviews=[]
review2 = MovieReview("Beautiful Sound", 5, 5, 5)
review2.add_movie_ratings(moviereviews)
review2.avg_star_ratings(moviereviews)
review1 = MovieReview ("Good Life", 1, 1, 3)
review1.add_movie_ratings(moviereviews)
review1.avg_star_ratings(moviereviews)
review3 = MovieReview("Smiley", 1, 1, 3)
review3.add_movie_ratings(moviereviews)
review3.avg_star_ratings(moviereviews)



