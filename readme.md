# Data Preparation
Our dataset is based on the following kaggle images

- https://www.kaggle.com/datasets/mouryap/koalas-in-the-wild
- https://www.kaggle.com/datasets/siddardhashayini3/wildvision47-wild-animal-image-dataset
- https://www.kaggle.com/datasets/hugozanini1/kangaroodataset

From these 3 kaggle datasets :
- we extract the koalas and kangaroos images
- we combine them 
- we added some negative examples using hare, wombat and bear

We then search online for images of koala and kangaroo together in 1 image
google "koala and kangaroo together" and download some images for them in together
we also add some empty images 

Our directory structure is now 
./koala_kangaroo_images
├── bear
├── hare
├── kangaroo
├── koala
├── none
├── together
└── wombat

we use `re_org.py` to gather the images and rename them 
We now have 2661 images that we upload to roboflow
We tested in roboflow SAM3 and we found bunch of mistakes
We would like to manually verify or try label-studio with dino groundhog model that we have installed locally
but this is too many images to verify or manual labelling

Hence, we manually filter and reduce some images and rerun `re_org.py`
```
Copied and renamed: 347.jpg -> image_0350_koala.jpg
Copied and renamed: 227.jpg -> image_0351_koala.jpg
Copied and renamed: 233.jpg -> image_0352_koala.jpg
Copied and renamed: image_017.jpg -> image_0353_koala.jpg
Copied and renamed: image_003.jpg -> image_0354_koala.jpg
Copied and renamed: image_002.jpg -> image_0355_koala.jpg
Copied and renamed: image_016.jpg -> image_0356_koala.jpg
Copied and renamed: 346.jpg -> image_0357_koala.jpg
Copied and renamed: 178.jpg -> image_0358_koala.jpg
Copied and renamed: 144.jpg -> image_0359_koala.jpg
Copied and renamed: 84.jpg -> image_0360_koala.jpg
Copied and renamed: 230.jpg -> image_0361_koala.jpg
Copied and renamed: 218.jpg -> image_0362_koala.jpg
Copied and renamed: image_014.jpg -> image_0363_koala.jpg
Copied and renamed: image_028.jpg -> image_0364_koala.jpg
Copied and renamed: image_029.jpg -> image_0365_koala.jpg
Copied and renamed: image_015.jpg -> image_0366_koala.jpg
Copied and renamed: image_001.jpg -> image_0367_koala.jpg
Copied and renamed: 219.jpg -> image_0368_koala.jpg
Copied and renamed: 0.jpg -> image_0369_koala.jpg
Copied and renamed: houbii-singaporezoo-09.jpg -> image_0370_none.jpg
Copied and renamed: image.jpg -> image_0371_none.jpg
```

Now we have 372 images, still a lot but more manageable

we use label studio to manually create annotation, occasionally with the help of grounding dino
We upload the annotated dataset to Roboflow (https://universe.roboflow.com/nyp-cwjfs/yolo_koala_kangaroo)
We then use roboflow studio to split our data to :
- train 70%
- validation 20%
- test 10%
Also we enable resize to 512x512 with auto orientation
