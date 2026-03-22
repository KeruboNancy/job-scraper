import requests
from bs4 import BeautifulSoup
import csv

URL = "https://realpython.github.io/fake-jobs/"


def fetch_jobs(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def parse_jobs(html):
    soup = BeautifulSoup(html, "html.parser")
    jobs = []

    job_cards = soup.find_all("div", class_="card-content")

    for job in job_cards:
        title = job.find("h2", class_="title").text.strip()
        company = job.find("h3", class_="company").text.strip()
        link = job.find("a")["href"]

        jobs.append({
            "title": title,
            "company": company,
            "link": link
        })

    return jobs


def save_to_csv(jobs, filename="jobs.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Job Title", "Company", "Link"])

        for job in jobs:
            writer.writerow([job["title"], job["company"], job["link"]])


def main():
    html = fetch_jobs(URL)
    jobs = parse_jobs(html)
    save_to_csv(jobs)
    print(f"{len(jobs)} jobs saved to jobs.csv")


if __name__ == "__main__":
    main()
