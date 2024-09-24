import tensorflow as tf
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

hei = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
wid = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

print(wid,hei)

model = tf.keras.Sequential([
  tf.keras.layers.Input(shape=(hei,wid,3)),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(100, activation="sigmoid", name="perceptron_1"),
  tf.keras.layers.Dense(100, activation="sigmoid", name="perceptron_2"),
  tf.keras.layers.Dense(100, activation="sigmoid", name="perceptron_3"),
  tf.keras.layers.Dense(100, activation="sigmoid", name="perceptron_4"),
  tf.keras.layers.Dense(100, activation="sigmoid", name="perceptron_5"),
  tf.keras.layers.Dense(2, activation="softmax", name="output"),
])

model.build()
print(model.summary())

model.compile(optimizer=tf.optimizers.Adam(learning_rate=0.001),
              loss='mse',
              metrics=['accuracy'])

init = [1.0,0.0]

op = []
cl = []
images = []

EPOCHS = 100
BS = 5

while True:

    ret, frame = cap.read()

    cv2.imshow('Frame', frame)

    wk = cv2.waitKey(1)

    grasp = False
    if wk == ord('q'):
        break

    elif wk == ord('1'):
        grasp = True
        init = [1.0,0.0]

    elif wk == ord('2'):
        grasp = True
        init = [0.0,1.0]

    elif wk == ord('t'):
        model.fit(np.array(images),np.array(cl), epochs=EPOCHS, shuffle=True, batch_size=BS, validation_split=0.3 )

    if wk == ord('p'):
        predict = model.predict(np.array([frame]))
        predict_label = list(np.where(predict[0] >= 0.5, 1 , 0))
        max_value = max(predict_label)
        max_index = predict_label.index(max_value)
        labels = ["True", "False"]
        print("predict_label", labels[max_index])
        print("predict" , predict)

    if grasp:
        print("Classe selected to train:   " , init)

        images.append(frame)
        cl.append(init)

        print(init)
        print("label -" , cl)


cap.release()
cv2.destroyAllWindows()