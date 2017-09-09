#!/usr/bin/python3

# import sklearn as sk
import lxml.html as html
import pandas as pd

from functools import reduce

main_url = 'http://www.imdb.com/'
user_id = 'ur58625091'
list_name = 'ratings'
parsed_url = '{main_url}/user/{user_id}/{list_name}'.format(
	main_url=main_url,
	user_id=user_id,
	list_name=list_name)


class Movie:
	'Class for containing movie information'

	def __init__(self, node):
		'Read html node and contain general information'
		# do something with node
		self.name = node.\
			cssselect('.info > b > a')[0].text_content()

		try:
			self.year = int(node.\
				cssselect('.year_type')[0].text_content()[1:-1])
		except ValueError:
			self.year = -1

		self.rating = int(movie_node.\
			cssselect('.value')[0].text_content())

		self.description = node\
			.cssselect('.item_description')[0].text_content()

		self.cast = reduce(
			lambda a, b: a + b.text_content() + '\n',
			movie_node.cssselect('div ~ .secondary'), '')

		self.duration = 0

		self.link = ''

	def __str__(self):
		return "{name}({year}):\n{description}\nRating: {rating}/10".format(
			name=self.name,
			year=self.year,
			description=self.description,
			rating=self.rating)

	def __repr__(self):
		return self.__str__()


page = html.parse(parsed_url)
last_hundred_nodes = page.getroot().\
	find_class('list detail').\
	pop().\
	find_class('list_item')

for movie_node in last_hundred_nodes:
	print(
		'Number:',
		int(movie_node.cssselect('.number')[0].text_content()[:-1]),
		Movie(movie_node),
		'\n')
