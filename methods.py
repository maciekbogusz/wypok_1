'''
Created on 26.07.2017

@author: Maciek
'''
from lxml import html
import requests
import string

def response_check(page):
    if page.status_code >= 500:
        print ("Server error", page.status_code)
    elif page.status_code >= 400:
        print ("Cleint error ", page.status_code)     
    elif page.status_code >= 300:
        print ("Redirection", page.status_code)
    elif page.status_code >= 200:
        print ("OK", page.status_code)
    elif page.status_code >= 100:
        print ("Response", page.status_code)

def get_data(
    hashtag
    ):
    hashtag_str = str(hashtag) 
    lower_name = hashtag_str.lower()
    page = requests.get('https://www.wykop.pl/tag/wpisy/'+lower_name)
    response_check(page)   
     
    
# def put_dictionary(
#         stock
#         ):
#     name = stock.name
#     price = stock.getPrice() 
#     my_dictionary = [name, price]
#     return my_dictionary
#     
# def print_dictionary(
#             dictionary
#         ):    
#    # write_csv(dictionary)
#     print(dictionary)