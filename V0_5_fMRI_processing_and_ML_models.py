# BrainSight.AI's fMRI pipeline - Main file

# import libraries
from nilearn import plotting
import subprocess
#get_ipython().run_line_magic('matplotlib', 'inline')

# Time to run the program
import timeit
start = timeit.default_timer()

# extract regional activity features
from regional_activity_extraction import regional_activity
def extract_regional_activity(pid, executionID):
	
	# Extract regional activity features
	complete_code, status_message = regional_activity(pid, executionID)
	if complete_code == 0:
		final_code = 200
		status_message = "COMPLETE"
	else:
		final_code = complete_code

	return final_code, status_message

# extract functional connectivity features
from functional_connectivity_extraction import functional_connectivity
def extract_functional_connectivity(pid, executionID):
	
	# Extract functional connectivity features
	complete_code, status_message = functional_connectivity(pid, executionID)
	if complete_code == 0:
		final_code = 200
		status_message = "COMPLETE"
	else:
		final_code = complete_code

	return final_code, status_message


# merge all regional and functional features into a single create pickle file
from create_multidata_dict_file import create_multidata_dict
def create_structural_functional_multidict(pid, executionID):
	
	# combine regional activity and functional connectivity features into a single file
	complete_code, status_message = create_multidata_dict(pid, executionID)
	if complete_code == 0:
		final_code = 200
		status_message = "COMPLETE"
	else:
		final_code = complete_code

	return final_code, status_message


from ml_model_inference import run_ml_algo
# Calculate classification accuracy and output inference
def ml_inference_plots(pid, executionID):
	
	# combine regional activity and functional connectivity features into a single file
	complete_code, status_message = run_ml_algo(pid, executionID)
	if complete_code == 0:
		final_code = 200
		status_message = "COMPLETE"
	else:
		final_code = complete_code

	return final_code, status_message


#ml_inference_plots('123456788', '261120201244')


#output_values = subprocess.check_output(['python', 'ML_algorithm.py'])
#output_values = str(output_values)[2:-3]
#print(output_values)
#with open("output/Results.txt", "w") as text_file:
#        text_file.write("Classification: %s" % output_values)


