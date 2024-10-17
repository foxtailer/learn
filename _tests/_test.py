import re

text = "Email: example@example.com"

if re.search(r'\S+@\S+', text):
    print("Found email:")
