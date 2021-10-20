from multiprocessing import cpu_count

bind = "0.0.0.0:5000"
workers = cpu_count()*2 + 1
worker_class = "gevent"
worker_connections = 1000
reload = True