nohup airflow scheduler
airflow webserver 
#!/bin/sh

# Initialize the Airflow database
airflow db init

# Create an Airflow user
airflow users create \
    --username admin \
    --password admin \
    --firstname Nithin \
    --lastname CH \
    --role Admin \
    --email cherukumallinithin@gmail.com

# Start the Airflow webserver
airflow webserver -p 8080 &

# Start the Airflow scheduler
airflow scheduler
