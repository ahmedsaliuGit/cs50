import emoji

response = requests.get("https://carpedm20.github.io/emoji/all.html?enableList=enable_list_alias")

print(response.json())
