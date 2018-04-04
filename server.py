from flask import Flask, render_template
import json

w = json.load(open("worldl.json"))
page_size = 20
app = Flask(__name__)

@app.route('/')
def mainPage():
#    return '<br> '.join([c['name'] for c in w])
    return render_template('index.html', w=w[0:page_size])

@app.route('/begin/<b>')
def beginPage(b):
    bn = int(b)
    return render_template('index.html', w=w[bn:bn+page_size],
                           page_number = bn,
                           page_size = page_size
                           )

@app.route('/continent/<a>')
def continentPage(a):
    cl= [c for c in w if c['continent']== a] 
    return render_template(
        'continent.html', len_of_cl = len(cl),
        cl = cl,
        a = a
        )

@app.route('/country/<i>')
def countryPage(i):
#    return w[int(i)]['name'] + w[int(i)]['continent'] + w[int(i)]['capital']
    return render_template('country.html', c= w[int(i)])

@app.route('/countryByname/<n>')
def countryBynamePage(n):
    c=None
    for x in w:
        if x['name']==n:
            c=x
    return render_template('country.html', c= c)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
