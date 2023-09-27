# GPS Streaming 

A real time GPS streaming application developed using python,kakfa and airflow

1. Phase 1 : Logging - Log real time gps data and store as text file.
2. Phase 2 : ETL- Perform ETL to clean data, extract useful one and merge on a weekly basis which could be used for ML
3. Phase 3 : Deploy a real time simple to use ML model to see.


Current progres [09/27] - Phase 1 is completed where gps logs are being stored in the logs folder. Other improvements in phase 1 include using SSL certifications. 

For Phase 2 : Use Airflow to build ETL pipelines. 


Current Archirecture: 

![image](https://github.com/praveen555/gps_streaming_kafka/assets/23379996/7af254fc-b8a7-4105-ac4b-5c95f2b6fe23)


