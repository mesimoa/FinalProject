# FinalProject
This Project is About sending Data from flask app to MongoDB, Using mongoDB as a Storage and creating an html file for my incoming data collection and integrating it into python env. Using FLask,Mongo, lastly html. 
Flask, a lightweight web framework in Python, paired with MongoDB that is a NoSQL database that provides a flexible and scalable solution for data storage.

Set Up the Environment
pip install Flask pymongo
MongoDB Setup: Make sure you have MongoDB installed and running. 
**Create a Flask App**
we Create a HTML files(template) for Flask app that handles incoming data.
from flask import Flask, request,  uri_for,render_template
from pymongo import MongoClient
import pymongo
#initializing the Flask App, input all the pfeatures needed to be input inline with the features in HTML.
**Running the Flask App**
Save the above script as app.py.
Run the Flask application:
Sending Data to Flask App

**Verify Data in MongoDB**
data was inserted by querying your MongoDB database: using MongoDB Atlas (a local-base MongoDB service).
This setup allows us to send data from a Flask application to a MongoDB database.

**PreProcessing Data**
Then i Preprocess the Data collected for analysis in python then using python jupyter for analysis. Save The image and proceed them to power point for presentation.





