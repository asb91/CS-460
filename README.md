# CS-460
Machine Learning model for the Identification of Sulphur Centred Hydrogen Bonds

The model can be used to identify SCHBs directly from the (.pdb) files. 

Usage:

Download the complete repository on your system

For identification on new inputs:

1. Place your input (.pdb) files in the /Data/Predict/ folder 
2. Execute the jupyter notebook (CS-460 Predictions.ipynb) for the ouput 

The model has been trained on the top-500 database from the Richardson Lab. It can be trained on new files as well

For training the model on new data:

1. Rename the new dataset (.csv) to Dataset and place it in the Datasets folder
2. Rename the positive instances file (.csv) to Positives and place it in the Datasets folder
3. Execute the jupyter notebook (CS-460 Model.ipynb)

Now, the previously explained method can be simply used for identifation process using the newly trained model.

Dependencies:

The code in this project makes use of modules from the following libraries:

1. BioPython
2. ProDy
3. Pandas
4. Numpy
5. MatPlotLib
6. SciKit Learn

Please make sure to install these libraries before running the code. Instructions for installation on specific platforms can be found on the Documenation page of the libraries' website.  
