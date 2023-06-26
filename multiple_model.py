import pickle
import os
from tensorflow import keras
from datetime import datetime
model_paths = ["h5Model.h5","h5model2.h5", "h5model3.h5"]



def load_models(model_paths):
    models = []
    for path in model_paths:
        model = keras.models.load_model(path)
        models.append(model)
    return models
