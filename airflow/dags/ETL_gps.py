import datetime
import json
from airflow.decorators import dag, task
from airflow.utils.dates import days_ago
import os
dag_path=os.getcwd()

default_args={ 'owner':"Praveen",'start_date':datetime.datetime(2023, 10, 12),'retries': 1,}

@dag(default_args=default_args,schedule_interval=None)

def etl():
    @task()
    def extract():
        """Extract data from .txt file
           return: pandas df
        """
        import pandas as pd
        path = os.path.join(dag_path, 'gps_logs')
        file_list = os.listdir(path)
        data_list=[]
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        p="log"+"_"+current_date+".txt"
        p_dir=os.path.join(dag_path,'gps_logs',p)
        if os.path.exists(p_dir):
            print("File exists")
            txt_file_path = os.path.join(path, file_list[-1])
            with open(txt_file_path, 'r') as file:
                for line in file:
                    if len(line) > 200:
                        d = json.loads(line)
                        # print(d)
                        data_list.append(d)
                    else:
                        print("Bad data")
            df = pd.DataFrame(data_list)
            if 't' in df.columns:
                df.drop(['t'], axis=1, inplace=True)
            df.drop(['_type', 'BSSID', 'SSID'], axis=1, inplace=True)
            df['datetime'] = pd.to_datetime(df['created_at'], unit='s')
            df['date'] = df['datetime'].dt.date
            df['time'] = df['datetime'].dt.time
            df.drop(['datetime', 'created_at', 'tst', 'tid'], axis=1, inplace=True)
            file_path = os.path.join(dag_path, 'csv_files')
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            file_name = os.path.join(file_path, f"log_{current_date}.csv")
            df.to_csv(file_name)
        else:
            print("File does not exist")

    data=extract()
etl_dag=etl()
