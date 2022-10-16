from flask import Flask, render_template, request
import 추천

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/post', methods=['POST'])
def post():
    if request.method == 'POST':
        value = str(request.form['games'])
        추천1 = str(추천.추천(value))
        with open('items.txt','a',encoding='utf-8') as file_data:
            file_data.write(value+"\n")
    return 추천1

app.run(host='0.0.0.0',port=80)