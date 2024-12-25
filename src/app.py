import requests
from bs4 import BeautifulSoup

# Step 1: Send an HTTP request to the website
url = "https://medium.com/spring-boot/building-a-reusable-spring-boot-kafka-messaging-system-with-avro-serialization-3c7bc430e888"
response = requests.get(url)

# Step 2: Check the HTTP response status
if response.status_code == 200:
    print("Successfully accessed the website!")
else:
    print(f"Failed to access the website. Status code: {response.status_code}")
    exit()

# Step 3: Parse the HTML content
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')
