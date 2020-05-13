import time
import pandas as pd
import numpy as np

from selenium import webdriver
import appium
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# browser = webdriver.Chrome()
# 
# browser.get("https://www.att.com/availability/")
class DynamicXpath(object):
    time.sleep(2)
    ctr=0
    
    def make_attribute_col(self,x,attribute):
            #print(x)
            try:
               if (x.get_attribute(attribute))!= None and len((x.get_attribute(attribute)))>1:
            #print(x.get_attribute(attribute))
                   return x.get_attribute(attribute)
            except NoSuchElementException:  #spelling error making this code not work as expected
                self.write_test_file("hiii")
                return np.nan
    def write_test_file(self,text):	
         with open("test1.txt",'a+') as file:
             file.write(str(text)+"\n")		
    def get_web_elements(self,browser,ctr):
        li=[]
      
        
#         elem = browser.find_element_by_xpath("//hierarchy")
#     
#         no_of_pagedowns = 17
#     
#     
#     
#         while no_of_pagedowns:
#             elem.send_keys(Keys.PAGE_DOWN)
#             time.sleep(0.2)
#             no_of_pagedowns-=1
            
        import pandas as pd
        tags=['android.widget.FrameLayout','android.widget.LinearLayout','android.view.ViewGroup','android.widget.ImageView ','android.support.v7.widget.LinearLayoutCompat','android.view.View','android.widget.TextView','android.widget.RelativeLayout','android.widget.Button','android.widget.HorizontalScrollView']
        
        df=pd.DataFrame()
        
       # Tag and Webelement coloumns
        self.write_test_file("here11")
        for tag in tags:
             df=df.append(pd.DataFrame({'webelement':browser.find_elements_by_class_name(tag)}))
             
             for i in browser.find_elements_by_class_name(tag):
                 li.append(tag)
        self.write_test_file(df)         
        df.reset_index(inplace=True)       
        #Attribute coloumns
        self.write_test_file("here0")
        attributes=['class','id','innerHTML','innerText','name','value','data-qa','aria-label','aria-control','data-test-id','resource-id','accessibility_id']
        df['tags']=pd.DataFrame(li)
        
        for attribute in attributes:
            df[attribute] = df['webelement'].apply(lambda x: self.make_attribute_col(x,attribute))
        self.write_test_file("here1")
        #print(df)
        
        #selecting those rows which contains less than 3 na values (can be modified for better results)
        
        df1=df.loc[(df.isna().sum(axis=1)>2)]
        
        
        
        
        
        #selecting those rows where innerText len is less than 30 char  (can be modified for better results)
        #cleaned_df1=cleaned_df[cleaned_df.innerText.str.len()<50]
        
        df1['classxpath']='//'+df1['tags']+'['+'@'+'class'+'='+'"'+df1['class']+'"'+']'
        df1['idxpath']='//'+df1['tags']+'['+'@'+'id'+'='+'"'+df1['id']+'"'+']'
        df1['innerTextxpath']='//'+'*'+'[contains(text()'+','+'"'+df1['innerText']+'"'+')'+']'
        df1['aria-label_xpath']='//'+df1['tags']+'['+'@'+'aria-label'+'='+'"'+df1['aria-label']+'"'+']'
        
        
        df1.fillna(value='N/A',inplace=True)
        #selecting those rows where innerHTML len is less than 170 char  (can be modified for better results)
        cleaned_df1=df1[df1.innerHTML.str.len()< 170]
        export_excel=cleaned_df1.to_excel('WebScrapping'+str(ctr)+'.xlsx',engine='xlsxwriter')
        print(cleaned_df1.tail())
        self.write_test_file("here2")
        #Scrapping Exisitng Item
        
        #inner text value can modified.
       
        innerText='Checkout'
    
        #scrapExistingItem(innerText,ctr)
        print('cleaned_df3',scrapExistingItem(innerText,ctr,cleaned_df1))
        
        
        
        #Scraping New Item 
        #webelement=scrapExistingItem(innerText,ctr)
        
        #print('list_attributes+:',scrapNewItem(scrapExistingItem(innerText,ctr)))
        
     
        
    def scrapExistingItem(self,innerText,ctr,cleaned_df1):
        #print(pwd)
        #print('WebScrapping'+str(ctr)+'.xlsx')
        cleaned_df2=cleaned_df1
        #print('hik',cleaned_df2)
        cleaned_df3=cleaned_df2[cleaned_df2['aria-label']==innerText]
        print('df3',cleaned_df3)
        #print(cleaned_df3.iloc[0]['webelement'])
        webelement=cleaned_df3.iloc[0]['webelement']
        #return  webelement
        return (scrapNewItem(webelement))
    def scrapNewItem(self,webelement):
        list_attributes=[]
        attributes=['class','id','innerHTML','innerText','name','value','data-qa','aria-label','aria-control','data-test-id']
    
        for i in attributes:
            if webelement.get_attribute(i)!=None:
                print(i)
                list_attributes.append(i+':'+webelement.get_attribute(i))
            else:
    
                continue
        #print(list_attributes)               
        return(list_attributes)
    ctr+=1
# get_web_elements(browser,ctr)
# from   selenium import webdriver
# from   selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait
# 
# 
# print(browser.current_url)
# 
# #address = browser.find_element_by_xpath('//input[@aria-label=" Enter your address"]')
# #apartment = browser.find_element_by_id("")
# #zip = browser.find_element_by_id("")
# submit   = browser.find_element_by_xpath('//button[@id="checkout-button"]')
#   
# #address.send_keys("952 helix ave, 91911")
# #apartment.send_keys("2020")
# #zip.send_keys("75243")
# submit.click()
#   
# 
# wait = WebDriverWait( browser, 15 )
# '''
# try:
#     page_loaded = wait.until_not(
# lambda browser: browser.current_url == login_page
# )
# except TimeoutException:
#     self.fail( "Loading timeout expired" )
#   
#     self.assertEqual(
#     browser.current_url,
#     correct_page,
#     msg = "Successful Login"
#     )
#  
# '''
# a=[]
# for i in range (2,1000):
#     for j in range(2,i+1):
#         if(i!=i and j%i==0):
#             break
#         elif(j==i-1):
#             a.append(j)
#             
# for i in range (2,n/2):
#     if(j%i==0) and j:
#         
#             break
#         
#             			
# 			