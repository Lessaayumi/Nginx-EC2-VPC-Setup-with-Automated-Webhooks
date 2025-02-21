import requests

#tenho a url do servidor que criei
WEBHOOK_URL = "https://discordapp.com/api/webhooks/1339647118004191348/cTE7JOOgK1qc51TYIsvohT50arXOhSShIr43x1xlwNrJJiRUjrpXdvh-YGCdEk2Yymzj"

# Vou ter um alerta caso o nginx não estaja funcionando

def send_alert(message):
    requests.post(WEBHOOK_URL, json={"content": message})

def check_site(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print("Site is alive!")
        else:send_alert(f"⚠ Site {url} returned status code: {response.status_code}")
    except:
        send_alert(f"❌ Site {url} is down!")

#ip publico que o nginx está rodando  check_site('http://3.89.92.220:80')