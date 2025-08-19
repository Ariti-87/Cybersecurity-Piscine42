from PIL import Image
from PIL.ExifTags import TAGS
import os
import sys

def extract_exif(image_path):
	"""Extracts and displays EXIF metadata from an image file."""
	try:
		image = Image.open(image_path)
		exif_data = image._getexif()

		if exif_data is not None:
			print(f"Metadata for {image_path}:")
			for tag, value in exif_data.items():
				tag_name = TAGS.get(tag, tag)
				print(f"{tag_name}: {value}")
		else:
			print(f"No EXIF data found for {image_path}")
	except Exception as e:
		print(f"Failed to process {image_path}: {str(e)}")

def main():
	if len(sys.argv) < 2:
		print("Usage: python scorpion.py FILE1 [FILE2 ...]")
		sys.exit(1)

	for image_file in sys.argv[1:]:
		if os.path.isfile(image_file):
			extract_exif(image_file)
		else:
			print(f"{image_file} is not a valid file.")
		print(f"-" * 40)

if __name__ == "__main__":
	main()
