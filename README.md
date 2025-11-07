# Email Extractor

This is a simple Python script that extracts email addresses from a webpage provided by the user. It fetches the page content, searches for valid email patterns using Regular Expressions (Regex), and saves all found emails into three different file formats.

---

## 📌 How It Works

1. You enter the website URL you want to extract emails from.
2. The script sends an HTTP request to the site.
3. It scans the HTML content for email addresses.
4. It saves the extracted emails in:
   - `emails.txt`
   - `emails.json`
   - `emails.csv`
5. It prints the number of emails found.

---

## 🛠 Requirements

Install required dependencies:

```bash
pip install httpx beautifulsoup4
