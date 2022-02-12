import tweepy
from config import create_client
import json
import random

def randTroll():
    with open('bd.json', encoding='utf-8') as jsonFile:
        jsonObj = json.load(jsonFile)
        jsonFile.close
    numMsgRand = random.randint(0, len(jsonObj['tweet'])-1)
    return jsonObj['tweet'][numMsgRand]['message']
    
def main():
    client = create_client()
    troll = randTroll()
    print(troll)

if __name__ == "__main__":
    main()
