import fiftyone as fo
import fiftyone.zoo as foz

max_samples = 1000
classes = ["Koala", "Kangaroo"]
for object_class in classes:
    print(f"Downloading images for class: {object_class}")
    # Download a subset of the Open Images V7 dataset
    dataset = foz.load_zoo_dataset(
        "open-images-v7",
        splits=["train","test", "validation"], # Specify the dataset splits
        classes=[object_class], # Specify the classes of interest 
        max_samples=max_samples, # Limit the number of samples to download we start small with 10 samples only
        label_types=["detections", "classifications"], # Specify label types if needed
        shuffle=True, # Shuffle the samples
        seed=51 # Set a random seed for reproducibility
    )
    # Define where you want to save the images
    export_dir = "/home/ray/Projects/Label-Studio/open-images-v7/" + object_class
    # Choose an export format, e.g., COCO Detection format
    export_format = fo.types.COCODetectionDataset
    # Export the dataset
    dataset.export(
        export_dir=export_dir,
        dataset_type=export_format,
        label_field="detections", # Specify the field to export if needed
    )
    print(f"Exported images to {export_dir}")
