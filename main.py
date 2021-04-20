# Import all processing functions
# from V0_5_fMRI_processing_and_ML_models import extract_regional_activity, extract_functional_connectivity, create_structural_functional_multidict, ml_inference_plots


from flask import Flask,jsonify,request,json,Blueprint
from flask_restful import Api, Resource
import requests

app =Flask(__name__)
# REQUEST_API = Blueprint('request_api', __name__)
api=Api(app)
import timeit
start = timeit.default_timer()
from flask_swagger_ui import get_swaggerui_blueprint
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)

dip={"pid": "123456788", "executionID": "261120201241", "status": 200, "statusMessage": "extractregionalactivity Complete!", "timeTaken": 4.559000444714911e-06}

from regional_activity_extraction import regional_activity
@app.route('/brainsightai/extractregionalactivity',methods = ['POST'])
def extract_regional_activity():
     pid = request.json['pid']
     executionId = request.json['executionID']
     complete_code, status_message = regional_activity(pid, executionId)
     if complete_code == 0:
        final_code = 200
        status_message = "COMPLETE"
     else:
        final_code = complete_code

     dictt= {"pid":pid,"executionID":executionId,'status': final_code,'statusMessage':'extractregionalactivity ' + status_message + '!','timetaken':start}
     return jsonify(dictt)
 
 
 
from functional_connectivity_extraction import functional_connectivity
@app.route('/brainsightai/extractfunctionalconnectivity',methods = ['POST'])
def extract_functional_connectivity():
     pid = request.json['pid']
     executionId = request.json['executionID']	
     
     complete_code, status_message = functional_connectivity(pid, executionId)
     if complete_code == 0:
        final_code = 200
        status_message = "COMPLETE"
     else:
        final_code = complete_code

     dictt= {"pid":pid,"executionID":executionId,'status': final_code,'statusMessage':'extractfunctionalconnectivity ' + status_message + '!','timetaken':start}
     return jsonify(dictt)
 
 

from create_multidata_dict_file import create_multidata_dict
@app.route('/brainsightai/createstructuralfunctionalmultidict',methods = ['POST'])
def create_structural_functional_multidict():
     pid = request.json['pid']
     executionId = request.json['executionID']	
     complete_code, status_message = create_multidata_dict(pid, executionId)
     if complete_code == 0:
        final_code = 200
        status_message = "COMPLETE"
     else:
        final_code = complete_code

     dictt= {"pid":pid,"executionID":executionId,'status': final_code,'statusMessage':'createstructuralfunctionalmultidict ' + status_message + '!','timetaken':start}
     return jsonify(dictt)




from ml_model_inference import run_ml_algo
@app.route('/brainsightai/mlinferenceplots',methods = ['POST'])
def ml_inference_plots():
	
     pid = request.json['pid']
     executionId = request.json['executionID']	

     complete_code, status_message = run_ml_algo(pid, executionId)
     if complete_code == 0:
        final_code = 200
        status_message = "COMPLETE"
     else:
        final_code = complete_code

     dictt= {"pid":pid,"executionID":executionId,'status': final_code,'statusMessage':'mlinferenceplots ' + status_message + '!','timetaken':start}
     return jsonify(dictt)

            
            
                                                
if __name__ == '__main__':
       app.run(debug = True)

