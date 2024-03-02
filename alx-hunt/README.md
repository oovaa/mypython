# ALX Login Script

This script allows you to log into the ALX website and retrieve the content of the user's homepage.

## Description

The script uses a Python `requests` Session to manage cookies and persist the login session across multiple requests. It first sends a GET request to the login page to retrieve the CSRF token, which is then included in the POST data for the login request. After a successful login, it sends a GET request to the homepage and saves the cookies into a JSON file.

## Installation

This script requires Python 3 and the following Python packages:

- `requests`
- `beautifulsoup4`

You can install these packages using pip:

```bash
pip install requests beautifulsoup4
```

## Usage
Before running the script, replace email and password in the login_data.sec dictionary with your ALX email and password.

To run the script, use the following command:

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
MIT

```
MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```