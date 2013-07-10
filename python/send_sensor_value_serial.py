# -*- coding: utf-8 -*-
#!/usr/bin/env python

import urllib2
import urllib
import serial
import time
import sys
import datetime

ser = serial.Serial(
    port='/dev/tty.xxx',
    baudrate=9600,
    timeout=1
)

def main():
    try:
        host = 'xxx'
        while True:
            if ser.inWaiting() > 0:
                data = ser.readline().rstrip()
                #data_list = data.split(',')
                #id = data_list[0]
                id = 1
                thermo = float(data)
                #hygro = float(data_list[2])
                date = datetime.datetime.today().strftime('%Y/%m/%d %H:%M:%S')
                
                #print date, id, thermo, hygro
                print date, id, thermo
                
                params = urllib.urlencode({
                    'id' : id,
                    'thermo' : thermo
                    #'hygro' : hygro
                })
                
                # サーバに送信
                res = urllib2.urlopen(host, params)

                # 送信に失敗した場合
                if res.code != 200:
                    print res.code, res.msg
            
            time.sleep(0.1)
    except KeyboardInterrupt:
        print u'キーボード処理により停止します。'
    except urllib2.HTTPError, e:
        print e.code, e.msg
    except urllib2.URLError, e:
        print e
    finally:
        if ser != None:
            ser.close()

if __name__ == '__main__':
    main()