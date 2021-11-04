from datetime import datetime
import time
from time import sleep
import psutil
from psutil._common import bytes2human
import pandas as pd
import csv

def main():
    print('MEMORY\n------')
    #pprint_ntuple(psutil.virtual_memory())
    print('\nSWAP\n----')
    #pprint_ntuple(psutil.swap_memory())
    ts=dict(psutil.virtual_memory()._asdict())
    ts.update({'timestamp':str(datetime.now())})
    df = pd.DataFrame(ts,index=[0])
    #df.set_index("timestamp", inplace = True)
    df.to_csv('my_csv.csv', mode='w')

def new_func():
    print("---")
    SDict = dict(psutil.virtual_memory()._asdict())
    SDict.update({'timestamp':str(datetime.now())})
    df = pd.DataFrame(SDict,index=[0])
    df.to_csv('my_csv.csv', mode='a', header=False)
if __name__ == '__main__':
    main()
    while(True):
        new_func()
        sleep(60)


