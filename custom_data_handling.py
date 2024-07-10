import requests
import zipfile
from pathlib import Path
import os
import torch

print(f"Torch Version: {torch.__version__}")


def download_and_extract_data():
    dir_path = Path("data/")
    data_path = dir_path / "pizza_steak_sushi"
    if data_path.is_dir():
        print("Data Folder is already available...")
    else:
        print(f"Did not find {data_path} directory, creating one...")
        data_path.mkdir(parents=True, exist_ok=True)

        with open(data_path / "pizza_steak_sushi.zip", "wb") as f:
            request = requests.get(
                "https://github.com/mrdbourke/pytorch-deep-learning/raw/main/data/pizza_steak_sushi.zip"
            )
            print("Downloading pizza, steak, sushi data...")
            f.write(request.content)

        with zipfile.ZipFile(data_path / "pizza_steak_sushi.zip", "r") as ref_zip:
            print("Unzipping pizza, steak, sushi data...")
            ref_zip.extractall(data_path)


def check_directory_structure(path: Path):
    for dirpath, image_dir, files in os.walk(path):
        print(
            f"There are {len(image_dir)} directories, {len(files)} image_files at {dirpath}"
        )


# Get the data download
if __name__ == "__main__":
    dir_path = Path(
        "/home/sces79/Farhan_zafrani/Self_Learning/deep_learning/mlops_functions/data"
    )
    download_and_extract_data()
    check_directory_structure(dir_path)
