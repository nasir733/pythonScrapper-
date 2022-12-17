from requests import get 
from bs4 import BeautifulSoup

MAX_PAGE_SIZE = 1
page_size =1

base_url = f'https://www.realtor.com/realestateagents/fort-lauderdale_fl/pg-'



def extract_relator(html):
    data={}
    agentExperience=''
    agentGroup=''
    
    soup = html.find('ul')
    title = html.find('div',class_="agent-name")
    phone_number = html.find('div',class_="agent-phone")
    sold_count = html.find('span',class_='sale-sold-count')
    sale_sold_cound = html.find('span',class_='sale-sold-count')
    agent_experience_soup = html.find('div',{'id':'agentExperience',})
    agent_group_soup = html.find('div',{'class':'agent-group'})
    if agent_experience_soup:
        agentExperience = agent_experience_soup.find('span').string
    if agent_group_soup:
        agentGroup = html.find('span').string

    data.update({
        'title':title.string,
        'phoneNumber':phone_number.string,
        'soldCount':sold_count.string,
        'saleSoldCount':sale_sold_cound.string,
        'agentExper':agentExperience,
        'agentGroup':agentGroup

    })
    return data 
 

    
    



def extract_relators():
    for i in range(MAX_PAGE_SIZE):
        response = get(f'{base_url}{i}')  

        if response.status_code != 200: 
            print('Cant Request the web page ')
        else :
            soup=BeautifulSoup(response.text,"html.parser")
            results =soup.find("div",{"class":"cardWrapper"})
            unorderdlist = results.find('ul')

            cards = soup.find_all("div",class_="agent-list-card")
            file = open('test.csv','wiviialkj')
            file.write('title,phoneNumber,soldCount,agentExper,agentGroup')


            for card in cards: 
      
                extract_relator(card)

          




extract_relators()