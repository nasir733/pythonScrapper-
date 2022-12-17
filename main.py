from requests import get 
from bs4 import BeautifulSoup

MAX_PAGE_SIZE = 365
page_size =1

base_url = f'https://www.realtor.com/realestateagents/fort-lauderdale_fl/pg-'



def extract_relator(html):
    data={}
    agentExperience=''
    agentGroup=''

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
    
    if title is not None: 

        if title.string is not None:
            title = title.string.replace(',','')
    
    if phone_number is not None: 
    
        if phone_number.string is not None:
            phone_number = phone_number.string.replace(',','')
    if sold_count is not None : 
        if sold_count.string is not None:
            sold_count = sold_count.string.replace(',','')
    if sale_sold_cound:
        if sale_sold_cound.string is not None:
         sale_sold_cound = sale_sold_cound.string.replace(',','')


    

    data.update({
        'title':title if title else "",
        'phoneNumber':phone_number if phone_number else " ",
        'soldCount':sold_count if sold_count else " ",
        'saleSoldCount':sale_sold_cound if sale_sold_cound else " ",
        'agentExper':agentExperience if agentExperience else " ",
        'agentGroup':agentGroup if agentGroup else " "

    })

    return data 
 

    
    



def extract_relators():
    results =list() # array in javascript and list in python  ['','']
    # file = open('test.csv','w')
    # file.write('title,phoneNumber,soldCount,saleSoldCount,agentExper,agentGroup\n')
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept-Encoding": "*",
    "Connection": "keep-alive"
}
    with open('test2.csv', "w", encoding="utf-8") as file:      
        file.write('title,phoneNumber,soldCount,saleSoldCount,agentExper,agentGroup\n')  
        for i in range(MAX_PAGE_SIZE):
            print(f'scrapping page {i} .....')
            response = get(f'{base_url}{i}',headers=headers)
            # `${asd}` this is in js and f'{}' is in python   
            print(response.status_code)

            if response.status_code != 200: 
                print('Cant Request the web page ')
            else :
                soup=BeautifulSoup(response.text,"html.parser")
                cards = soup.find_all("div",class_="agent-list-card")
       

                local_result =[]       
                for card in cards: 
      
                    relaters_data = extract_relator(card)
    
                    local_result.append(relaters_data)
                for result in local_result :                     
                        file.write(f"{result['title']},{result['phoneNumber']},{result['soldCount']},{result['saleSoldCount']},{result['agentExper']},{result['agentGroup']}\n")

           
            
                print(f'scraping page {i} is done')
    
 

    print(results)
   
    # file.close()

         


          




extract_relators()