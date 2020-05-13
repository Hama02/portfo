from flask import Flask,render_template,request,redirect
import csv
app = Flask(__name__)

def write_to_file(data):
    with open('database.txt',mode='a') as file:
        for key,value in data.items():
            file.write(f'{key} : {value} ; \n')

def write_to_csv(data):
    with open('database.csv',mode='a') as file1:
        csv_writer = csv.writer(file1,delimiter=';',
            quotechar='/',quoting=csv.QUOTE_MINIMAL)
        for key,value in data.items():
            csv_writer.writerow([key,value])


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        write_to_csv(data)
        return redirect('/ty.html')
    else:
        return 'something get wrong ... try later '
