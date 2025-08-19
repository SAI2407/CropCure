
from class_predict import Predict
from model import model
from model import leaf_model

device = "cpu"
disease_class_names = ['Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy']
leafmodel_class_names = ['leaf', 'Not_leaf']
def predict(transformed_img) :
    leafNotleaf = Predict(transformed_img , leaf_model , device  , leafmodel_class_names )
    if leafNotleaf[0] == 'Not_leaf' :
        result = ("Not a leaf", 1.0, {}) 
    else :
        result = Predict(transformed_img, model, device , disease_class_names)

    return result
        
   