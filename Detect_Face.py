import cv2
import time

import numpy as np
import mediapipe as mp

from keras.models import load_model
from pathlib import Path


if __name__ == '__main__':
    data = ['Buffalo', 'Capybara', 'Cat', 'Cow', 'Deer', 'Dog', 'Elephant', 'Giraffe', 'Jaguar', 'Kangaroo', 'Lion', 'Rhino', 'Sheep', 'Tiger', 'Zebra']

    current_path = str(Path.cwd())

    model_save = current_path + r'\Model\Model_Data\Model.h5'
    model = load_model(model_save)

    vid = cv2.VideoCapture(0)
    _, frame = vid.read()
    h, w, _ = frame.shape

    face_detection = mp.solutions.face_detection.FaceDetection()
    db = None

    while True:
        _, frame = vid.read()
        frame = cv2.flip(frame, 1)

        face_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face = face_detection.process(face_frame)

        if face.detections:
            for detection in face.detections:
                face_data = detection.location_data
                box_data = face_data.relative_bounding_box
                x = round(box_data.xmin * w)
                y = round(box_data.ymin * h)
                wi = round(box_data.width * w)
                he = round(box_data.height * h)

                if 0 < x < w and 0 < y < h and 0 < x+wi < w and 0 < y+he < h:
                    if not db:
                        db = time.time()

                        predict_frame = cv2.resize(face_frame[y: y+he, x: x+wi], (224, 224), interpolation=cv2.INTER_LINEAR_EXACT)
                        predict_data = np.asarray(predict_frame)
                        predict_data = np.expand_dims(predict_data, axis=0)

                        prediction = np.squeeze(model.predict(predict_data))
                        _predict = np.argmax(prediction)
                    
                    if time.time() - db > 1.5: db = None
                    
                    cv2.rectangle(frame, (x, y), (x+wi, y+he), (0, 255, 0), 2)
                    cv2.putText(frame, f'{data[_predict]}: {str(prediction[_predict]*100)[:5]}%', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2, cv2.LINE_AA, False)

        cv2.imshow('Cam', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'): break
        if cv2.waitKey(1) == 27: break
        if cv2.getWindowProperty('Cam', cv2.WND_PROP_VISIBLE) < 1: break

    vid.release()
    cv2.destroyAllWindows()
