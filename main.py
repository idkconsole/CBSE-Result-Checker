import requests
from bs4 import BeautifulSoup
import time

def uwu():
    return time.strftime("%Y-%m-%d %H:%M:%S")

def check_results():
    url = "https://results.cbse.nic.in/"
    find = "Senior School (Class XII) Certificate Examination (Supplementary) Results 2024"
    attempt = 1
    while True:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            results = soup.find_all('a', string=lambda t: find in t if t else False)
            if results:
                print(f"{uwu()} | Attempt {attempt} | {find} Results are available:")
                for result in results:
                    print(f"Result Found: {result.text.strip()} - URL: {result['href']}")
                break
            else:
                print(f"{uwu()} | Attempt {attempt} | Results not available yet....")
            attempt += 1
        except requests.RequestException as e:
            print(f"{uwu()} | Attempt {attempt} | An error occurred: {e}")

if __name__ == "__main__":
    check_results()
