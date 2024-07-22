import requests
import html

def get_data():
    respons = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")

    data = [(html.unescape(item['question']), item["correct_answer"]) for item in eval(respons.text)["results"]]
    return data

