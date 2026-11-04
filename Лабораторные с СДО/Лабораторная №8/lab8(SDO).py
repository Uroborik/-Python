import os
import tarfile
from PIL import Image

IMAGE_EXT = (".png", ".jpg", ".jpeg", ".gif", ".bmp")


def extract_images(tar_path, save_dir):
    os.makedirs(save_dir, exist_ok=True)
    count = 0
    with tarfile.open(tar_path) as tar:
        for member in tar.getmembers():
            if member.isfile() and member.name.lower().endswith(IMAGE_EXT):
                image = Image.open(tar.extractfile(member))
                image.save(os.path.join(save_dir, os.path.basename(member.name)))
                count += 1
    return count


os.makedirs("src", exist_ok=True)
Image.new("RGB", (10, 10), "red").save("src/a.png")
Image.new("RGB", (10, 10), "blue").save("src/b.jpg")
with open("src/notes.txt", "w", encoding="utf-8") as f:
    f.write("не изображение")
with tarfile.open("images.tar", "w") as tar:
    tar.add("src", arcname="src")

print("Распаковано изображений:", extract_images("images.tar", "out"))
print("Файлы в out:", sorted(os.listdir("out")))
