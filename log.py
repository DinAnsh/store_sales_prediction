import logging

def put_log(level,msg):
    '''
    Put your log messages in 'log.log' file\n
    level   - 1 or 2 or 3\n
    \t\t1-info\n
    \t\t2-warning\n
    \t\t3-error\n
    message - short description of level
    '''
    logging.basicConfig(filename= "app_logging/log.log",
                        filemode='a+',
                        format=  '%(asctime)s\t%(levelname)s- %(message)s',
                        datefmt="%d-%m-%Y, %H:%M:%S")
    
    if level == 1:
        logging.info(msg)
    if level == 2:
        logging.warning(msg)
    if level == 3:
        logging.error(msg)

#To Count the lines in log.log
def _count_generator(reader):
    b = reader(1024 * 1024)
    while b:
        yield b
        b = reader(1024 * 1024)

#if log file contains more than 2000 lines than make file empty 
with open('app_logging/log.log', 'rb+') as fp:
    c_generator = _count_generator(fp.raw.read)
    count = sum(buffer.count(b'\n') for buffer in c_generator)
    if count+1 >= 2000:                 
        fp.truncate(0)

