import requests
import random
import string
import time

def generate_random_string(length=6):
    """random chain de 6"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def check_url(base_url, path, tested_urls):
    """test url"""
    if path in tested_urls:
        return  
    try:
        url = f"{base_url}{path}"
        response = requests.get(url)
        if "Not Found" in response.text:
            print("Not working")
        else:
            print("Lien trouvé:", url)
    except requests.exceptions.RequestException as e:
        print("request casser:", e)
    finally:
        tested_urls.add(path)  # tej des urls used

def main():
    base_url = "https://s06.io/"
    tested_urls = set()  # traces anciens urls
    while True:
        random_path = generate_random_string()
        check_url(base_url, random_path, tested_urls)
        time.sleep(1)  # anti ddos

if __name__ == "__main__":
    main()
