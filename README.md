# Human-Animal-Face
This project is just a parody for Animal Detection. Instead of an animal to be used, the human face is used to correspond which animal is the most related to the face. 

The [Model](/Model) is trained to detect 15 different animals:
- Buffalo
- Capybara
- Cat
- Cow
- Deer
- Dog
- Elephant
- Giraffe
- Jaguar
- Kangaroo
- Lion
- Rhino
- Sheep
- Tiger
- Zebra

Execute [Detect_Face.py](/Detect_Face.py) to start the program.

A working webcam is mandatory for the project to work. The window can be terminated via `Esc`, `Q` or the close button.

# Model
 ## Model
 More information on the model is provided [here](/Model/README.md).

 ## Dataset
 The dataset can be downloaded from [here]().

# Installation
- Python version 3.9.10.
- Libraries can be installed -> `pip install -r /path/to/requirements.txt`.

# Sources
 ## Dataset
 - https://www.kaggle.com/datasets/jirkadaberger/zoo-animals

 ## VGG16 Model
 - https://github.com/keras-team/keras/blob/v2.13.1/keras/applications/vgg16.py
 - https://medium.com/@mygreatlearning/everything-you-need-to-know-about-vgg16-7315defb5918
