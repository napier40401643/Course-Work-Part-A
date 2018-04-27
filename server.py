from flask import Flask, render_template, request
import json

page_number = 10
w = json.load(open("worldl.json"))
alph = sorted(list(set([c['name'][0] for c in w])))
print(alph)

for c in w:
        c['tld'] = c['tld'][1:]
page_size = 25
app = Flask(__name__)

@app.route('/')
def mainPage():
    return render_template('main.html', page_number=0, w=w[0:page_size],
                           page_size=page_size, alph=alph)

@app.route('/Begin/<m>')
def BeginPage(m):
    num = int(m)
    return render_template('main.html', w=w[num:num+page_size],
                           page_number = num,
                           page_size = page_size,
                           alph=alph
                           )

@app.route('/Country/<cty>')
def CountryPage(cty):
#    return w[int(i)]['name'] + w[int(i)]['continent'] + w[int(i)]['capital']
    return render_template('For_Country.html', c= w[int(cty)])


@app.route('/continent/<con>')
def continentPage(con):
    cl= [c for c in w if c['continent']== con] 
    return render_template(
        'For_Continent.html', len_of_cl = len(cl),
        cl = cl,
        con = con,
        alph=alph
        )

@app.route('/CountryName/<C_Name>')
def CountryNamePage(C_Name):
    c=None
    for n in w:
        if n['name']==C_Name:
            c=n
    return render_template('For_Country.html', c= c)


@app.route('/EditCountryName/<C_Name>')
def EditCountryNamePage(C_Name):
    c=None
    for n in w:
        if n['name']==C_Name:
            c=n
    return render_template('For_CountryEdit.html', c= c)


@app.route('/UpdateCountryName')
def UpdateCountryNamePage():
    C_Name = request.args.get('name')
    c=None
    for n in w:
        if n['name'] == C_Name:
            c = n
    c['capital'] = request.args.get('capital')
    c['continent'] = request.args.get('continent')
    return render_template('For_CountryEdit.html', c = c)


@app.route('/DeleteCountry/<C_Name>')
def DeleteCountryPage(C_Name):
    i=0
    for c in w:
        if c['name']==C_Name:
            break
        i=i+1
    del w[i]
    return render_template('main.html',
                           page_number = 0,
                           page_size = page_size,
                           w=w[0:page_size])

@app.route('/CreateCountry')
def CreateCountryByPage():
    c=None   
    return render_template('For_CreateCountry.html', c=c)

@app.route('/SaveCountry')
def SaveCountryByPage():
    c={}
    c['name'] = request.args.get('name')
    c['capital'] = request.args.get('capital')
    c['continent'] = request.args.get('continent')
    c['population'] = request.args.get('population')
    c['tld'] = request.args.get('tld')
    c['area'] = request.args.get('area')
    c['gdp'] = int(request.args.get('gdp'))
    w.append(c)
    return render_template('For_Country.html', c=c)     

@app.route('/ForAlphabetic/<con>')
def ForAlphabetic(con):
    cl= [c for c in w if c['name'] [0]== con] 
    return render_template(
        'For_Continent.html', len_of_cl = len(cl),
        cl = cl,
        con = con,
        alph = alph
        )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5643, debug=True)
