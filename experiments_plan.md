Using label studio we select and annotated koala and kangaroo images gathered from :
- https://www.kaggle.com/datasets/mouryap/koalas-in-the-wild
- https://www.kaggle.com/datasets/siddardhashayini3/wildvision47-wild-animal-image-dataset
- https://www.kaggle.com/datasets/hugozanini1/kangaroodataset

Using roboflow universe we also collect images from :
- https://universe.roboflow.com/yolov12objectdetectionproject-fmiep/koala-f5iir
- https://universe.roboflow.com/yolov12objectdetectionproject-fmiep/kangaroo-2rbwz

we have the following datasets created using label-studio and roboflow :
- From https://universe.roboflow.com/raymonds-mqlky/yolo_koala_kangaroo/dataset/6
    - yolo_koala_kangaroo.v2-original.yolov11.zip 
        - 300 train and 44 validation images
        - Annotated manually using Label Studio 
        - Add background images to avoid detecting people and gum trees
        - Resize using Roboflow to 640x640 and auto-orient
        - No augmentation
    - yolo_koala_kangaroo.v3-add_rotation.yolov11.zip
        - 600 train and 44 validation images
        - Add Rotation Augmentation between -15 degree and +15 degree
    - yolo_koala_kangaroo.v4-add_rotation_brightness.yolov11.zip
        - 600 train and 44 validation images
        - Add Rotation Augmentation between -15 degree and +15 degree
        - Add Brightness Augmentation between -15% and +15%
    - yolo_koala_kangaroo.v5-add_rotation_brightness_blur.yolov11.zip
        - 600 train and 44 validation images
        - Add Rotation Augmentation between -15 degree and +15 degree
        - Add Brightness Augmentation between -15% and +15%
        - Add Blur up to 2.5px 
    - yolo_koala_kangaroo.v6-add_rotation_brightness_blur_flip.yolov11.zip
        - 600 train and 44 validation images
        - Add Rotation Augmentation between -15 degree and +15 degree
        - Add Brightness Augmentation between -15% and +15%
        - Add Blur up to 2.5px 
        - Add Horizontal Flip
- From https://universe.roboflow.com/raymonds-mqlky/koala_kangaroo_rfu_kaggle/dataset/2
    - koala_kangaroo_rfu_kaggle.v2-latest.yolov11.zip
        - Expand the images using pre-annotated Koala dataset from roboflow universe
        - Expand the images using pre-annotated Kangaroo dataset from roboflow universe
        - Augmentations: 
            -  Flip: Horizontal
            -  Rotation: Between -15° and +15°
            -   Brightness: Between -15% and +15%
            -   Blur: Up to 2.5px

we unzip them into datasets folder

We then create config files in experiments folder to use the datasets
./experiments/
├── 1_original_20.yaml
├── 2_rotation_20.yaml
├── 3_rotation_brightness_20.yaml
├── 4_rotation_brightness_blur_20.yaml
├── 5_rotation_brightness_blur_flip_20.yaml
├── 6_rotation_brightness_blur_flip_100.yaml
├── 7_rotation_brightness_blur_flip_large_20.yaml
└── 8_rotation_brightness_blur_flip_large_50.yaml
the file names indicates the augmentation and lastly the epoch
