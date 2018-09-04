
from hashtag import Hashtag
from methods import get_data

myHashtags = ('lodz')
for element in myHashtags:
    newHashtag = Hashtag(element)
    request = get_data(newHashtag)
  #  result = put_dictionary(newHashtag)
  #  print_dictionary(result)