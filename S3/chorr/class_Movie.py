# We create the class Movie, where our objects will be the movies extracted from the file with parser
class Movie:
    
    def __init__(self,title="emptyTitle",
                 director=["emptyDirector"],
                 cast = ["emptyCast"],
                 producer = ["emptyProducer"],
                 writer = ["emptyWriter"],
                 country = ["emptyCountry"],
                 language = ["emptyLanguage"],
                 year = "emptyYear",
                 genres = ["emptyGenres"],
                 votes = "emptyVotes",
                 rating = "emptyRating",
                 runtime = ["emptyRuntime"],
                 plot = ["emptyPlot"],
                 cover_url = "emptyCover"):
	
	"""The constructor will assign the characteristics of each movie to its attributes as an object"""
	self.title = title
	self.director = director
	self.cast = cast
	self.producer = producer
	self.writer = writer
	self.country = country
	self.language = language
	self.year = year
	self.genres = genres
	self.votes = votes
	self.rating = rating
	self.runtime = runtime
	self.plot = plot
	self.cover_url = cover_url
	
	# We define the get of title
    def GetTitle(self):
	return self.title