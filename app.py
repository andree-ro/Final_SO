from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    student_data = {
        "name": "Andreé Robles",
        "carnet": "1523820",
        "university": "Universidad Rafael Landivar",
        "faculty": "Facultad de Ingeniería",
        "course": "Ingeniería de Sistemas"
    }
    return render_template('index.html', data=student_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
