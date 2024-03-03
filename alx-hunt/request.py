import json
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

# Include the CSRF token in the login datao
login_data['authenticity_token'] = csrf_token

# Now you can send the POST request with the login data
login_response = session.post(login_url, data=login_data, allow_redirects=True, headers={
                              'Referer': 'https://intranet.alxswe.com/'})
# Check if login was successful (you may need to customize this based on the website's response)
if login_response.ok:
    # print("Login successful")

    response = session.get('https://intranet.alxswe.com')

    project_page = session.get('https://intranet.alxswe.com/projects/299')

    # print(project_page.content.decode("UTF-8"))

    with open('alx.json', 'r') as alxjs:
        ids_from_js = json.load(alxjs)
        pure_projects_ids = list(ids_from_js.keys())

        # Remove 'current' from the list
        if 'current' in pure_projects_ids:
            pure_projects_ids.remove('current')

        print(pure_projects_ids)

# ----------------- get projects ids and store it in json file ---------------
    # projects_page = session.get('https://intranet.alxswe.com/projects/current')
    # # Get the content of the response
    # content = response.content

    # # Write the content to a file
    # # with open('alx.html', 'wb') as f:
    # #     f.write(content)

    # # Assume content is the HTML content you've fetched
    # soup = BeautifulSoup(content, 'html.parser')

    # # Find all anchor tags with hrefs that start with "/projects/"
    # project_tags = soup.find_all(
    #     'a', href=lambda href: href and href.startswith('/projects/'))

    # # Extract the project IDs and names from the hrefs
    # project_info = {(tag['href'].split('/')[-1], tag.text)
    #                 for tag in project_tags}

    # # print(project_info)

    # with open('alx.json', 'w') as file:
    #     json.dump(dict(project_info), file, indent=3)
# ----------------- get projects ids and store it in json file ---------------
