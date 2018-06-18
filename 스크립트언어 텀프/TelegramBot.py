import telepot
import time
import threading

#파싱용
import urllib.request
import string
import codecs
import smtplib
from xml.dom.minidom import *

# API공유키
global key
key = "ESfoqLgZIPMdxDVdj9b%2FHG4IM%2FxzY2rgg0bcScQR2HZAI7wpwnBxf10VBUMdNIch2HrhKzD%2FCgOEzg400RDeAw%3D%3D"

# Telegram API
global bot

#메뉴검색해 휴게소 메뉴가져오기함수
def getList():
    global AllmenuList
    global AllrestList
    global AllrestList2
    global AllmenuList2
    AllmenuList = []
    AllrestList = []
    AllrestList2 = []
    AllmenuList2 = []
    # 1~10 까지 한 이유는 xml 에서 2100개가 있고 999개 까지만 검색이 되므로
    for i in range(1, 10):
        print(i)
        # OpenAPI를 불러와서 String으로 넣어준다.  i는 페이지 수
        getParsingXMLString = openAPItoXML("http://data.ex.co.kr/exopenapi/restinfo/restBestfoodList?serviceKey=",
                                           "&pageNo=" + str(i) + "&numOfRows=999&pageSize=999&type=xml")
        getParsingXMLString2 = openAPItoXML("http://data.ex.co.kr/exopenapi/restinfo/restBestfoodList?serviceKey=",
                                            "&pageNo=" + str(i) + "&numOfRows=999&pageSize=999&type=xml")
        # XML Mother, Child 를 가져와서 List에 넣어준다.
        menuList = addParsingDicList(getParsingXMLString, "list", "foodNm")
        restList = addParsingDicList(getParsingXMLString, "list", "stdRestNm")
        restList2 = addParsingDicList(getParsingXMLString2, "list", "stdRestNm")
        menuList2 = addParsingDicList(getParsingXMLString2, "list", "foodNm")

        # 각 가져온 List를 전체 List로 넣어준다.
        AllmenuList = AllmenuList + menuList
        AllrestList = AllrestList + restList
        AllrestList2 = AllrestList2 + restList2
        AllmenuList2 = AllmenuList2 + menuList2

# 파시을 편하게 하기 위하여 Open APi 주소를 넣어서 Stirng 데이터로 넣어줌.
def openAPItoXML(server, value):
    global key
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')]
    # ↑ User-Agent를 입력하지 않을경우 naver.com 에서 정상적인 접근이 아닌것으로 판단하여 차단을 한다.
    data = ""
    urldata = server + key + value
    with opener.open(urldata) as f:
        data = f.read(300000).decode('utf-8') # 300000bytes 를 utf-8로 변환하여 읽어온다.  변환이 없을경우 unicode로 받아온다.
    return data

def addParsingDicList(xmlData, motherData, childData):
    # 파싱된 데이터를 리스트에 넣어서 리턴 한다.
    doc = parseString(xmlData)
    siGunGuList = doc.getElementsByTagName(motherData)
    signguCdSize = len(siGunGuList)
    list = []
    for index in range(signguCdSize):
        mphms = siGunGuList[index].getElementsByTagName(childData)
        list.append(str(mphms[0].firstChild.data))
    return list

def handle(msg):
    global bot
    global RenderList2
    global AllmenuList

    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text':
        bot.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
        return

    text = msg['text']
    strText = ""
    strText = text

    if strText.find("메뉴") != -1:
        # 메뉴로 검색 합니다.
        strText = strText.replace("메뉴 ", "")
        strText = strText.replace("메뉴", "")
        resultText = ""
        number = 0
        for name in AllmenuList:
            number = number + 1
            if(name.find(strText) != -1 and number < len(AllmenuList)):
                resultText = resultText + AllrestList[number].replace("휴게소", "") + " : " + name + "\n"
        bot.sendMessage(chat_id, '입력 단어 : ' + strText + '\n\n' + resultText)
    elif strText.find("휴게소") != -1:
        strText = strText.replace("휴게소 ", "")
        strText = strText.replace("휴게소", "")
        resultText = ""
        number2 = 0
        for name2 in AllrestList2:
            number2 = number2 + 1
            if(name2.find(strText) != -1):
                resultText = resultText + AllmenuList2[number2].replace("메뉴", "") + " : " + name2 + "\n"
        bot.sendMessage(chat_id, '입력 단어 : ' + strText + '\n\n' + resultText)
    else:
        bot.sendMessage(chat_id, '메뉴, 휴게소 입력후 내용을 입력해 주세요..!')
        pass
    

getList()
bot = telepot.Bot('564671951:AAENJ7W55otzTDgVzOFL6vS9i0idE3l4Kdk')
bot.getMe()

bot.message_loop(handle)

while 1:
    time.sleep(10)