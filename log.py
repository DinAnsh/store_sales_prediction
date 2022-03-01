from datetime import datetime

def put_log(file_obj,message):
    '''
    Put your log messages in 'log.txt' file\n
    file_obj - object of 'log.txt' file\n
    message - a message to put in 'log.txt' file
    '''
    present_date_time = datetime.now()
    date_time = present_date_time.strftime("%d/%m/%Y, %H:%M:%S")
    file_obj.write(f"{date_time}\t{message}\n")
