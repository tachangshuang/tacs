# fileName: get_log.py
import logging.config
import logging


# 读取日志配置文件
def get_log():
    con_log = "../configs/log.conf"
    logging.config.fileConfig(con_log)
    log = logging.getLogger()
    return log
