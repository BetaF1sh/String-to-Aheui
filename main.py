inputStr = input("아희로 바꿀 문장을 입력하세요 : ")
curUNum = 0
resultStr = ""
TTh = 0
Tho = 0
Hun = 0
Ten = 0
One = 0

def firstNum(fnum):
    global resultStr
    if fnum == 0:
        resultStr += ""
    elif fnum == 1:
        resultStr += ""
    elif fnum == 2:
        resultStr += "박"
    elif fnum == 3:
        resultStr += "받"
    elif fnum == 4:
        resultStr += "밥"
    elif fnum == 5:
        resultStr += "밙"
    elif fnum == 6:
        resultStr += "밦"
    elif fnum == 7:
        resultStr += "밠"
    elif fnum == 8:
        resultStr += "밣"
    elif fnum == 9:
        resultStr += "밞"

for curChar in inputStr:
    curUNum = ord(curChar)
    TTh = int(curUNum / 10000)
    Tho = int((curUNum / 1000) % 10)
    Hun = int((curUNum / 100) % 10)
    Ten = int((curUNum / 10) % 10)
    One = int(curUNum % 10)

    global digit, plus
    digit = 5
    plus = [0] * 5
    for num in [TTh, Tho, Hun, Ten, One]:
        firstNum(num)
        if digit == 5:
            if num > 0:
                resultStr += "밙밚밙밚밥밤"
                if num < 2:
                    resultStr += "따따따따따"
                else:
                    resultStr += "따따따따따따"
                plus[0] = 1
        elif digit == 4:
            if num > 0:
                resultStr += "밙밚밙밣"
                if num < 2:
                    resultStr += "따따따"
                else:
                    resultStr += "따따따따"
                plus[1] = 1
        elif digit == 3:
            if num > 0:
                resultStr += "밙밚밤"
                if num < 2:
                    resultStr += "따따"
                else:
                    resultStr += "따따따"
                plus[2] = 1
        elif digit == 2:
            if num > 0:
                resultStr += "밙반"
                if num < 2:
                    resultStr += "따"
                else:
                    resultStr += "따따"
                plus[3] = 1
        elif digit == 1:
            resultStr += ""
            if num > 0:
                plus[4] = 1
            if num == 1:
                resultStr += "반밧나"
        digit -= 1

    plusCount = 0
    for i in range(0,5):
        plusCount += plus[i]
    if (plusCount == 0) or (plusCount == 1):
        resultStr += ""
    elif plusCount == 2:
        resultStr += "다"
    elif plusCount == 3:
        resultStr += "다다"
    elif plusCount == 4:
        resultStr += "다다다"
    elif plusCount == 5:
        resultStr += "다다다다"

    resultStr += "맣"
resultStr += "희"

print("아희코드 : " + resultStr)
