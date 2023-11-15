import tempfile
from PIL import Image

with tempfile.NamedTemporaryFile(mode="wb", delete=False) as jpg:
    jpg.write(b"Hello World!")
    print(jpg.name)

    img = Image.open(jpg.name)
    img.show()
