import log as log
def write_in_file(features, obj, log_file):
    '''
    This function will write the prediction into 'prediction.txt' file. 
    So any time you can check what model predicted for certain values.\n
    l - list\n
    o - output of model\n
    log_file - object of log.txt file\n
    '''
    with open("prediction.txt","a+") as pred_file:
        log.put_log(log_file,"Prediction file opened")
        for i in features:
            pred_file.write(f"{i},")
            log.put_log(log_file,f"list Value {i} inserted")
        pred_file.write(f"{obj**4}\n")
        log.put_log(log_file,f"Output inserted")