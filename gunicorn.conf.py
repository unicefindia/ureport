import os
import multiprocessing

current_path = os.path.dirname(os.path.abspath(__file__))
bind = '0.0.0.0:8000'
workers = multiprocessing.cpu_count() * 2
name = 'ureport'
env = 'DJANGO_SETTINGS_MODULE=ureport.settings'
proc_name = 'ureport'
default_proc_name = proc_name
chdir = current_path
python_path = ','.join([os.path.join(current_path, 'env'),])
loglevel = 'info'
accesslog = '/dev/stdout'
errorlog = '/dev/stderr'
