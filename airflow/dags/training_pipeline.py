from __future__ import annotations
import json
from textwrap import dedent
import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
from src.pipeline.training_pipeline import TrainingPipeline

# Initialize the TrainingPipeline instance
training_pipeline = TrainingPipeline()

# Define the DAG
with DAG(
    "gemstone_training_pipeline",
    default_args={"retries": 2},
    description="This is my training pipeline",
    schedule_interval="@weekly",
    start_date=pendulum.datetime(2024, 7, 21, tz="UTC"),  # Ensure correct timezone
    catchup=False,
    tags=['machine_learning', 'Classification', 'gemstoneprediction']
) as dag:

    dag.doc_md = __doc__

    def data_ingestion(**kwargs):
        ti = kwargs["ti"]
        train_data_path, test_data_path = training_pipeline.start_data_ingestion()
        ti.xcom_push("data_ingestion_artifact", {'train_data_path': train_data_path, 'test_data_path': test_data_path})

    def data_transformation(**kwargs):
        ti = kwargs["ti"]
        data_paths = ti.xcom_pull(task_ids='data_ingestion', key='data_ingestion_artifact')
        train_data_path = data_paths['train_data_path']
        test_data_path = data_paths['test_data_path']
        train_arr, test_arr = training_pipeline.start_data_transformation(train_data_path, test_data_path)
        ti.xcom_push("data_transformation_artifact", {'train_arr': train_arr, 'test_arr': test_arr})

    def model_trainer(**kwargs):
        ti = kwargs["ti"]
        data_arrs = ti.xcom_pull(task_ids='data_transformation', key='data_transformation_artifact')
        train_arr = data_arrs['train_arr']
        test_arr = data_arrs['test_arr']
        training_pipeline.start_model_training(train_arr, test_arr)

    def push_data_to_s3(**kwargs):
        import os 
        bucket_class = os.getenv("BUCKET_NAME")
        artifact_folder = "/app/artifacts"
        os.system(f"aws s3 sync {artifact_folder} s3:/{bucket_name}/artifact")
        
    # Define the tasks
    data_ingestion_task = PythonOperator(
        task_id="data_ingestion",
        python_callable=data_ingestion,
        provide_context=True
    )

    data_transformation_task = PythonOperator(
        task_id="data_transformation",
        python_callable=data_transformation,
        provide_context=True
    )

    model_trainer_task = PythonOperator(
        task_id="model_trainer",
        python_callable=model_trainer,
        provide_context=True
    )

    push_data_to_s3_task = PythonOperator(
        task_id="push_data_to_s3",
        python_callable=push_data_to_s3,
        provide_context=True
    )

    # Set task dependencies
    data_ingestion_task >> data_transformation_task >> model_trainer_task >> push_data_to_s3_task
