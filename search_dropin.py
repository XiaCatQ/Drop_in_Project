
import requests
from bs4 import BeautifulSoup

class BadmintonWeb:
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.3'}
        self.url = 'https://www.badmintontw.com/search.php?city=&area=&level%5B%5D='

    def key_words_search_words(self, user_message):
        words = user_message.split()[1:]
        keywords = '+'.join(words)
        search_words = ' '.join(words)
        return keywords, search_words

    def search(self, keywords):
        print(self.url+keywords)
        response = requests.get(self.url+keywords, headers = self.headers)
        content = response.content
        soup = BeautifulSoup(content, 'html.parser')
        result_links = soup.findAll('tr')
        
        day_link = set()
        for tr in result_links:
            text = tr.text.lower()
            if "小時" in text: 
                link2 = tr.find('a')
              
                day_link.add(link2)
                
                
#         print(link2)
        print(day_link)
        return day_link
      
    def send_link(self, day_link, search_words): 
        send_link = set()
        for link in day_link:
#             text = link.text.lower()
#             print(text)
#             if search_words in text:  
            send_link.add("https://www.badmintontw.com/" + link.get('href'))
        print(send_link)
        print("Finished!")
        return send_link
 
