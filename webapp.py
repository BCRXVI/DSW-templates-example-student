from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/") #annotation tells the URL that will amek this function run
def render_main():
    return render_template('home.html')

@app.route("/p1")
def render_page1():
    return render_template('page1.html')

@app.route("/p2")
def render_page2():
    return render_template('page2.html')
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
