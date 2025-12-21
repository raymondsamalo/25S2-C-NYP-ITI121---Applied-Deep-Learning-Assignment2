import os
import fiftyone.zoo as foz

# Define your desired parameters
DATASET_NAME = "open-images-v6" # Or "open-images-v6"
SPLITS = ["train","test"] # Choose 'train', 'validation', or 'test'
MAX_SAMPLES = 10 # Limit the number of samples to download (optional)
CLASSES_OF_INTEREST = ["Koala", "Kangaroo"] # Download images only if they contain these classes (optional)
SCRIPT_DIR =  os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "data/images")
os.makedirs(DATA_DIR,exist_ok=True) # make data dir
print(f"Downloading a subset of {DATASET_NAME} splits='{SPLITS}' with images only...")

# Download and load the dataset subset
dataset = foz.load_zoo_dataset(
    DATASET_NAME,
    splits=SPLITS,
    label_types=[], # This is crucial to download only images and no labels
    max_samples=MAX_SAMPLES,
    classes=CLASSES_OF_INTEREST,
    shuffle=True,
    seed=51,
    # You can add a `dataset_dir` argument to specify where to save the files
    # dataset_dir=DATA_DIR
)
print("Download complete. Dataset summary:")
print(dataset)
