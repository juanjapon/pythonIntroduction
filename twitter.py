import re

url = input("URL: ").strip()

matches=re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(.+)$",url,re.IGNORECASE)

if matches:
    print(matches.group(1))


