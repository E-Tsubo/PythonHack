# -*- coding: utf-8 -*-

########################################################
# 2017/11/12
# Ver 0.1.0 初版作成

import os
import sys
import time

def run():
    while(True):
        time.sleep(5)
        print 'Daemon Running...'

def fork():
    pid = os.fork() # 子プロセスをfork

    if(pid > 0): # 親プロセスの場合はPIDが0より大きい
        f = open('/var/run/mydaemon/daemon_forkd.pid', 'w')
        f.write(str(pid)+"\n")
        f.close()

        sys.exit()
        
    if(pid == 0): # 子プロセスの場合はPIDが0
        run()

if __name__ == '__main__':
    fork()
