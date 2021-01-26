import urllib3, requests
from bs4 import BeautifulSoup

def download(URL, fileName):
    with open(fileName, "wb") as f:
        r = requests.get(URL, verify=False)
        f.write(r.content)

def mediaLengthFormat(t):
    t = int(t) / 1000
    return "%02d:%02d" % (int(t/60), int(t%60))

def main():
    GET_MEDIA_URL = "https://res.wx.qq.com/voice/getvoice?mediaid="

    URL = input("Please input WeChat Offical Account Page URL (Like https://mp.weixin.qq.com/s/******): ")
    response = requests.get(URL)
    HTMLContent = response.content
    bs = BeautifulSoup(HTMLContent, "html.parser")
    print("Media_Name", "Play_Length", "Media_ID")
    for mpvoice in bs.find_all("mpvoice"):
        voiceName = mpvoice.get("name")
        voiceLength = mediaLengthFormat(mpvoice.get("play_length"))
        voiceID = mpvoice.get("voice_encode_fileid")
        print(voiceName, voiceLength, voiceID)
        download("%s%s" % (GET_MEDIA_URL, voiceID), voiceName + ".mp3")
    print("Download Finished!")

if __name__ == '__main__':
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    main()
