from datetime import datetime, timedelta
 
dateList = []
fn = r'PATH' #путь к файлу со списком студентов
with open(fn) as f:
    onstring = f.readlines()
    for line in onstring:
        for date in line:
            date = line[0:12]
            borndate = date[1:7]
            year = '20' + borndate[0:2]
            month = borndate[2:4]
            day = borndate[4:6]
        fullDate = datetime(*(map(int, (year, month, day))))
        dateList.append(fullDate)
        bigDate = max(dateList).date().strftime('%Y%m%d')
        smallDate = min(dateList).date().strftime('%Y%m%d')
        strBigDate = bigDate[2:8]
        strSmallDate = smallDate[2:8]
    print(onstring)
    print(strBigDate)
    print(strSmallDate)
    for guy in onstring:
        if strBigDate in guy:
            print("Самый старший", guy)
        elif strSmallDate in guy:
            print("Самый младший", guy)
