from pathlib import Path
from lerobot.common.datasets.lerobot_dataset import LeRobotDataset
from huggingface_hub import login

login() 


repo_id = "LiamFy/red_cup_slim_groot"
local_root = Path("/Users/liamachenbach/Documents/VSprojects/Isaac-GR00T-mimic/red_cup_pour")  # Path to your local dataset

dataset = LeRobotDataset(repo_id, root=local_root)

dataset.push_to_hub(
    tags=["LeRobot", "test"],  # Optional tags
    private=False,  # Set to True for private repo
    upload_large_folder=True,  # Set to True for large datasets
)