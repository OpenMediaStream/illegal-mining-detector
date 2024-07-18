from PIL import Image

from ultralytics import YOLO

model = YOLO("./runs/detect/Sentinel+Landsat/weights/best.pt")

results = model("./teste3.jpg", iou=0.4, conf=0.3)
print(results)

for i, r in enumerate(results):
    
    im_bgr = r.plot()
    im_rgb = Image.fromarray(im_bgr[..., ::-1])

    r.show()