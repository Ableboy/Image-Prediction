"""import the necessary libraries"""
from imageai.Classification import ImageClassification # The lib make predictions in classification object

import os # This brings in imgs that need to be predicted 

exec_path = os.getcwd() # This brings testable imgs to the predictive ground

prediction = ImageClassification() # var carries the obj class of ML
 
prediction.setModelTypeAsMobileNetV2() # This set out desirable ML models creation

prediction.setModelPath(os.path.join(exec_path, 'mobilenet_v2-b0353104.pth')) # This gives access to model for path image prediction

prediction.loadModel() # This created models runs through

'''The below - predictions are the created models for testing img, while probalilities shows the assurance/accuracy of the prediction'''
predctions, probabilities = prediction.classifyImage(os.path.join(exec_path,'giraffe.jpg'), result_count=5)
for eachPred, eachProb in zip(predctions, probabilities):
    print(f'{eachPred} : {eachProb}')
