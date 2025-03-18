from flask import Flask, request, render_template, jsonify
from project_app.utils import MedicalInsurance

app = Flask(__name__)

@app.route('/')
def ABC():
    return render_template('index.html')

####################################################################

@app.route('/get_insurance_charges', methods = ['POST'])
def get_insurance_charges():
     data = request.form  # dictionary
     print("Data is : ",data)

     age = float(data.get('age'))  
     gender = data.get('gender')
     bmi = float(data.get('bmi'))
     children = int(data.get('children'))
     smoker = data.get('smoker')
     region = data.get('region')

     #med_ins = MedicalInsurance(age,gender,bmi,children,smoker,region)
     #charges = med_ins.get_predict_charges()
     
     #return jsonify({"Result" : f"Predicted Medical Insurance Charges are: {charges}"})

     med_ins = MedicalInsurance(age, gender, bmi, children, smoker, region)
     charges = med_ins.get_predict_charges()

     return render_template('result.html', prediction=round(charges[0], 2))

app.run(debug = True)