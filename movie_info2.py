from urllib2 import urlopen 
from json import load 
import movie_info *

def get_data():
	movies=[]
	for movies in json_obj:
		director=movies["director"]
		release_year = movies["release_year"]
		title = movies["title"]
		actor_1 = movies["actor_1"]
		actor_2 = movies["actor_2"]
		location = movies["locations"]
	


def movie_2002(json_obj):
	movie_list=[]
	for film in json_obj:
		if film["release_year"]=="2002": 
			title= film["title"] 
			if title not in movie_list:
				movie_list.append(title)
	movie_list.sort()
	return movie_list	


# element=json_obj[0]		
# print element["release_year"]
# print element["title"]

def main():
	#sf open data source: film location in sfapiUrl =
	apiUrl = "https://data.sfgov.org/resource/yitu-d5am.json?"

	#open the apiUrl and assign data to variable
	response = urlopen(apiUrl)

	json_obj = load(response)

	# print json_obj[0]
	# print type (json_obj)


	print movie_2002(json_obj)
	


if __name__ == '__main__':
	main()