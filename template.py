import os
from pathlib import Path # this will take care of path compatable with different os

list_of_files=[
    
    ".github/workflows/.gitkeep",
    "src/__init__.py",#src represents the source code
    "src/components/__init__.py", #different stages like data ingestion etc are called componensts
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/exception.py",
    "tests/unit/__init__.py",#unit testing is for single unit and integrated is for all the units
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",#for deployment
    "requirements_dev.txt",#to install for development
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file