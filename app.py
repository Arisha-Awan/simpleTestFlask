from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        return render_template_string('''
            <!doctype html>
            <title>Display Input</title>
            <h1>Your Input: {{ user_input }}</h1>
            <a href="/">Go Back</a>
        ''', user_input=user_input)
    return render_template_string('''
        <!doctype html>
        <title>Input Form</title>
        <h1>Enter Something</h1>
        <form method="post">
            <input type="text" name="user_input">
            <input type="submit" value="Submit">
        </form>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
