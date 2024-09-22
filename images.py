from PIL import Image
import os
my_image = Image.open(r"C:/Users/ULTRAPC/Desktop/projects/learning/python/practice-py/img.jpg")


cropped = (0 , 0 , 450 , 450)

cropped_image = my_image.crop(cropped)
my_image.show()

cropped_image.show()

# cropped_image.save(r"C:/Users/ULTRAPC/Desktop/projects/learning/python/practice-py/cropped_img.jpg")
# cropped_image.remove(r"C:/Users/ULTRAPC/Desktop/projects/learning/python/practice-py/cropped_img.jpg")
os.remove(r"C:/Users/ULTRAPC/Desktop/projects/learning/python/practice-py/cropped_img.jpg")
