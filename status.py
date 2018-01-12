import vk, requests, time
session = vk.AuthSession("VkAppId", "login", "password", scope="friends,status,account,offline")
vk = vk.API(session)
def Steam_Status():
    response = requests.get("http://steamcommunity.com/id/SteamID/")
    parsed = response.content.decode('UTF-8')
    parsing = parsed.split()
    for i in parsing:
        print(i)
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
while True:
    time.sleep(15)
    Steam_Status()
    Blacklist_Get()
    getInfo = vk.account.getCounters()
    numMsgs = getInfo.get('messages')
    numGifts = getInfo.get('gifts')
    getFriends = vk.friends.get()
    numFriends = len(getFriends)
    CurrentTime = a = time.ctime(time.time())
    StatusFormatting = "📅 {0} | Человек в ЧС: {1} 🔥 | Входящих сообщений: {2} ✉ | Подарков: {3} 🎁 | Друзей: {4} 👬 | Steam: {5} 💻".format(curTime, Blacklist_Get(), numMsgs, numGifts, numFriends, Steam_Status())
    vk.status.set(text=setStatus)
