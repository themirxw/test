import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np

# بارگذاری مدل از پیش‌آموزش‌دیده
model = tf.keras.applications.MobileNetV2(weights='imagenet')

# بارگذاری و پردازش تصویر
img_path = 'new_aks.jpeg' # مسیر عکس خود را وارد کنید
img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = preprocess_input(img_array)

# پیش‌بینی محتوای تصویر
predictions = model.predict(img_array)
decoded_predictions = decode_predictions(predictions, top=3)[0]

# بررسی اینکه آیا گربه در تصویر وجود دارد یا خیر
cat_found = any("cat" in pred[1].lower() for pred in decoded_predictions)

if cat_found:
    print("گربه در تصویر یافت شد.")
else:
    print("گربه در تصویر وجود ندارد.")