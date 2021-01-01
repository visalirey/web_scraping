import requests
import lxml.html
import csv
import pandas as pd
web_page=requests.get('https://www.faballey.com/grey-floral-bell-sleeve-skater-dress-83/prdt')
tree=lxml.html.fromstring(web_page.content)
##print(tree)
e_tree=tree.xpath('.//div[@class="prodRight"]')[0]
##print(e_tree)
product_name=e_tree.xpath('//h1[@itemprop="name"]/text()')
#print(product_name)
original_price=e_tree.xpath('//h4/span[@style="color:#fc6486"]/text()')
#print(original_price)
offer_price=e_tree.xpath('//h4/span[@style="text-decoration:line-through;color:#000"]/text()')
#print(offer_price)
off_percentage=e_tree.xpath('//h4/span[@style="font-size:11px;color:#000;float:right;margin:4px 0 0 10px"]/text()')
#print(off_percentage)
dress_code=e_tree.xpath('//p/span[@class="proSkuid"]/text()')
#print(dress_code)

data=[]
for info in zip(product_name,original_price,offer_price,off_percentage,dress_code):
    resp={}
    resp['product_name']=info[0]
    resp['original_price']=info[1]
    resp['offer_price']=info[2]
    resp['off_percentage']=info[3]
    resp['dress_code']=info[4]
    data.append(resp)
print(data)

df=pd.DataFrame(data,columns=['product_name','original_price','offer_price','off_percentage','dress_code'])
df.to_csv(r'C:\Users\adminpc\Desktop\pandas\tem.csv')
