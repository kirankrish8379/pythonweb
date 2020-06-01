import csv
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<page>')
def html_page(page=None):
    return render_template(page)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit():
	try:
		userdata = request.form.to_dict()
	#print(userdata)
		uname = userdata['name']
		write_to_db(userdata)
	except Exception as err:
		print(err)
		return 'something went wrong!!!'
	else:
		return render_template('thankyou.html', name=uname)

def write_to_db(userdata):
	with open('./database.csv', 'a', newline='') as cs:
		field_names = ['name','email','subject','message']
		csvwriter = csv.DictWriter(cs, fieldnames=field_names)
		csvwriter.writerow(userdata)



