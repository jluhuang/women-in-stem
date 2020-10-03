from flask import Flask, render_template, request, redirect, flash, make_response

app = Flask(__name__, template_folder="templates");

@app.route('/')
def home(): 
    return render_template("HomePage.html")

@app.route('/Timeline')
def timeline(): 
    return render_template("TimelinePageAll.html")

@app.route('/Photo Gallery')
def photo_gallery(): 
    return render_template("PhotoGalleryPage.html")

@app.route('/About Creators')
def about_creators(): 
    return render_template("AboutCreatorsPage.html")

@app.route('/YnesMexia')
def about_Ynes(): 
    return render_template("TimelinePageYnes.html")

@app.route('/JanakiAmmal')
def about_Janaki(): 
    return render_template("TimelinePageAmmal.html")

@app.route('/GraceHopper')
def about_Grace(): 
    return render_template("TimelinePageGrace.html")

@app.route('/MaryRoss')
def about_Mary(): 
    return render_template("TimelinePageMary.html")

@app.route('/ChienWu')
def about_Wu(): 
    return render_template("TimelinePageWu.html")

@app.route('/MaeJemison')
def about_Jemison(): 
    return render_template("TimelinePageMae.html")

if __name__ == '__main__': 
    app.run(debug=True, port=8004)