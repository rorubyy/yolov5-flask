import multiprocessing

bind = "0.0.0.0:5000"
# 启动的进程数
workers = multiprocessing.cpu_count()
