import pandas as pd
from datetime import date
from autots import AutoTS
from sklearn.metrics import mean_squared_error
import numpy as np
import numpy as np
import pandas as pd
import pickle
from pathlib import Path
root = Path(".")


def predict(model_name):
    if(model_name[0] == 'i'):
        my_path = root / "ipc" / model_name
    else:
        my_path = root / "sll" / model_name

    filename = open(my_path, 'rb')
    mp = pickle.load(filename)
    return mp.predict().forecast
    