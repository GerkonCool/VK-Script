import vk, requests, time
session = vk.AuthSession("VkAppId", "login", "password", scope="friends,status,account,offline")
vk = vk.API(session)
def Steam_Status():
    response = requests.get("http://steamcommunity.com/id/SteamID/")
    parsed = response.content.decode('UTF-8')
    parsing = parsed.split()
    for i in parsing:
        if i == 'Online</div>':
            steamstat = "В сети"
            return steamstat
        elif i == 'Offline</div>':
            steamstat = "Не в сети."
            return steamstat
        elif i == 'In-Game</div>':
            steamstat = "В игре."
            return steamstat
def Blacklist_Get():
    getBan = vk.account.getBanned()
    del(getBan[0])
    return len(getBan)
def main():
    while True:
        try:
            time.sleep(60)
            Steam_Status()
            Blacklist_Get()
            getInfo = vk.account.getCounters()
            msg = getInfo.get('messages')
            gift = getInfo.get('gifts')
            getFriends = vk.friends.get()
            lenfriends = len(getFriends)
            setStatus = "Человек в ЧС: {0} 🔥 | Входящих сообщений: {1} ✉ | Подарков: {2} 🎁 | Друзей: {3} 👬 | Steam: {4} 💻".format(Blacklist_Get(), msg, gift, lenfriends, Steam_Status())
            vk.status.set(text=setStatus)
        except Exception as e:
            print("Catched: ", e)
            time.sleep(120)
            main()
main()
