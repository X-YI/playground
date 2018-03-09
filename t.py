import math

from matplotlib import cm
from matplotlib import gridspec
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
import tensorflow as tf
from tensorflow.python.data import Dataset
import pdb

tf.logging.set_verbosity(tf.logging.ERROR)
pd.options.display.max_rows = 10
pd.options.display.float_format = '{:.1f}'.format

california_housing_dataframe = pd.read_csv("data.txt", sep=",")


def preprocess_features(california_housing_dataframe):
    selected_features = california_housing_dataframe[["a", "b", "c", "re1", "re2", "x11", "x12", "x21", "x22"]]
    processed_features = selected_features.copy()
    # Create a synthetic feature.
    return processed_features

def preprocess_targets(california_housing_dataframe):
    output_targets = pd.DataFrame()
    # Scale the target to be in units of thousands of dollars.
    output_targets["re1"] = california_housing_dataframe["re1"]
    return output_targets

training_examples = preprocess_features(california_housing_dataframe.head(8000))
training_examples.describe()
training_targets = preprocess_targets(california_housing_dataframe.head(8000))
pdb.set_trace()

validation_examples = preprocess_features(california_housing_dataframe.tail(2000))
validation_targets = preprocess_targets(california_housing_dataframe.tail(2000))



plt.figure(figsize=(13, 8))

ax = plt.subplot(1, 2, 1)
ax.set_title("Validation Data")

ax.set_autoscaley_on(False)
ax.set_ylim([32, 43])
ax.set_autoscalex_on(False)
ax.set_xlim([-126, -112])
plt.scatter(validation_examples["b"],
            validation_examples["c"],
            cmap="coolwarm",
            c=validation_targets["re1"] / validation_targets["re1"].max())

ax = plt.subplot(1,2,2)
ax.set_title("Training Data")

ax.set_autoscaley_on(False)
ax.set_ylim([32, 43])
ax.set_autoscalex_on(False)
ax.set_xlim([-126, -112])
plt.scatter(training_examples["b"],
            training_examples["c"],
            cmap="coolwarm",
            c=training_targets["re1"] / training_targets["re1"].max())
_ = plt.plot()
