from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play_ground():
    return render_template('index.html') 

@app.route('/play/<int:x>')
def box_repeat(x):
    repeat = x
    return render_template('/index2.html', repeat=repeat)

@app.route('/play/<int:x>/<color>')
def color_change(x,color):
    repeat = x
    color_change = color
    return render_template('/index3.html', repeat=repeat, color_change=color_change)

if __name__=="__main__":
    app.run(debug=True)