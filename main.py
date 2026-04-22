import os
from PIL import Image

class ImageConverter:
    def __init__(self, source_path, dest_path, from_format, to_format):
        # initialize paths and formats
        self.source_path = source_path
        self.dest_path = dest_path
        self.from_format = from_format.lower()
        self.to_format = to_format.lower()

        # supported file types
        self.supported = ["png", "jpeg", "jpg", "pdf", "bmp", "gif", "tiff", "webp"]

        # basic validation
        if self.from_format not in self.supported:
            raise ValueError(f"Unsupported input format: {self.from_format}")

        if self.to_format not in self.supported:
            raise ValueError(f"Unsupported output format: {self.to_format}")

    def convert(self):
        # make destination folder if it doesn’t exist
        os.makedirs(self.dest_path, exist_ok=True)

        # if source is a folder, loop through files
        if os.path.isdir(self.source_path):
            for file in os.listdir(self.source_path):
                if file.lower().endswith(self.from_format):
                    full_path = os.path.join(self.source_path, file)
                    self._convert_single(full_path)
        else:
            # if it's a single file
            if self.source_path.lower().endswith(self.from_format):
                self._convert_single(self.source_path)
            else:
                print("File does not match specified input format")

    def _convert_single(self, path):
        try:
            # open image
            img = Image.open(path)

            # create new file name
            base_name = os.path.splitext(os.path.basename(path))[0]
            new_file = os.path.join(self.dest_path, f"{base_name}.{self.to_format}")

            # some formats need RGB (like jpg/pdf)
            if self.to_format in ["pdf", "jpeg", "jpg"]:
                img = img.convert("RGB")

            # save converted file
            img.save(new_file, self.to_format.upper())

            print(f"Saved: {new_file}")

        except Exception as e:
            print(f"Skipped {path}: {e}")



    
input_folder = "/Users/kamari/Downloads/pokedex/"
output_folder = "/Users/kamari/Downloads/pokedex_converted2/"
 
# example usage (update paths before running)
if __name__ == "__main__":
    converter = ImageConverter(
        input_folder,        # replace with your source folder or file
        output_folder,       # replace with your destination folder
        "jpg",                # input format
        "png"                 # output format
    )

    converter.convert()

    