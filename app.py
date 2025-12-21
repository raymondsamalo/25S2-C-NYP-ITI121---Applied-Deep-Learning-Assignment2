from ultralytics import YOLO
from PIL import Image
import gradio as gr
from huggingface_hub import snapshot_download
import os

model_path = "/Users/markk/Downloads/best_int8_openvino_model"

def load_model(repo_id):
    download_dir = snapshot_download(repo_id)
    print(download_dir)
    path  = os.path.join(download_dir, "best_int8_openvino_model")
    print(path)
    detection_model = YOLO(path, task='detect')
    return detection_model


def predict(pilimg):

    source = pilimg
    # x = np.asarray(pilimg)
    # print(x.shape)
    result = detection_model.predict(source, conf=0.5, iou=0.6)
    img_bgr = result[0].plot()
    out_pilimg = Image.fromarray(img_bgr[..., ::-1])  # RGB-order PIL image
    
    return out_pilimg


REPO_ID = "khengkok/balloon_yolov8"
detection_model = load_model(REPO_ID)

gr.Interface(fn=predict,
             inputs=gr.Image(type="pil"),
             outputs=gr.Image(type="pil")
             ).launch(share=True)
