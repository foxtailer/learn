from flask import Flask, render_template, request
import calendar, datetime
import random


_year = None
_month = None

app = Flask(__name__)

def get_month(year, month):
    cal = []
    element_values = []
    curent_month = True
    _date = datetime.datetime.now()

    if (year and month) and month != _date.month :
        curent_month = False

    if curent_month:
        [cal.extend(item) for item in calendar.Calendar().monthdayscalendar(_date.year, _date.month)]
    else:
        [cal.extend(item) for item in calendar.Calendar().monthdayscalendar(year, month)]
    
    # Create list of tuples[(day#,empty_class,busy of day)]
    for i in range(35):
        element_values.append((cal[i],"_",random.randint(0,100)))
    if curent_month:
        for i in range(35):
            if element_values[i][0]==_date.day:
                temp = list(element_values[i])
                temp[1]="current-day"
                element_values[i] = tuple(temp)
    # last element in cal is tuple (day name, day, month_name, year, month)
    element_values.append((_date.strftime("%A"), _date.day, _date.strftime("%B"), _date.year, _date.month) if curent_month else (0,0,calendar.month_name[month],year,month))

    return element_values


@app.route("/", methods=['GET', 'POST'])
def home():
    global _month, _year
    if request.method == "POST":
        request_data = request.get_json()
        _month = int(request_data["month"])
        _year = int(request_data["year"])
        if _month > 12:
            _month = 12
        return ";p;"
    else:
        element_values = get_month(_year, _month)
        return render_template('index.html', element_values=element_values)


if __name__ == "__main__":
    app.run(debug=True)
   