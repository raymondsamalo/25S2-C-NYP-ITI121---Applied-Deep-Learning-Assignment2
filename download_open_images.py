import os
import fiftyone as fo
import fiftyone.types as fot
import fiftyone.zoo as foz
dataset_name = "open-images-koala-kangaroo"
classes_to_download = ["Koala", "Kangaroo"]
script_dir = os.path.dirname(os.path.realpath(__file__))

MAX_SAMPLES = 50
export_dir=script_dir+"/data/images"
os.makedirs(export_dir, True)
# Load the dataset
dataset = foz.load_zoo_dataset(
    "open-images-v7",
    splits=["train","validation","test"],
    classes=classes_to_download,
    max_samples=MAX_SAMPLES,  # Limits the number of samples for demonstration,
    seed=51,
    dataset_name=dataset_name
)
# export dataset 
dataset.export(
    export_dir=export_dir, dataset_type=fot.ImageDirectory
)
