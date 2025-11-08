import re
import httpx
from bs4 import BeautifulSoup

# Define the target URL
target_url = str(input("Enter the web address: "))  # Replace with your target website
# target_url = "https://eportal.oauife.edu.ng/contact.php"  # Replace with your target website

# Send an HTTP request
response = httpx.get(target_url)
page_html = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(page_html, 'html.parser')

# Extract only visible text from the page
text = soup.get_text(separator=" ")

# Use regex to find email addresses
email_pattern = re.compile(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})')
email_matches = re.findall(email_pattern, text)

# Remove duplicates by converting the list to a set and back to a list
email_matches = list(set(email_matches))

# Store emails in a text file
file_names = ["emails.txt", "emails.json", "emails.csv"]
for file_name in file_names:
    with open(file_name, "w") as file:
        for email in email_matches:
            file.write(email + "\n")

print(f"Extracted {len(email_matches)} emails and saved them in 'emails.txt'.")
print("Saved results to emails.txt, emails.json, and emails.csv")
