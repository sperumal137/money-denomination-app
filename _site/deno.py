from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_denominations(notes):
    denominations = [500, 200, 100, 50, 20, 10]
    result = {}
    total_amount = 0
    for denom in denominations:
        count = int(notes.get(str(denom), 0))
        if count > 0:
            result[denom] = count
            total_amount += denom * count
    return result, total_amount

@app.route('/', methods=['GET', 'POST'])
def index():
    breakdown = {}
    total = 0
    if request.method == 'POST':
        notes = request.form
        breakdown, total = calculate_denominations(notes)
    return render_template('index.html', breakdown=breakdown, total=total)

if __name__ == '__main__':
    app.run(debug=True)
