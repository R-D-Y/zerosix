Here is a README for the two scripts you provided:

---

# URL Finder Scripts

This repository contains two Python scripts designed to test random URL paths on a given base URL and report the results.

## Script 1: `url_to_discord.py`

This script generates random paths and checks if they exist on the specified base URL. If a valid URL is found, it sends a notification to a predefined Discord webhook.

### Features:
- **Random Path Generation:** Generates a random 6-character string to append to the base URL.
- **URL Checking:** Sends an HTTP GET request to the generated URL to check its validity.
- **Discord Notification:** If a valid URL is found, a message is sent to a Discord channel via a webhook.
- **Continuous Execution:** The script runs indefinitely, continuously generating and testing new URLs.

### Usage:
1. Set up your Discord webhook URL in the script.
2. Run the script, and it will notify you on Discord whenever a valid URL is found.

## Script 2: `url_checker.py`

This script is similar to the first one but does not send notifications to Discord. Instead, it simply prints the results to the console.

### Features:
- **Random Path Generation:** Generates random 6-character strings for URL testing.
- **URL Checking:** Tests each generated URL to see if it is valid.
- **Console Output:** Outputs the results directly to the console, indicating whether a valid URL was found or not.
- **Rate Limiting:** Includes a delay between requests to avoid overwhelming the target server.

### Usage:
1. Run the script, and it will continuously generate and check random URLs, printing the results to the console.

## Requirements
- Python 3.x
- `requests` library

You can install the necessary package using pip:

```bash
pip install requests
```

## Note
- Ensure that you have permission to test the URLs on the specified base URL.
- Be cautious with the frequency of requests to avoid being blocked by the server.

---

