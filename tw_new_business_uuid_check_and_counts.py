#台灣 統一編號 新規則可用數量計算(驗證函式可單獨使用) 
#舊規則為可被10整除，新規則為可被5整除
#詳情請見 財政部資訊中心公告 https://www.fia.gov.tw/singlehtml/3?cntId=c4d9cff38c8642ef8872774ee9987283
#我盡量把程式寫得平鋪直敘，這樣應該比較好理解
#Enjoy it! By 信賢Hsinken

import datetime

CHECK_RULE = "12121241"

def check_tw_buuid(buuid, checkbase):
    checksum = 0
    for i in range(8):
        num = int(buuid[i]) * int(CHECK_RULE[i])
        num_add = num % 10 + int(num / 10)
        #print(num_add)
        if int(num_add) < 10:
            checksum += num_add

    #print(checksum)
    if checksum % checkbase == 0:
        #print('OK', buuid)
        return 1
    elif (buuid[6] == '7') and ((checksum+1) % checkbase == 0):
        #print('+1 OK', buuid)
        return 1
    else:
        return 0

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    checkAry = range(99999999)
    count_old = 0
    count_new = 0
    start = datetime.datetime.now()
    #old 10整除
    for i in checkAry:
        check_buuid_str = str(i)
        check_buuid_str = check_buuid_str.zfill(8)
        #print(check_buuid_str)
        count_old += check_tw_buuid(check_buuid_str, 10)

    print('舊統一編號規則(10整除) 可用數：', count_old)
    end = datetime.datetime.now()
    print("執行時間：", end - start)

    start = datetime.datetime.now()
    #new 5整除
    for i in checkAry:
        check_buuid_str = str(i)
        check_buuid_str = check_buuid_str.zfill(8)
        #print(check_buuid_str)
        count_new += check_tw_buuid(check_buuid_str, 5)

    print('新統一編號規則(5整除) 可用數：', count_new)
    print('新/舊統一編號 可用比：', count_new / count_old)
    end = datetime.datetime.now()
    print("執行時間：", end - start)