import requests
from bs4 import BeautifulSoup
'''
This code Scrapes the titles of books reviewed from 
slate.com's book review page. It works with the page markup 
as of 2/3/2018. 
'''
#Set the URL of the page you wish to scrape
url = 'http://www.slate.com/topics/s/slate_book_review.html'

#Set the response from the page to a variable in this case resposne
#Note that the pages response has several attributes see documentation
#for details. http://docs.python-requests.org/en/master/user/quickstart/#make-a-request

response = requests.get(url)

#Pass the text of our response into beautiful soup to be parsed.

soup = BeautifulSoup(response.text, 'html.parser')
#Find all titles based on previous search of pages markup structure and pass them into a response set assigned to the variable titles

titles = soup.find_all('span', class_='hed')

#Take the set of responses and use get_text() to pass only the text into the varialble title_list. 
#Note this will be a list of string types. 

titles_list = [title.get_text() for title in titles]

#Now you have your list you can print it to console or write it to a file, or further parse it. 

print(titles_list)
