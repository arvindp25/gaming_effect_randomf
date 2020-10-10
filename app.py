
from flask import *
import pickle
#import gspread

#gc = gspread.service_account(filename = "cred.json")
#sh = gc.open_by_key("10Eaw0vi941eOeapiAVvfScrEySvWZBQiP_DmyPTUEfI")

#worksheet = sh.sheet1

app = Flask(__name__, static_url_path='/static')
model = pickle.load(open('game_affecting_model.pkl', 'rb'))
@app.route('/')
def Home():
    return render_template('index.html')
	
@app.route("/add", methods = ['POST'])
def predict():
    if request.method == 'POST':
        Name = request.form['fn']
        Gender = request.form['gender']
        age = int(request.form['age'])
        mean_hours_gaming = int(request.form['mean_hours_gaming'])
        period_considered_as_gamer = int(request.form['period_considered_as_gamer'])
        insonmia = int(request.form['insonmia'])
        daytime_sleep = int(request.form['daytime_sleep'])
        anx = int(request.form['anx'])
        dep = int(request.form['dep'])
        platform = int(request.form['platform'])
		
        prediction = model.predict([[age, mean_hours_gaming, period_considered_as_gamer, insonmia, daytime_sleep, anx,dep,platform]])
        pred = prediction[0]
        out = "Error"
        if pred ==1:out = "Low"
        else: out = "High"
			
		#worksheet.append_row([name ,Gender ,out])
        return render_template('index.html', results = out)
    else:
        return render_template('index.html')
		
		

if __name__ == "__main__":
	app.run(debug = True)
