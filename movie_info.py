
class Movie_info(object): 
	def __init__(self, director="",release_year="",title="",actor_1="",actor_2="",location=""):
		self.director=director 
		self.release_year=release_year
		self.title=title 
		self.actor_1=actor_1
		self.actor_2=actor_2
		self.location=location 

movie1 = Movie_info("James Cameron", "1999", "Titanic", "Leonardo DiCaprio", "Kate Winslet", "Atlantic Ocean")

print movie1.__dict__

