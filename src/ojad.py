import geckodriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from time import sleep
import os
from bs4 import BeautifulSoup

#install webdriver if needed
geckodriver_autoinstaller.install()

#set options
#set webdriver to be headless(it means to make it invisble)
options = FirefoxOptions()
options.add_argument('-headless')
driver = webdriver.Firefox(options=options)

#this function downloads the pitch accent graph, 
#the pitch accent graphs are saved in the pitch_graph folder as png
def get_pitched_text(text,filename=None):
    if "pitch_graph" not in os.listdir():
        os.mkdir("pitch_graph")

    #remove html tags and &nbsp;
    text = BeautifulSoup(f"<div>{text}</div>", "html.parser" ).get_text().replace("\xa0","")

    if filename == None:
        filename = text
    if f"{filename}.png" in os.listdir("pitch_graph"):
        return f"{filename}.png"
    try:
        print("Getting graph from OJAD", text)
        driver.get("https://www.gavo.t.u-tokyo.ac.jp/ojad/phrasing")

        #putting text into the input field
        input_element = driver.find_element(By.ID,"PhrasingText")
        input_element.send_keys(text);

        #pressing the submit button and waiting for 5 seconds
        submit_button = driver.find_element(By.ID, "phrasing_submit_wrapper").find_element(By.TAG_NAME,"input")
        submit_button.click()
        sleep(5)

        #change css to remove unnecessery elements from page before making screenshot 
        driver.execute_script("""
            var styleElement = document.createElement('style');
            styleElement.innerText = `input{display:none;} font{display:none} select{display:none} *{padding:0; margin:0;} #phrasing_main{width:fit-content} .ds_t{display:none}`
            document.body.appendChild(styleElement);
            const elements = document.querySelectorAll('*');
            elements.forEach(element => {
              element.style.cssText = 'background-color:white';
            });
        """)
        #making a screenshot of the generated pitch accent graph
        driver.find_element(By.ID,"phrasing_main").screenshot(f"pitch_graph/{filename}.png")
        return f"{filename}.png"

    except Exception as e:
        print("Error: ", e)
