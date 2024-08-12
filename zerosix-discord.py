import requests
import random
import string
import time

def generate_random_string(length=6):
    """Random string with 6 letters"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def send_to_discord(url):
    """Send to your discord URL"""
    webhook_url = "https://discord.com/api/webhooks/123456789"
    data = {"content": f"URL trouvé: {url}"}
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print("Message send, check discord")
    else:
        print("Sent message error")

def check_url(base_url, path, tested_urls):
    """Check if the url working"""
    if path in tested_urls:
        return  
    try:
        url = f"{base_url}{path}"
        response = requests.get(url)
        if "Not Found" not in response.text:  # Link found
            send_to_discord(url)  # Send it to discord
    except requests.exceptions.RequestException as e:
        print("Erreur de requête:", e)
    finally:
        tested_urls.add(path)  # stock url

def main():
    base_url = "https://s06.io/"
    tested_urls = set()  # keep url
    while True:
        random_path = generate_random_string()
        check_url(base_url, random_path, tested_urls)
        #time.sleep(0.01)  # Pas obligatoire

if __name__ == "__main__":
    main()
