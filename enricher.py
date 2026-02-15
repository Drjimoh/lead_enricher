import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

EMAIL_REGEX = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
PHONE_REGEX = r"\+?\d[\d\s\-()]{7,}\d"

CONTACT_PATHS = ["", "/contact", "/contact-us", "/about"]

def extract_contacts(html):
    emails = set(re.findall(EMAIL_REGEX, html))
    phones = set(re.findall(PHONE_REGEX, html))
    return list(emails), list(phones)

def crawl_site(base_url):
    found_emails = set()
    found_phones = set()

    for path in CONTACT_PATHS:
        try:
            url = urljoin(base_url, path)
            r = requests.get(url, timeout=8)
            soup = BeautifulSoup(r.text, "html.parser")
            text = soup.get_text(" ")

            emails, phones = extract_contacts(text)
            found_emails.update(emails)
            found_phones.update(phones)

        except:
            continue

    return ", ".join(found_emails), ", ".join(found_phones)

df = pd.read_csv(r"C:\Users\waliu\Downloads\apollo-accounts-export.csv", delimiter=",")

emails_col = []
phones_col = []

for site in df["Website"]:
    if pd.isna(site):
        emails_col.append("")
        phones_col.append("")
        continue

    emails, phones = crawl_site(site)
    emails_col.append(emails)
    phones_col.append(phones)

df["Enriched Emails"] = emails_col
df["Enriched Phones"] = phones_col

df.to_csv("enriched_leads.csv", index=False)

print("Enrichment complete.")
