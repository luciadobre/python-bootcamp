import os
MAIN_FILE_PATH =os.path.dirname(__file__)
IMAGES_FOLDER = os.path.join(MAIN_FILE_PATH, "images")
CARDS_FOLDER = os.path.join(IMAGES_FOLDER, "cards")

files = [f for f in os.listdir(CARDS_FOLDER)]



for i in files:
    print(f"'{i[:-4]}': '{i, i[0]}")