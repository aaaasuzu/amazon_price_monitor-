import requests

WEBHOOK_URL = "https://discordapp.com/api/webhooks/1492204544116129802/kYYxx6we0y5frdGwCongnDXpUNE5121AF49_Bv6IZamoxlTPONm-5i_YS7RXF2z476or"

    #discord通知
def send_discord(name,price, url):

    data = {
        "embeds": [
            {
                "title":"価格が下がりました!",
                "description":f"{name}",
                "color": 5814783,
                "fields":[
                    {"name": "価格","value": f"{price}円","inline": True},
                    {"name": "リンク","value": url,"inline": False}
                ]
            }
        ]
    }
    response = requests.post(WEBHOOK_URL, json=data)

    if response.status_code == 204:

       print("Discord通知成功")
    else:
        print("Discord通知失敗,response.status_code")


