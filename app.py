from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def train_status():

    url = "https://transit.yahoo.co.jp/traininfo/detail/20/0/"

    response = requests.get(
        url,
        headers={"User-Agent":"Mozilla/5.0"},
        timeout=10
    )

    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text()

    if "平常運転" in text:
        status = "平常運転"
    else:
        status = "運行情報確認中"

    return jsonify({
        "line":"宇都宮線",
        "status":status
    })

if __name__ == "__main__":
    app.run()