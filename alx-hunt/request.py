import requests
from bs4 import BeautifulSoup

# Your login credentials
with open('data.sec', 'r') as data:
    email = data.readline()
    password = data.readline().strip()


# URL for login
login_url = 'https://intranet.alxswe.com/auth/sign_in'

# Session to persist the login session
session = requests.Session()

# Perform login
login_data = {
    'user[email]': email,
    'user[password]': password
}
# Get the login page
login_page_response = session.get(login_url)

# Parse the HTML content
soup = BeautifulSoup(login_page_response.content, 'html.parser')

# Get the CSRF token
csrf_token = soup.find('meta', {'name': 'csrf-token'})['content']

# Include the CSRF token in the login data
login_data['authenticity_token'] = csrf_token

# Now you can send the POST request with the login data
login_response = session.post(login_url, data=login_data, allow_redirects=True)
# Check if login was successful (you may need to customize this based on the website's response)
if login_response.ok:
    # print("Login successful")

    print(login_response.content.decode('UTF-8'))

    # Now, parse the HTML content
    soup = BeautifulSoup(login_response.content, 'html.parser')

    # Check if the logout link is present
    logout_link = soup.find('a', href='/auth/sign_out')

    if logout_link:
        print("You are logged in!")
    else:
        print("You are not logged in.")
else:
    print(f"Login failed with status code {login_response.status_code}")
