from flask import Flask, render_template, request, redirect
import threading
import time
from scraper import create_driver, get_price
from notifier import send_discord



app = Flask(__name__)

driver = create_driver()
products = []

# === 定期監視　===
def monitor():
    while True:
        for p in products:
            try :
                price = get_price(driver,p["url"])
                p["price"] = price

                price(f"{p['name']} : {price}円")

                if price <= p["target_price"] and not p["notified"]:
                    send_discord(p["name"], price,p["url"])
                    p["notified"] = True 

            except Exception as e:
                 print("エラー:", e)

        time.sleep(600)              
threading.Thread(target=monitor, daemon=True).start()

# ==== 画面====
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        url = request.form["url"]
        target_price = int(request.form["target_price"])

        price = get_price(driver, url)

        products.append({
            "name": name,
            "url": url,
            "price": price,
            "target_price": target_price,
            "notified": False
        })

        return redirect("/")

    return render_template("index.html", products=products)

if __name__ == "__main__":
    app.run(debug=True)