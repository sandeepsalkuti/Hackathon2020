Unemployment Prediction:

Created a web application using HTML, CSS, Python and FLASK framework and Machine Learn Models are deployed on production using Flask API deployed in Heroku and can be accessed using below link
https://hackathonspring2020.herokuapp.com/.

Dataset link: http://localhost:8888/notebooks/Downloads/sumanth.ipynb
Jupyter link: http://localhost:8888/notebooks/Downloads/sumanth.ipynb


Prerequisites
You must have Scikit Learn, Pandas (for Machine Leraning Model), Numpy for numerical calculations and Flask (for API) installed.

Project Structure
This project has four major parts :

model.py - This contains code fot our Machine Learning model to predict unemployment based on training data in 'edited.csv' file.
app.py - This contains Flask APIs that receives employee details through GUI or API calls, computes the precited value based on our model and returns it.
request.py - This uses requests module to call APIs already defined in app.py and dispalys the returned value.
templates - This folder contains the HTML template to allow user to enter some basic detail and displays the predicted unemployment .
Running the project
Ensure that you are in the project home directory. Create the machine learning model by running below command -
python model.py
This would create a serialized version of our model into a file model.pkl

Run app.py using below command to start Flask API
python app.py
By default, flask will run on port 5000.

Navigate to URL http://localhost:5000
You should be able to view the homepage 

Functionality:
By giving some basic fields unemployment chances are predicted based on age group field where giving certain number of people of that age, Income of certain number of people, Transoprtation used by certain number of people like drove alone, Bicycle, Taxi cab etc. and by clicking predict button probability is predicted with percentage.
User can check usecase or problemset given by clicking on usecase button
Enter valid numerical values in all 3 input boxes and hit Predict.
If everything goes well, you should be able to see the predcited unemployment vaule on the HTML page!

