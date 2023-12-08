# -*- coding: utf-8 -*-
from flask import Flask, request, Response
from joblib import load
import pandas as pd
import os
os.environ["PYTHONUNBUFFERED"]="0"


# Initialising
app = Flask(__name__)

def load_decision_model_predict(model_path, encoder_path, data_points):

        # Loading the model
        my_decision_model = load(model_path) 
        
        #Loading my encoder
        le=load(encoder_path)
    
        # Creating a DataFrame 
        temp_dict = {'sepal.length':data_points[0], 'sepal.width':data_points[1], 'petal.length':data_points[2], 'petal.width':data_points[3]}
        df_temp = pd.DataFrame(temp_dict)
    
        # Predicting on my_data
        predictions = my_decision_model.predict(df_temp)
          
        labels= [le.inverse_transform([i])[0] for i in predictions]
 
        return labels


@app.route("/getvariety", methods = ['POST','GET'])
def getvariety():
    
    # Reading user data, it will look like this {"mydata": '1'}
    print(request,flush=True)
    print("Hello-1")

    #print(data)
    leaf_input1 = float(request.args.get("o1"))
    leaf_input2 = float(request.args.get("o2"))
    leaf_input3 = float(request.args.get("o3"))
    leaf_input4 = float(request.args.get("o4"))  
    my_prediction=load_decision_model_predict('my_decision_tree_model.joblib', 'labelEncoder.joblib',
                                [[leaf_input1],[leaf_input2],[leaf_input3],[leaf_input4]])
    
    # Giving the user the answer we are looking for
    return Response(str(my_prediction[0]))


if __name__ == '__main__':
    app.run(debug=False)



