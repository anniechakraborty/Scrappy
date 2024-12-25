import requests
import webbrowser
import os
from bs4 import BeautifulSoup

url = input('Please enter the url to parse : ').strip()
response = requests.get(url)
try:    
    if response.status_code == 200:
        print("Successfully accessed the website!")
    else:
        print(f"Failed to access the website. Status code: {response.status_code}")
        exit()

    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    # Writing the soup content into an html file
    file_name = 'output/pageContent.html'
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(soup.prettify())

    # Opening the generated HTML file in a web browser
    file_path = os.path.abspath(file_name)
    webbrowser.open(f"file://{file_path}")

except Exception as e:
    print(f"An error occurred: {str(e)}")