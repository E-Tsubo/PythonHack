# -*- coding: utf-8 -*-

########################################################
# 2017/11/12
# Ver 0.1.0 初版作成

########################################################
# Standard Daemon Process Library
# https://www.python.org/dev/peps/pep-3143/

########################################################
# 参考資料:デーモンプログラムを作成するにあたって
# https://qiita.com/knoguchi/items/385fe91038760c856530

from daemon import DaemonContext
from lockfile.pidlockfile import PIDLockFile
import time
import datetime

def run():
    while(True):
        
        with open('./tmp/damond_test.txt', 'a') as f:
            f.write(datetime.datetime.now().isoformat() + '\n')
        time.sleep(5)
        

def main():

    with DaemonContext( pidfile = PIDLockFile('/tmp/daemond.pid'),
                        stderr  = open('/tmp/err_console.txt', 'w+') ):
        print "test"
        run()
    
if __name__ == '__main__':
    main()
