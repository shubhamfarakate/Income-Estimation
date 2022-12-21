from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('income_gradboost.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():

    if request.method == 'POST':
        
        age = int(request.form['age'])
        
        fnlwgt = float(request.form['fnlwgt'])
        
        hours_per_week = float(request.form['hours_per_week'])
        
        education_num = float(request.form['education_num'])
        
        capital_gain = int(request.form['capital_gain'])
        
        capital_loss = int(request.form['capital_loss'])
        
        
        
        Gender = request.form['Gender']
        if (Gender == 'Male'):
            sex_Male = 1
            
        else :
            sex_Male = 0
            
        
        Race = request.form['Race']
        if (Race == 'race_Asian_Pac_Islander'):
            race_Asian_Pac_Islander = 1
            race_Black = 0
            race_Other = 0
            race_White = 0
            
        elif (Race == 'race_Black'):
            race_Asian_Pac_Islander = 0
            race_Black = 1
            race_Other = 0
            race_White = 0
            
        elif (Race == 'race_Other'):
            race_Asian_Pac_Islander = 0
            race_Black = 0
            race_Other = 1
            race_White = 0
            
        elif (Race == 'race_White'):
            race_Asian_Pac_Islander = 0
            race_Black = 0
            race_Other = 0
            race_White = 1
            
        else:
            race_Asian_Pac_Islander = 0
            race_Black = 0
            race_Other = 0
            race_White = 0
            
        
        Relationship = request.form['Relationship']
        if (Relationship == 'relationship_Not_in_family'):
            relationship_Not_in_family = 1
            relationship_Other_relative = 0
            relationship_Own_child = 0
            relationship_Unmarried = 0
            relationship_Wife = 0
            
        elif (Relationship == 'relationship_Other_relative'):
            relationship_Not_in_family = 0
            relationship_Other_relative = 1
            relationship_Own_child = 0
            relationship_Unmarried = 0
            relationship_Wife = 0
            
        elif (Relationship == 'relationship_Own_child'):
            relationship_Not_in_family = 0
            relationship_Other_relative = 0
            relationship_Own_child = 1
            relationship_Unmarried = 0
            relationship_Wife = 0
            
        elif (Relationship == 'relationship_Unmarried'):
            relationship_Not_in_family = 0
            relationship_Other_relative = 0
            relationship_Own_child = 0
            relationship_Unmarried = 1
            relationship_Wife = 0
            
        elif (Relationship == 'relationship_Wife'):
            relationship_Not_in_family = 0
            relationship_Other_relative = 0
            relationship_Own_child = 0
            relationship_Unmarried = 0
            relationship_Wife = 1
            
        else:
            relationship_Not_in_family = 0
            relationship_Other_relative = 0
            relationship_Own_child = 0
            relationship_Unmarried = 0
            relationship_Wife = 0
            
        
        Occupation = request.form['Occupation']
        if (Occupation == 'occupation_Armed_Forces'):
            occupation_Armed_Forces = 1
            occupation_Craft_repair = 0
            occupation_Exec_managerial = 0
            occupation_Farming_fishing = 0
            occupation_Handlers_cleaners = 0
            occupation_Machine_op_inspct = 0
            occupation_Other_service = 0
            occupation_Priv_house_serv = 0
            occupation_Prof_specialty = 0
            occupation_Protective_serv = 0
            occupation_Sales = 0
            occupation_Tech_support = 0
            occupation_Transport_moving = 0
            
        elif (Occupation == 'occupation_Craft_repair'):
            occupation_Armed_Forces = 0
            occupation_Craft_repair = 1
            occupation_Exec_managerial = 0
            occupation_Farming_fishing = 0
            occupation_Handlers_cleaners = 0
            occupation_Machine_op_inspct = 0
            occupation_Other_service = 0
            occupation_Priv_house_serv = 0
            occupation_Prof_specialty = 0
            occupation_Protective_serv = 0
            occupation_Sales = 0
            occupation_Tech_support = 0
            occupation_Transport_moving = 0
            
        elif (Occupation == 'occupation_Exec_managerial'):
            occupation_Armed_Forces = 0
            occupation_Craft_repair = 0
            occupation_Exec_managerial = 1
            occupation_Farming_fishing = 0
            occupation_Handlers_cleaners = 0
            occupation_Machine_op_inspct = 0
            occupation_Other_service = 0
            occupation_Priv_house_serv = 0
            occupation_Prof_specialty = 0
            occupation_Protective_serv = 0
            occupation_Sales = 0
            occupation_Tech_support = 0
            occupation_Transport_moving = 0
        
        elif (Occupation == 'occupation_Farming_fishing'):
            occupation_Armed_Forces = 0
            occupation_Craft_repair = 0
            occupation_Exec_managerial = 0
            occupation_Farming_fishing = 1
            occupation_Handlers_cleaners = 0
            occupation_Machine_op_inspct = 0
            occupation_Other_service = 0
            occupation_Priv_house_serv = 0
            occupation_Prof_specialty = 0
            occupation_Protective_serv = 0
            occupation_Sales = 0
            occupation_Tech_support = 0
            occupation_Transport_moving = 0
            
        elif (Occupation == 'occupation_Handlers_cleaners'):
            occupation_Armed_Forces = 0
            occupation_Craft_repair = 0
            occupation_Exec_managerial = 0
            occupation_Farming_fishing = 0
            occupation_Handlers_cleaners = 1
            occupation_Machine_op_inspct = 0
            occupation_Other_service = 0
            occupation_Priv_house_serv = 0
            occupation_Prof_specialty = 0
            occupation_Protective_serv = 0
            occupation_Sales = 0
            occupation_Tech_support = 0
            occupation_Transport_moving = 0
            
        elif (Occupation == 'occupation_Machine_op_inspct'):
            occupation_Armed_Forces = 0
            occupation_Craft_repair = 0
            occupation_Exec_managerial = 0
            occupation_Farming_fishing = 0
            occupation_Handlers_cleaners = 0
            occupation_Machine_op_inspct = 1
            occupation_Other_service = 0
            occupation_Priv_house_serv = 0
            occupation_Prof_specialty = 0
            occupation_Protective_serv = 0
            occupation_Sales = 0
            occupation_Tech_support = 0
            occupation_Transport_moving = 0
            
        elif (Occupation == 'occupation_Other_service'):
            occupation_Armed_Forces = 0
            occupation_Craft_repair = 0
            occupation_Exec_managerial = 0
            occupation_Farming_fishing = 0
            occupation_Handlers_cleaners = 0
            occupation_Machine_op_inspct = 0
            occupation_Other_service = 1
            occupation_Priv_house_serv = 0
            occupation_Prof_specialty = 0
            occupation_Protective_serv = 0
            occupation_Sales = 0
            occupation_Tech_support = 0
            occupation_Transport_moving = 0
            
        elif (Occupation == 'occupation_Priv_house_serv'):
            occupation_Armed_Forces = 0
            occupation_Craft_repair = 0
            occupation_Exec_managerial = 0
            occupation_Farming_fishing = 0
            occupation_Handlers_cleaners = 0
            occupation_Machine_op_inspct = 0
            occupation_Other_service = 0
            occupation_Priv_house_serv = 1
            occupation_Prof_specialty = 0
            occupation_Protective_serv = 0
            occupation_Sales = 0
            occupation_Tech_support = 0
            occupation_Transport_moving = 0
            
        elif (Occupation == 'occupation_Prof_specialty'):
            occupation_Armed_Forces = 0
            occupation_Craft_repair = 0
            occupation_Exec_managerial = 0
            occupation_Farming_fishing = 0
            occupation_Handlers_cleaners = 0
            occupation_Machine_op_inspct = 0
            occupation_Other_service = 0
            occupation_Priv_house_serv = 0
            occupation_Prof_specialty = 1
            occupation_Protective_serv = 0
            occupation_Sales = 0
            occupation_Tech_support = 0
            occupation_Transport_moving = 0
            
        elif (Occupation == 'occupation_Protective_serv'):
            occupation_Armed_Forces = 0
            occupation_Craft_repair = 0
            occupation_Exec_managerial = 0
            occupation_Farming_fishing = 0
            occupation_Handlers_cleaners = 0
            occupation_Machine_op_inspct = 0
            occupation_Other_service = 0
            occupation_Priv_house_serv = 0
            occupation_Prof_specialty = 0
            occupation_Protective_serv = 1
            occupation_Sales = 0
            occupation_Tech_support = 0
            occupation_Transport_moving = 0
            
        elif (Occupation == 'occupation_Sales'):
            occupation_Armed_Forces = 0
            occupation_Craft_repair = 0
            occupation_Exec_managerial = 0
            occupation_Farming_fishing = 0
            occupation_Handlers_cleaners = 0
            occupation_Machine_op_inspct = 0
            occupation_Other_service = 0
            occupation_Priv_house_serv = 0
            occupation_Prof_specialty = 0
            occupation_Protective_serv = 0
            occupation_Sales = 1
            occupation_Tech_support = 0
            occupation_Transport_moving = 0
            
        elif (Occupation == 'occupation_Tech_support'):
            occupation_Armed_Forces = 0
            occupation_Craft_repair = 0
            occupation_Exec_managerial = 0
            occupation_Farming_fishing = 0
            occupation_Handlers_cleaners = 0
            occupation_Machine_op_inspct = 0
            occupation_Other_service = 0
            occupation_Priv_house_serv = 0
            occupation_Prof_specialty = 0
            occupation_Protective_serv = 0
            occupation_Sales = 0
            occupation_Tech_support = 1
            occupation_Transport_moving = 0
            
        elif (Occupation == 'occupation_Transport_moving'):
            occupation_Armed_Forces = 0
            occupation_Craft_repair = 0
            occupation_Exec_managerial = 0
            occupation_Farming_fishing = 0
            occupation_Handlers_cleaners = 0
            occupation_Machine_op_inspct = 0
            occupation_Other_service = 0
            occupation_Priv_house_serv = 0
            occupation_Prof_specialty = 0
            occupation_Protective_serv = 0
            occupation_Sales = 0
            occupation_Tech_support = 0
            occupation_Transport_moving = 1
            
        else:
            occupation_Armed_Forces = 0
            occupation_Craft_repair = 0
            occupation_Exec_managerial = 0
            occupation_Farming_fishing = 0
            occupation_Handlers_cleaners = 0
            occupation_Machine_op_inspct = 0
            occupation_Other_service = 0
            occupation_Priv_house_serv = 0
            occupation_Prof_specialty = 0
            occupation_Protective_serv = 0
            occupation_Sales = 0
            occupation_Tech_support = 0
            occupation_Transport_moving = 0
            
        
        Marital = request.form['Marital']
        if (Marital == 'marital_Married_AF_spouse'):
            marital_Married_AF_spouse = 1
            marital_Married_civ_spouse = 0
            marital_Married_spouse_absent = 0
            marital_Never_married = 0
            marital_Separated = 0
            marital_Widowed = 0
            
        elif (Marital == 'marital_Married_civ_spouse'):
            marital_Married_AF_spouse = 0
            marital_Married_civ_spouse = 1
            marital_Married_spouse_absent = 0
            marital_Never_married = 0
            marital_Separated = 0
            marital_Widowed = 0
            
        elif (Marital == 'marital_Married_spouse_absent'):
            marital_Married_AF_spouse = 0
            marital_Married_civ_spouse = 0
            marital_Married_spouse_absent = 1
            marital_Never_married = 0
            marital_Separated = 0
            marital_Widowed = 0
            
        elif (Marital == 'marital_Never_married'):
            marital_Married_AF_spouse = 0
            marital_Married_civ_spouse = 0
            marital_Married_spouse_absent = 0
            marital_Never_married = 1
            marital_Separated = 0
            marital_Widowed = 0
            
        elif (Marital == 'marital_Separated'):
            marital_Married_AF_spouse = 0
            marital_Married_civ_spouse = 0
            marital_Married_spouse_absent = 0
            marital_Never_married = 0
            marital_Separated = 1
            marital_Widowed = 0
            
        elif (Marital == 'marital_Widowed'):
            marital_Married_AF_spouse = 0
            marital_Married_civ_spouse = 0
            marital_Married_spouse_absent = 0
            marital_Never_married = 0
            marital_Separated = 0
            marital_Widowed = 1
            
        else :
            marital_Married_AF_spouse = 0
            marital_Married_civ_spouse = 0
            marital_Married_spouse_absent = 0
            marital_Never_married = 0
            marital_Separated = 0
            marital_Widowed = 0
            
        Workclass = request.form['Workclass']
        if (Workclass == 'workclass_Local_gov'):
            workclass_Local_gov = 1
            workclass_Private = 0
            workclass_Self_emp_inc = 0
            workclass_Self_emp_not_inc = 0
            workclass_State_gov = 0
            workclass_Without_pay = 0
            
        elif (Workclass == 'workclass_Private'):
            workclass_Local_gov = 0
            workclass_Private = 1
            workclass_Self_emp_inc = 0
            workclass_Self_emp_not_inc = 0
            workclass_State_gov = 0
            workclass_Without_pay = 0
            
        elif (Workclass == 'workclass_Self_emp_inc'):
            workclass_Local_gov = 0
            workclass_Private = 0
            workclass_Self_emp_inc = 1
            workclass_Self_emp_not_inc = 0
            workclass_State_gov = 0
            workclass_Without_pay = 0
            
        elif (Workclass == 'workclass_Self_emp_not_inc'):
            workclass_Local_gov = 0
            workclass_Private = 0
            workclass_Self_emp_inc = 0
            workclass_Self_emp_not_inc = 1
            workclass_State_gov = 0
            workclass_Without_pay = 0
            
        elif (Workclass == 'workclass_State_gov'):
            workclass_Local_gov = 0
            workclass_Private = 0
            workclass_Self_emp_inc = 0
            workclass_Self_emp_not_inc = 0
            workclass_State_gov = 1
            workclass_Without_pay = 0
            
        elif (Workclass == 'workclass_Without_pay'):
            workclass_Local_gov = 0
            workclass_Private = 0
            workclass_Self_emp_inc = 0
            workclass_Self_emp_not_inc = 0
            workclass_State_gov = 0
            workclass_Without_pay = 1
            
        else:
            workclass_Local_gov = 0
            workclass_Private = 0
            workclass_Self_emp_inc = 0
            workclass_Self_emp_not_inc = 0
            workclass_State_gov = 0
            workclass_Without_pay = 0
            
        Country = request.form['Country']
        if (Country == 'United States'):
            is_US = 1
            
        else :
            is_US = 0
            
        education = 0
        Education = request.form['Education']
        if (Country == 'Preschool'):
            education = 0
            
        elif (Country == '1st-4th'):
            education = 0
            
        elif (Country == '5th-6th'):
            education = 0
            
        elif (Country == '7th-8th'):
            education = 1
            
        elif (Country == '9th'):
            education = 1
            
        elif (Country == '10th'):
            education = 1
            
        elif (Country == '11th'):
            education = 2
            
        elif (Country == '12th'):
            education = 2
            
        elif (Country == 'Some-college'):
            education = 2
            
        elif (Country == 'HS-grad'):
            education = 2
            
        elif (Country == 'Bachelors'):
            education = 3
            
        elif (Country == 'Assoc-acdm'):
            education = 3
            
        elif (Country == 'Assoc-voc'):
            education = 3
            
        elif (Country == 'Prof-school'):
            education = 4
            
        elif (Country == 'Masters'):
            education = 5
            
        elif (Country == 'Doctorate'):
            education = 6
            
            
        prediction=model.predict([[education, is_US, workclass_Local_gov, workclass_Private,
       workclass_Self_emp_inc, workclass_Self_emp_not_inc,
       workclass_State_gov, workclass_Without_pay,
       marital_Married_AF_spouse, marital_Married_civ_spouse,
       marital_Married_spouse_absent, marital_Never_married,
       marital_Separated, marital_Widowed, occupation_Armed_Forces,
       occupation_Craft_repair, occupation_Exec_managerial,
       occupation_Farming_fishing, occupation_Handlers_cleaners,
       occupation_Machine_op_inspct, occupation_Other_service,
       occupation_Priv_house_serv, occupation_Prof_specialty,
       occupation_Protective_serv, occupation_Sales,
       occupation_Tech_support, occupation_Transport_moving,
       relationship_Not_in_family, relationship_Other_relative,
       relationship_Own_child, relationship_Unmarried,
       relationship_Wife, race_Asian_Pac_Islander, race_Black,
       race_Other, race_White, sex_Male, age, fnlwgt,
       education_num, capital_gain, capital_loss, hours_per_week]])

        
                    
        output = prediction

        if output == 0:
            return render_template('index.html',prediction_text="Income of the person is less than $50k per year")
        elif output == 1:
            return render_template('index.html',prediction_text="Income of the person is more than $50k per year")
    else:
        return render_template('index.html')
            
        

if __name__=="__main__":
    app.run(debug=True)
