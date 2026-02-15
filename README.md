# Lead Enrichment Scraper

A lightweight Python tool that enriches company leads by automatically scanning publicly available webpages for email addresses and phone numbers.

This script is designed for practical prospecting workflows. It crawls common contact pages for each company website in your dataset and extracts visible contact information using pattern matching. No guessing, no fabricated data, only publicly exposed information.

---

## ✨ Features

* Crawls common high-yield pages like `/contact`, `/contact-us`, and `/about`
* Extracts visible emails and phone numbers using regex
* Works directly with CSV lead exports
* Appends enrichment results into new columns
* Simple, dependency-light workflow

---

## ⚠️ Ethical Use Notice

This tool only extracts publicly available contact information. It does not bypass protections, scrape private databases, or infer hidden contacts.

Always follow:

* Website terms of service
* Local data privacy regulations
* Responsible outreach practices

You are responsible for how you use enriched data.

---

## 📦 Requirements

Python 3.8+

Install dependencies:

```bash
pip install requests beautifulsoup4 pandas
```

---

## 📁 Input Format

The script expects a CSV file containing at least:

```
Website
```

Example:

```
Company Name,Website
Acme Corp,https://acme.com
```

---

## 🚀 Usage

1. Place your CSV file in the project directory:

```
apollo-accounts-export.csv
```

2. Run the script:

```bash
python enrich.py
```

3. Output file:

```
enriched_leads.csv
```

New columns added:

* Enriched Emails
* Enriched Phones

---

## 🔍 How It Works

For each website:

1. Visits likely contact endpoints
2. Parses HTML content
3. Searches for:

   * email patterns
   * phone number formats
4. Aggregates results into your dataset

---

## 🧠 Limitations

* Only finds information that is publicly visible
* Does not validate email deliverability
* Some sites block automated requests
* Dynamic JavaScript-heavy pages may require advanced scraping

---

## 🛠 Possible Extensions

* Email validation pipeline
* LinkedIn/contact directory scraping
* n8n automation workflow
* Proxy rotation for scale
* Headless browser support

---

## 🤝 Contributions

Pull requests are welcome. Ideas for improving extraction accuracy or workflow automation are encouraged.

---

## 📜 License

MIT License. Use responsibly.

---

## 💡 Philosophy

Lead enrichment should be transparent, reproducible, and grounded in publicly accessible data. This tool focuses on practical automation without crossing ethical boundaries.

Happy building.
