import os

txt_path = "data/train.txt"
data_dir = "data/grains"

with open(txt_path, "w") as f:
    for img_name in sorted(os.listdir(data_dir)):
        _, ext = os.path.splitext(img_name)
        if ext.lower() in [".png", ".jpg", ".jpeg"]:
            img_path = os.path.join(data_dir, img_name)
            f.write(img_path + "\n")
