import requests, os, time






try:
    os.system("tor HTTPTunnelPort 8000")

    ip = requests.get("https://api.ipify.org", proxies={"http": "http://localhost:8000", "https:": "https://localhost:8000"})
    print("\n"+ip.text+"\n")

    while True:
        time.sleep(5)
        os.system("killall -HUP tor")
except:
    pass
    os.system("killall tor")
    os.system("clear")


