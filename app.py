from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def maintenance_calc():
    title = "Maintenance Calorie Calculator"
    return render_template('calc.html', title=title)

@app.route('/result', methods=['POST'])
def calc_result():
    title= "Maintenance Calories"
    weight = request.form.get('weight')
    height = request.form.get('height')
    age = request.form.get('age')
    gender = request.form.get('gender')
    activityLevel = request.form.get('activityLevel')
    if not weight or not height or not age or not gender or not activityLevel:
        error_statement = "All form fields Required"
        return render_template('calc.html',
        error_statement=error_statement,
        weight = weight,
        height = height,
        age = age,
        gender = gender,
        activityLevel = activityLevel)

    weight = int(weight)
    height = int(height)
    age = int(age)
    gender = str(gender)
    activityLevel = str(activityLevel.split(") ")[0])

    if gender == 'Male':
        BMR = 66 + (6.3 * weight) + (12.9 * height) - (6.8 * age)
# IF female formula for BMR is:
    # 665 + (4.3 * weight in lbs.) + (4.7 * height in inches) - (4.7 * age in years)
    elif gender == 'Female':
        BMR = 665 + (4.3 * weight) + (4.7 * height) - (4.7 * age)

    if activityLevel == '1':
        MainCalorie = BMR * 1.2
    elif activityLevel == '2':
        MainCalorie = BMR * 1.375
    elif activityLevel == '3':
        MainCalorie = BMR * 1.55
    elif activityLevel == '4':
        MainCalorie = BMR * 1.725
    elif activityLevel == '5':
        MainCalorie = BMR * 1.9
    return render_template('result.html', title=title, MainCalorie=round(MainCalorie,))

if __name__ == '__main__':
    app.run(debug=True)
