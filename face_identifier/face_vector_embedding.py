from keras_vggface.vggface import VGGFace
from keras_vggface import utils
import numpy as np

vgg_features = VGGFace(include_top=False, input_shape=(224, 224, 3), pooling='avg')
def predict_features(image):
    image = np.expand_dims(image, axis=0).astype('float32')
    image = utils.preprocess_input(image, version=1)
    preds = vgg_features.predict(image)[0]
    return preds