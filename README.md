# Email Scrapper

A Flask web app that extracts publicly visible email addresses from a webpage.

## Features

- Enter a website URL in a browser
- Extract unique email addresses
- Download results as TXT, JSON, or CSV
- Responsive Tailwind CSS interface
- Ready for deployment on Render

## Run locally

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Windows:

```bash
venv\\Scripts\\activate
```

Then open http://127.0.0.1:5000

## Deploy

The repository includes `render.yaml` and a `Procfile`.

On Render, create a new Web Service from this GitHub repository. Render will install the requirements and start the app with Gunicorn.

## Note

Only scrape websites and collect contact information in ways permitted by the website's terms, applicable law, and privacy requirements.
