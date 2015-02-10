
import fresh_tomatoes

class Movies(object):

  def __init__(self, title, poster_url, movie_link):
    """ Creates a Movies class. 
    @parameters:
    title: Type String.
    poster_url: Type String.
    movie_link: Type String.
    """
    
    self.title = title
    self.poster_image_url = poster_url
    self.trailer_youtube_url = movie_link


a = Movies('Cast Away',
           'http://upload.wikimedia.org/wikipedia/en/a/a7/Cast_away_film_poster.jpg',
           'https://www.youtube.com/watch?v=PJvosb4UCLs')

b = Movies("Good Will Huntung",
           'http://cdn.miramax.com/media/assets/726_GoodWillHunting_Catalog_Poster-BB_v2_Approved.png',
           'https://www.youtube.com/watch?v=WDcMUCpppVs')

c = Movies('A Long Kiss Goodnight',
           'http://ia.media-imdb.com/images/M/MV5BMTUxMTY5MDE0OF5BMl5BanBnXkFtZTcwMzU5NjgxMQ@@._V1_SX640_SY720_.jpg',
           'https://www.youtube.com/watch?v=oDuma1M09B0')

d = Movies('Human Stain',
           'http://upload.wikimedia.org/wikipedia/en/thumb/b/b6/HumanStainPoster.jpg/220px-HumanStainPoster.jpg',
           'https://www.youtube.com/watch?v=MjX8TWmUPE4')

if __name__ == '__main__':

  # A list of all the movies.
  movie_list = list((a,b,c,d))

  # Generates html page showing movie list with posters and trailer link.
  fresh_tomatoes.open_movies_page(movie_list)
