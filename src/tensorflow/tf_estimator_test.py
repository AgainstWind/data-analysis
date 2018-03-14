import tensorflow as tf
from tensorflow import losses
from tensorflow import flags

classifier = tf.estimator.LinearClassifier()

"""
      input_fn: Input function returning a tuple of:
          features - `Tensor` or dictionary of string feature name to `Tensor`.
          labels - `Tensor` or dictionary of `Tensor` with labels.
"""
def train_input_fn():
    data = {
        tf.contrib.time
    }

classifier.train(steps=2000,input_fn=train_input_fn)

predictions = classifier.predict(input_fn=predict_input_fn)