from requests import get
from env import API_KEY
from random import randint
import arabic_reshaper
from bidi.algorithm import get_display


def get_random_int_not_reapeated(min, max, list_int):
    while True:
        num = randint(min, max)
        if num not in list_int:
            return num


def GetListCommentFromYoutube(videoId, count):
    req = get(
        f"https://www.googleapis.com/youtube/v3/commentThreads?key={API_KEY}&textFormat=plainText&part=snippet&videoId={videoId}&maxResults=100")
    list_com = []
    for i in req.json()['items']:
        obj = {'profile': i["snippet"]["topLevelComment"]
               ["snippet"]["authorProfileImageUrl"], 'author': i["snippet"]["topLevelComment"]
               ["snippet"]["authorDisplayName"], 'text': i["snippet"]["topLevelComment"]["snippet"]["textDisplay"]}
        if(obj["author"] not in list_com):
            list_com.append(obj)
    if(count > len(list_com)):
        print("The number of comments is less than the number you requested")
    else:
        list_int = []
        for _ in range(count):
            gen_int = get_random_int_not_reapeated(
                0, len(list_com)-1, list_int)
            selected = list_com[gen_int]
            list_int.append(gen_int)
            reshaped_text = arabic_reshaper.reshape(selected["text"])
            reshaped_author = arabic_reshaper.reshape(selected["author"])
            selected["text"] = get_display(reshaped_text)
            selected["author"] = get_display(reshaped_author)

            print(
                f"\nUser : {selected['author']} \nComment : {selected['text']}\nImage Profile : {selected['profile']}")


print("""
 _    _      _                            _____                            
| |  | |    | |                          |_   _|                           
| |  | | ___| | ___ ___  _ __ ___   ___    | | ___                         
| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \   | |/ _ \                        
\  /\  /  __/ | (_| (_) | | | | | |  __/   | | (_) |                       
_\/  \/ \___|_|\___\___/|_|_|_| |_|\___|_  \_/\___/ _   _                  
\ \ / /         | |       | |          | |         | | | |                 
 \ V /___  _   _| |_ _   _| |__   ___  | |     ___ | |_| |_ ___ _ __ _   _ 
  \ // _ \| | | | __| | | | '_ \ / _ \ | |    / _ \| __| __/ _ \ '__| | | |
  | | (_) | |_| | |_| |_| | |_) |  __/ | |___| (_) | |_| ||  __/ |  | |_| |
 _\_/\___/ \__,_|\__|\__,_|_.__/ \___| \_____/\___/ \__|\__\___|_|   \__, |
/  __ \                                    | |                        __/ |
| /  \/ ___  _ __ ___  _ __ ___   ___ _ __ | |_                      |___/ 
| |    / _ \| '_ ` _ \| '_ ` _ \ / _ \ '_ \| __|                           
| \__/\ (_) | | | | | | | | | | |  __/ | | | |_                            
 \____/\___/|_| |_| |_|_| |_| |_|\___|_| |_|\__|                           
                                                                     
                                                                           
""")


if(__name__ == "__main__"):
    try:
        VidId = input("Enter Youtube Video ID : ")
        count = int(input("Enter Count Comment : "))
        GetListCommentFromYoutube(VidId, count)
    except KeyboardInterrupt:
        print("\nExiting...")
