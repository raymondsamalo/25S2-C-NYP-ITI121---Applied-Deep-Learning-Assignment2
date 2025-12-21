Using label studio we select and annotated koala and kangaroo images gathered from :
- https://www.kaggle.com/datasets/mouryap/koalas-in-the-wild
- https://www.kaggle.com/datasets/siddardhashayini3/wildvision47-wild-animal-image-dataset
- https://www.kaggle.com/datasets/hugozanini1/kangaroodataset

We have 170 Kangoroo and 174 Koala images

Using roboflow universe we also collect images from :
- https://universe.roboflow.com/yolov12objectdetectionproject-fmiep/koala-f5iir
- https://universe.roboflow.com/yolov12objectdetectionproject-fmiep/kangaroo-2rbwz

we have the following datasets created using label-studio and roboflow :
- From https://app.roboflow.com/raymonds-mqlky/yolo_koala_kangaroo_no_bg/1
    - yolo_koala_kangaroo_no_bg.v1-no_background.yolov11.zip
        - no background images
        - 296 train and 44 validation images
        - Annotated manually using Label Studio 
        - Resize using Roboflow to 640x640 and auto-orient
        - No augmentation
    - yolo_koala_kangaroo_no_bg.v2-no_bg_brightness.yolov11
        - 592 train and 44 validation images
        - Add Brightness Augmentation between -15% and +15%
    - yolo_koala_kangaroo_no_bg.v3-no_bg_brightness_hflip.yolov11.zip
        - 592 train and 44 validation images
        - Add Brightness Augmentation between -15% and +15%
        - Add Flip Horizontal Augmentation
    - yolo_koala_kangaroo_no_bg.v3-no_bg_brightness_hflip.yolov11.zip
        - 592 train and 44 validation images
        - Add Brightness Augmentation between -15% and +15%
        - Add Grayscale images augmentation 15% of population -> I added this to allow model to differentiate between background and image (kangoroo especially)
    - yolo_koala_kangaroo_no_bg.v5-no_bg_b_g_exposure.yolov11.zip
        Grayscale: Apply to 15% of images
        Brightness: Between -15% and +15%
        Exposure: Between -10% and +10%

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
├── 0_no_background_20.yaml
├── 1_original_20.yaml
├── 2_rotation_20.yaml
├── 3_nbg_brightness_20.yaml
├── 4_nbg_b_hflip_20.yaml
├── 5_nbg_b_gray_20.yaml
├── 6_nbg_b_g_exposure_20.yaml
├── 7_nbg_b_gray_70.yaml


the file names indicates the augmentation and lastly the epoch


results :
- Experiment 0 No Background 
    mAP@50 0.84261 F1 Score: 0.8138382232715108 Precision: 0.8663764093828317, Recall: 0.7673076923076922
- Experiment 1 Original 
    mAP@50 0.82677 F1 Score: 0.8016221694929363 Precision: 0.8111582564790287, Recall: 0.7923076923076923 -> add background made it worse
- Experiment 2 Rotation 
    mAP@50 0.79385 F1 Score: 0.7575404488062254 Precision: 0.7924105674337826, Recall: 0.725609901218067 -> Rotation made it worse
- Experiment 3 No Background Brightness
    mAP@50 0.87867 F1 Score: 0.8192785323219932 Precision: 0.8497767682998405, Recall: 0.7908935959226651 -> better than previous experiments
- Experiment 4 No Background Brightness Horizontal Flip
    mAP@50 0.87639 F1 Score: 0.8183291601052397 Precision: 0.8876127833353802, Recall: 0.7590784315854575 -> not as good as experiment 3 
- Experiment 5 No Background Brightness Gray
    mAP@50 0.89114 F1 Score: 0.8581574409111282 Precision: 0.8809234790530212, Recall: 0.8365384615384616 -> improved
- Experiment 6 No Background Brightness Gray Exposure
    mAP@50 0.89227 F1 Score: 0.8468006970334975 Precision: 0.8582671798082908, Recall: 0.8356365602132901 -> our mAP improved but we are less precise and our confusion metrics looks worst as we have more background identified as kangaroo, let's avoid this as our improvement in mAP is slight only
- Experiment 7 No Background Brightness Gray -> Train longer than 20 epochs -> increase to 50 Epochs

