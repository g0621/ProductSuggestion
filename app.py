# importing modules
from flask import Flask, render_template, request
import s_main

# declaring app name
app = Flask(__name__)

items = s_main.generate_random_products()

def reset():
    global items
    items = s_main.generate_random_products()



@app.route('/')
def homepage():
    # returning index.html and listasc
    # and length of list to html pagecassdf
    return render_template("index.html", len=len(items), items=items, to_show = False)


@app.route('/send', methods=['GET','POST'])
def send():
    if request.method == 'POST':
        onews = int(request.form['pid'])
        res = s_main.get_recomendattions(onews)
        return render_template("index.html", len=len(items), items=items, to_show = True,len1 = len(res),res = res)
    return render_template("index.html", len=len(items), items=items, to_show = False)

@app.route('/reset', methods=['GET','POST'])
def rset():
    if request.method == 'POST':
        reset()
        return render_template("index.html", len=len(items), items=items, to_show = False)
    return render_template("index.html", len=len(items), items=items, to_show = False)


if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
