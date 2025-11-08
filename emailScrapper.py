import re
import httpx
from bs4 import BeautifulSoup

# Define the target URL
target_url = str(input("Enter the web address: "))  # Replace with your target website
# target_url = "https://eportal.oauife.edu.ng/contact.php"  # Replace with your target website

# Send an HTTP request
response = httpx.get(target_url)
page_html = response.text

# Use regex to find email addresses
email_pattern = re.compile(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})')
email_matches = re.findall(email_pattern, page_html)

# Store emails in a text file
file_names = ["emails.txt", "emails.json", "emails.csv"]
for file_name in file_names:
    with open(file_name, "w") as file:
        for email in email_matches:
            file.write(email + "\n")

print(f"Extracted {len(email_matches)} emails and saved them in 'emails.txt'.")

