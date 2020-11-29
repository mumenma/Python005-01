import logging
import time
from pathlib import *

# 编写一个函数, 当函数被调用时，将调用的时间记录在日志中, 日志文件的保存位置建议为：/var/log/python- 当前日期 /xxxx.log

def saveLog():
    fileName = "log/" + time.strftime("%Y-%m-%d",time.localtime()) + ".log"
    p = Path(fileName)
    p.parent.mkdir(exist_ok=True,parents=True)
    logging.basicConfig(filename=fileName,
                        level=logging.DEBUG,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        format='%(asctime)s %(name)-8s %(levelname)-8s [line: %(lineno)d] %(message)s'
                        )
    logging.debug(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    logging.debug("debug message")
    logging.info("info message")
    logging.warning("warning message")
    logging.error("error message")
    logging.critical("critical message")


if __name__ == '__main__':
    saveLog()