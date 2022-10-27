from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def index():
    get_arg = lambda x: request.args.get(x, '')
    
    day = get_arg('day')
    month = get_arg('month')
    year = get_arg('year')
    date_str = f"{day}/{month}/{year}"
    
    try:
            date = datetime.strptime(date_str, "%d/%m/%Y")
            date += timedelta(days=1)
            res = date.strftime("%d %B %Y")
    except Exception as e:
        res = "Something went wrong... Check your input"
    
    if date_str == "//":
        res = None
        
    return render_template('index.html', answer=res)

@app.route('/v2/')
def v2():
    get_arg = lambda x: request.args.get(x, '')
    
    day = get_arg('day')
    month = get_arg('month')
    year = get_arg('year')
    date_str = f"{day}/{month}/{year}"
    
    try:
            date = datetime.strptime(date_str, "%d/%m/%Y")
            date += timedelta(days=1)
            res = date.strftime("%d %B %Y")
    except Exception as e:
        res = "Something went wrong... Check your input"
    
    if date_str == "//":
        res = None
    
    if day == '28' and month == '2':
        res = f'29 February {year}'
        
    return render_template('index2.html', answer=res)