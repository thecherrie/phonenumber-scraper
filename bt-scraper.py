import requests
import urllib.request
import time
from bs4 import BeautifulSoup


vowels = ['A','E','H','I','L','O','R','U','Y']
# consonants = ['B','C','D']
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def is_vowel(letter):
    for vowel in vowels:
        if letter == vowel:
            return True 
    return False

def find_numbers(city, street):
    combos = []
    for i, letter in enumerate(alphabet):
        for secondLetter in alphabet:
            if not is_vowel(secondLetter) and not is_vowel(letter):
                continue
            if is_vowel(secondLetter) and is_vowel(letter):
                continue
            else:
                combos.append([letter, secondLetter])


    with open('nums.txt', 'w') as file:

        for i in range(len(combos)):
            print(combos[i][0],combos[i][1])

            url = "https://www.thephonebook.bt.com/Person/PersonSearch/?Surname="+combos[i][0]+combos[i][1]+"&Location="+city+"&Street="+street
            response = requests.get(url)

            soup = BeautifulSoup(response.text, "html.parser")

            name = soup.find_all("div", class_="col-12 py-2")
            # number = soup.find_all("a", class_="no-hover")
            dataSets = soup.find_all('div', {'class' :'mb-3 border border-dark px-3'})

            for dataSet in dataSets:
                names = dataSet.find_all('span', {'class': 'black medium'})
                for name in names:
                    file.write("["+combos[i][0]+","+combos[i][1]+"]  "+name.text.replace('\n',''))
                    # data.append(name.text.replace('\n',''))

                numbers = dataSet.find_all('a', {'class': 'no-hover'})
                for number in numbers: 
                    file.write(number.text[0:18].replace('\n', '') + "-")
                    # data.append(number.text[0:18].replace('\n', ''))

            # print(data)

entered_city = input("Enter city: ")
entered_street = input("Enter Street: ")
find_numbers(entered_city, entered_street)

