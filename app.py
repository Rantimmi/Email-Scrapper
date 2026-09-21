from flask import Flask, render_template, request, send_file
import csv
import io
import json
import re
import httpx
from bs4 import BeautifulSoup

app = Flask(__name__)

EMAIL_RE = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")

@app.route("/", methods=["GET", "POST"])
def index():
    emails = []
    error = None
    url = ""

    if request.method == "POST":
        url = request.form.get("url", "").strip()

        if not url.startswith(("http://", "https://")):
            error = "Please enter a valid URL starting with http:// or https://."
        else:
            try:
                response = httpx.get(
                    url,
                    timeout=15,
                    follow_redirects=True,
                    headers={"User-Agent": "EmailScrapper/1.0"}
                )
                response.raise_for_status()

                soup = BeautifulSoup(response.text, "html.parser")
                text = soup.get_text(separator=" ")
                emails = sorted(set(EMAIL_RE.findall(text)))

            except httpx.HTTPError as exc:
                error = f"Could not fetch that website: {exc}"
            except Exception as exc:
                error = f"Something went wrong: {exc}"

    return render_template("index.html", emails=emails, error=error, url=url)

@app.route("/download/<file_type>", methods=["POST"])
def download(file_type):
    emails = request.form.getlist("emails")
    emails = sorted(set(emails))

    if not emails:
        return "No emails to download.", 400

    if file_type == "txt":
        content = "\n".join(emails)
        return send_file(
            io.BytesIO(content.encode()),
            as_attachment=True,
            download_name="emails.txt",
            mimetype="text/plain"
        )

    if file_type == "json":
        content = json.dumps(emails, indent=2)
        return send_file(
            io.BytesIO(content.encode()),
            as_attachment=True,
            download_name="emails.json",
            mimetype="application/json"
        )

    if file_type == "csv":
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["email"])
        writer.writerows([[email] for email in emails])
        return send_file(
            io.BytesIO(output.getvalue().encode()),
            as_attachment=True,
            download_name="emails.csv",
            mimetype="text/csv"
        )

    return "Unsupported file type.", 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
