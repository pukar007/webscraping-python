#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import requests
from bs4 import BeautifulSoup
import datetime
from tabula import read_pdf
from tabulate import tabulate


# In[4]:


root_url = 'https://www.everestbankltd.com'
page_url = root_url + '/supports/interest-and-rates/fees-and-services"' 


# In[5]:


r =requests.get(page_url)
content = r.content


# In[6]:



soup = BeautifulSoup(r.content,"html.parser")
print(soup.prettify())


# In[ ]:





# In[11]:


body = soup.find_all ("div", {"class":"card-body"})
body
  


# In[12]:


rows = soup.find_all('tr')
print(rows[:120])


# In[13]:


for row in rows:
    
    row_td = row.find_all('td')
    row_th = row.find_all('th')
print(row_td)
print(row_th)
type(row_td)
type(row_th)


# In[14]:


str_cells = str(row_td)
cleantext = BeautifulSoup(str_cells, "lxml").get_text()
print(cleantext)


# In[15]:


import re

list_rows = []
for row in rows:
    cells = row.find_all('td')
    str_cells = str(cells)
    clean = re.compile('<.*?>')
    clean2 = (re.sub(clean, '',str_cells))
    list_rows.append(clean2)
print(clean2)
type(clean2)


# In[16]:


df = pd.DataFrame(list_rows)
df.head(110)


# In[17]:


df1 = df[0].str.split(',', expand=True)
df1.head(110)


# In[28]:


df1[0] = df1[0].str.strip('[')
df1[1] = df1[0].str.strip(']')
df1[3] = df1[3].str.strip(']')
df1.head(110)


# In[31]:


df2 = pd.DataFrame(df1)

writer =pd.ExcelWriter("/home/hendrix/Desktop/everestbank.xlsx", engine='xlsxwriter')

df2.to_excel(writer,sheet_name='sheet1')

writer.save()




# In[ ]:


#def save_to_csv(df1):
#    print('df1')
 #   with open('/home/hendrix/Desktop/list.csv', 'w', newline='') as fp:
  #     a = csv.writer( df1, delimiter = ',' '[')
   #     #a.writerow(['list_row'])
#a.writerows(df1)


# In[47]:


#IF DATA IN IMAGE FORMAT 

# CONVERT IMAGE TO PDF AND SAVE

import img2pdf
from PIL import Image 
import os 
  
# storing image path 
img_path = "/home/hendrix/Desktop/nb.jpg"
  
# storing pdf path 
pdf_path = "/home/hendrix/Desktop/nb.pdf"
  
# opening image 
image = Image.open(img_path) 
  
# converting into chunks using img2pdf 
pdf_bytes = img2pdf.convert(image.filename) 
  
# opening or creating pdf file 
file = open(pdf_path, "wb") 
  
# writing pdf files with chunks 
file.write(pdf_bytes) 
  
# closing image file 
image.close() 
  
# closing pdf file 
file.close() 
  
# output 
print("Successfully made pdf file") 


# In[ ]:


#for image


# In[36]:


from PIL import Image
import pytesseract

Image.open("/home/hendrix/Desktop/nb.jpg")

pytesseract.image_to_string(Image.open("/home/hendrix/Desktop/nb.jpg"))


# In[ ]:





# In[ ]:





# In[ ]:




