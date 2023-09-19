# Model

The model used is [VGG16](https://www.geeksforgeeks.org/vgg-16-cnn-model/), which is a CNN that is useful to detect images. The weights of the model are of imagenet.
Transfer learning is used here to increase the efficiency of training and accuracy of the model.

[Train_Model.ipynb](Train_Model.ipynb) can be used to train the model with custom inputs and dataset. The model was able to achieve **94%** validation accuracy along
**20%** validation loss.

The Model and the Original Imagenet Weights are saved in [Model_Data](Model_Data) folder.

# Dataset

The dataset has to be downloaded, and has to be extracted with the folders (`test` and `train`) to be inside `Dataset` folder. For detailed instructions, refer 
to [README.md](Dataset/README.md).
