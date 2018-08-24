inputStr = input("아희로 바꿀 문장을 입력하세요 : ")
curUNum = 0
resultStr = ''

first = {2: '박', 3: '받', 4: '밥', 5: '밙', 6: '밦', 7: '밠', 8: '밣', 9: '밞'}
second = {5: ['밙밚밙밚밥밤', '따따따따따', '따따따따따따'], 4: ['밙밚밙밣', '따따따', '따따따따'], 3: ['밙밚밤', '따따', '따따따'], 2: ['밙반', '따', '따따']}
third = {0: '', 1: '', 2: '다', 3: '다다', 4: '다다다', 5: '다다다다'}

for curChar in inputStr:
    curUNum = ord(curChar)
    TTh = int(curUNum / 10000)
    Tho = int((curUNum / 1000) % 10)
    Hun = int((curUNum / 100) % 10)
    Ten = int((curUNum / 10) % 10)
    One = int(curUNum % 10)

    digit = 5
    plus = [0] * 5
    for num in [TTh, Tho, Hun, Ten, One]:
        resultStr = resultStr + first.get(num, '')

        if digit == 1:
            resultStr += ""
            if num > 0:
                plus[4] = 1
            if num == 1:
                resultStr = resultStr + "반밧나"
        
        elif digit > 1 and digit < 6:
            if num > 0:
                resultStr = resultStr + second.get(digit)[0]
                if num < 2:
                    resultStr = resultStr + second.get(digit)[1]
                else:
                    resultStr = resultStr + second.get(digit)[2]
                plus[5-digit] = 1
        digit = digit - 1

    plusCount = 0
    for i in range(0,5):
        plusCount = plusCount + plus[i]
    resultStr = resultStr + third.get(plusCount)

    resultStr = resultStr + "맣"
resultStr = resultStr + "희"

print("아희코드 : " + resultStr)
