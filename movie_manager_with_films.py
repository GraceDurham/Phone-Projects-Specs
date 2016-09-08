from urllib2 import urlopen 
from json import load 
from movie_info import *

movie_list=[]

def get_data():
	
	apiUrl = "https://data.sfgov.org/resource/yitu-d5am.json?"
	response = urlopen(apiUrl)
	json_obj = load(response)
	


	for movies in json_obj:
		director=movies["director"]
		release_year = movies["release_year"]
		title = movies["title"]
		actor_1 = movies["actor_1"]
		actor_2 = movies["actor_2"]
		location = movies["locations"]
	


# def movie_2002(json_obj):
# 	movie_list=[]
# 	for film in json_obj:
# 		if film["release_year"]=="2002": 
# 			title= film["title"] 
# 			if title not in movie_list:
# 				movie_list.append(title)
# 	movie_list.sort()
# 	return movie_list	

	for movie_info in json_obj:
		if "director" in movie_info:
			director = str(movie_info["director"].encode("utf8"))
		if "release_year" in movie_info:
			release_year=str(movie_info["director"].encode("utf8"))
		if "title" in movie_info:
			title=str(movie_info["title"].encode("utf8"))
		if "actor_1" in movie_info:
			actor_1=str(movie_info["actor_1"].encode("utf8"))
		if "actor_2" in movie_info:
			actor_2=str(movie_info["actor_2"].encode("utf8"))
		if "locations" in movie_info:
			locations=str(movie_info["locations"].encode("utf8"))


		new_movie=Movie_info(director=director,release_year=release, title=title, actor_1=actor_1, actor_2=actor_2,location=location)	
		movie_list.append(new_movie)

		response.close()
		return movie_list 			

def get_movie_info_by_year(year):
	movie_list_by_year =[]
	for info in movie_list:
		if info.release_year==year:
			movie_list_by_year.append(info)
	return movie_list_by_year

def get_release_year_list():
	year_list=[]
	for info in movie_list: 
		year_list.append(info.release_year)	

	unique_set =set(year_list)
	new_list=list(unique_set)	
	new_list.sort()
	return new_list			


# element=json_obj[0]		
# print element["release_year"]
# print element["title"]

def main():

	get_data()
	print get_release_year_list()
	print get_movie_info_by_year("1998")

	for info in movie_list:
		print "title - " + info.title
		print "director - " + info.director
		print "release year - " + info.release_year
		print "actor1 - " + info.actor_1
		print "actor2 - " + info.actor_2
		print "location - " + info.location
	#sf open data source: film location in sfapiUrl =
	# apiUrl = "https://data.sfgov.org/resource/yitu-d5am.json?"

	#open the apiUrl and assign data to variable
	# response = urlopen(apiUrl)

	# json_obj = load(response)

	# print json_obj[0]
	# print type (json_obj)


	# print movie_2002(json_obj)
	


if __name__ == '__main__':
	main()