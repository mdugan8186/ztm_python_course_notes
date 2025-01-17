# ==== exercise: ReallySmartBrain ====

# to execute this script remember to cd to your current filepath

from imageai.Classification import ImageClassification
import os

# Set up the execution path
exec_path = os.getcwd()

# Initialize the ImageClassification object
prediction = ImageClassification()

# Set model type and load model
prediction.setModelTypeAsMobileNetV2()
prediction.setModelPath(os.path.join(exec_path, 'mobilenet_v2-b0353104.pth'))
prediction.loadModel()

# Perform image classification
predictions, probabilities = prediction.classifyImage(
    os.path.join(exec_path, 'house.jpg'), result_count=5)

# Display predictions and probabilities
for eachPred, eachProb in zip(predictions, probabilities):
    print(f'{eachPred} : {eachProb}')
