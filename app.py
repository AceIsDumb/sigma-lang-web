from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/dimini/')
@app.route('/dimini')
def diminipage():
    return render_template('dimini.html')

@app.route('/syntax/')
@app.route('/syntax')
def syntax():
    return render_template('syntax.html')

if __name__ == "__main__":
    devmode = True
    if devmode:
        app.run(debug=True)
    else:
        from waitress import serve
        serve(app, host="0.0.0.0", port=7272)