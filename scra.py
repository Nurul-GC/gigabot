import sqlite3
import requests
from bs4 import BeautifulSoup as bs

def save_on_db(question, answer):
	conn = sqlite3.connect('quizdeomilhao.db')
	conn.execute('INSERT INTO quizdeomilhao(question,answer) VALUES(?,?)',(question,answer))
	conn.commit()
	conn.close()

def show():
	conn = sqlite3.connect('quizdeomilhao.db')
	cursor = conn.cursor()
	cursor = conn.execute('SELECT * FROM quizdeomilhao')
	for row in cursor:
		print(f"{row[0]} - {row[1]} \n {row[2]}")

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'}

url = "http://quizdomilhao.com.br/category/g8"

question_page = requests.get(url, headers = headers )
question_page.encoding = 'utf-8'

soup = bs(question_page.text, 'lxml')

ul = soup.find('ul', {'class':'square'})

li = ul.find_all('li')    
a = ul.find_all('a')

text_link = [[item.text, item2['href']] for item, item2 in zip(li,a)]

for item in text_link:
    question, link = item
    print(question)
    #print(link)
    answer_page = requests.get(link, headers=headers)
    answer_page.encoding = 'utf-8'
    soup = bs(answer_page.text, 'html.parser')
    ul = soup.find('ul', {'class':'square'})
    li = ul.find_all('li')  
    answer = [item.find('strong').text for item in li if item.find('strong')]
    answer= ''.join(answer).capitalize()
    save_on_db(question,answer)
    print(answer)
    print("Salvando...")

#show()