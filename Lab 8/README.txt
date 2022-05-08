*****************************************LAB 8************************************

Author: Elizabeth Huang
Class: EE104

Video Demos
CNN Classifier
Pt. 1: https://drive.google.com/file/d/1H-8830fH7UvdCETKpyEel58VEYATol9w/view?usp=sharing
Pt. 2: https://drive.google.com/file/d/1ueQ70TOTls6BDiUI7Ytyt8P5iiV4QTpV/view?usp=sharing
Game: https://drive.google.com/file/d/1FGvpiGSRPeXbEHa8-eNAQVjqu1vCggr2/view?usp=sharing

Github: https://github.com/huangabeth/Lab8

*************************************************************************************
References:
Dr. Christopher Pham's Module 8 Lectures & Code
Coding Games In Python & its Python Games Resource Pack: Chapter 8 Balloon Flight

*************************************************************************************
ABOUT THE CODE
CNN Classifier > Check Github link and run on Colab
	or cnn.ipynb > copy and paste to Colab or whatever you prefer

Balloon Flight Game
	Chapter 8 Balloon Flight > balloon.py: run this code to play Balloon Flight!
				   high-scores.txt: text file of top 5 high scores
*************************************************************************************
***MAKE SURE THAT THE FOLLOWING PYTHON MODULES ARE INSTALLED***
CNN Classifier
(Was ran on Colab, not needed to install anything, but in case you need to install:)
	import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import numpy as np


For Balloon Flight Game
	pip install pgzero on command line
	import pgzrun
	from pgzero.builtins import Actor
	from random import randint
*************************************************************************************
Instructions:
CNN Classifier: copy and paste github code to Colab and run there.

Balloon Flight Game
	1. Run balloon.py
	2. Click on mouse to move balloon up.
	3. The balloon will gradually move down when mouse is unclicked.
	4. Avoid the bird, tree and house obstacles. The bird is much faster than other
		obstacles at it has been Sped Up.
	5. Passing an obstacle will immediately gain a point (Different Way to Score)
	6. The tree is designed to be spaced out from the house (Space Out).
	7. The balloon's top can go off screen a little for more mobility.
	8. Hitting an obstacle will end the game. The top 5 high scores (more High Scores)
		will be shown.