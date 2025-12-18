## Images DataSet & Movie

### Images DataSet Collection

#### Google OpenImages DataSet
We try to collect images from [Google OpenImages DataSet](https://https://storage.googleapis.com/openimages/web/download_v7.html#download-manually) where we download 2 set of images :

1. Koala
2. Kangaroo

To simplify downloading, we will be using [FiftyOne](https://https://docs.voxel51.com/) python library which is recommended by Google in order to download a specific class of images.
```python
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

```

Unfortunately the images provided by Google Open Images often include wrong objects e.g. koala may include teddy bears, disney stitch etc
Similarly for Kangaroo, it may includes lemur or other objects

#### Roboflow Universe

We tried [Roboflow Universe](https://universe.roboflow.com/) and this time we managed to find good image collection for Koala and Kangaroo
- [Koala](https://universe.roboflow.com/yolov12objectdetectionproject-fmiep/koala-f5iir)  546 Images
- [Kangaroo](https://universe.roboflow.com/yolov12objectdetectionproject-fmiep/kangaroo-2rbwz) 853 images

The quality of the dataset is much better than Google Open Images although there are some pictures of wombat appear on the data set too which we filtered out

### Images DataSet Labeling

For labeling we will be using [Label Studio with Groundhog](https://labelstud.io/guide/ml_tutorials/grounding_dino)


### Movie

We will be using Brisbane Lone Pine Koala Sanctuary [movie](https://www.youtube.com/watch?v=x5uvIG5bjyw) from YouTube