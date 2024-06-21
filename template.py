import os
from pathlib import Path
import logging

list_of_files = [
    r".github\workflows\.gitkeep",
    r"src\__init__.py",
    r"src\components\__init__.py",
    r"src\components\data_ingestion.py",
    r"src\components\data_transformatiion.py",
    r"src\components\model_trainer.py",
    r"src\components\model_evalution.py",
    r"src\pipeline\__init__.py",
    r"src\pipeline\training_pipeline.py",
    r"src\pipeline\prediction_pipeline.py",
    r"src\utils\__init__.py",
    r"src\utils\utils.py",
    r'src\logger\logger.py',
    r'src\exception\exception',
    r"test\unit\__init__.py",
    r"test\integration\__init__.py",
    r"init_setup.py",
    r"requirements.txt",
    r"requirements_dev.txt",
    r'setup.config',
    r'pyproject.toml',
    r'tox.ini',
    r'experiment\experiments.ipynb'
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Creating Directory: {filedir} for file: {filename}')

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
