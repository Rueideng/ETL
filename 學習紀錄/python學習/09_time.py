import  time
'''若無法輸入中文可打以下
import locale
locale.setlocale(locale.LC_CTYPE, 'chinese'
'''
unix_time=time.time()
loc_time=time.localtime()
utc_time=time.gmtime()
readable_time=time.asctime()


print('世界標準時間', unix_time)
print("本地時間",loc_time)
print("世界標準時間",utc_time)
print("可閱讀時間",readable_time)


#時間日期格式化範例
tmp_str=time.strftime("year%y, %m%d",loc_time)
print(tmp_str)
