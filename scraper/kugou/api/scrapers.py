import json,random,datetime,re,os
import requests

basepath = os.path.abspath(os.path.dirname(__file__))

def getSongJson(filehash,albumid):
    default_url = "http://www.kugou.com/yy/index.php?r=play/getdata&hash={HASH}&_={TIMESTAMP}"
    current_timestamp = datetime.datetime.utcnow().timestamp() * 1000 # timstamp反回的是float型，酷狗用毫秒级的timestamp,所以要乘1000
    request_url = default_url.format(HASH=filehash,ALBUMID=albumid,TIMESTAMP=int(current_timestamp))
    print(request_url)
    data = requests.get(request_url)
    # writeToFile(data_json)
    # return play_url = data_json['data']['play_url']
    return data.json()

def songsearch(keyword="",page=1,pagesize=30,retry=3):

    song_list = []
    default_url = "http://songsearch.kugou.com/song_search_v2?callback={JQUERYRANDOM}_{TIMESTAMP}&keyword={KEYWORD}&page={PAGE}&pagesize={PAGESIZE}&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_={TIMESTAMP}"
    current_timestamp = datetime.datetime.utcnow().timestamp() * 1000 # timstamp反回的是float型，酷狗用毫秒级的timestamp,所以要乘1000

    jQueryRandom = "jQuery118512392571613747921"
    request_url = default_url.format(JQUERYRANDOM=jQueryRandom,TIMESTAMP=int(current_timestamp),KEYWORD=keyword,PAGESIZE=pagesize,PAGE=page)
    print("requesting : {0}".format(request_url))
    request = requests.get(request_url)

    if request.status_code == 200:
        return request.content.decode('utf-8')
    else:
        raise "RequestError"

    # return song_list

def getSongGenerator(data):
    from model import Song
    response = (re.search('"data.*}',data)).group(0)
    response = '{' + response
    data = json.loads(response)['data']
    for each in data['lists']:
        song_json = getSongJson(each['FileHash'],each['AlbumID'])
        this = Song(
            id=each['ID'],
            filename = each['FileName'],
            filehash = each['FileHash'],
            singername = each['SingerName'],
            albumid = each['AlbumID'],
            songname = each['SongName'],
            albumname = each['AlbumName'],
            play_url = song_json['data']['play_url'],
            lyrics = song_json['data']['lyrics'],
            img_url = song_json['data']['img'],
        )
        yield this

def writeToFile(data):

    print(basepath)
    filename = os.path.join(basepath,"songs.json")

    mode = 'ab+' # adding content into the end
    if not os.path.exists(filename):
        mode = 'xb' # x -- write the file only the file is not existed
    
    with open(filename,mode=mode) as f:
        f.write(bytes(data.encode('utf-8')))

if __name__ == '__main__':
    # fileDecoding()
    lst = songsearch(keyword='五月天',pagesize=5) # 可以自己调整的
    for each in getSongGenerator(lst):
        # each.save()
        print(each)
