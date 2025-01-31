from flask import Flask,render_template, request, redirect,Response
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import datetime
import pathlib
from flask import send_file

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class Site(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    intro = db.Column(db.String(300), nullable= False)
    title = db.Column(db.String(300), nullable= False)
    text = db.Column(db.Text, nullable= False)
    img = db.Column(db.Text, unique=True , nullable= False)
    name = db.Column(db.Text, unique=True , nullable= False)
    mimetype = db.Column(db.Text, nullable= False)
    timepost = db.Column(db.Text, nullable= False)


# @app.route("/t")
# def test():
#     return render_template("test.html")

@app.route("/")
@app.route("/index")
def index():
    c = Site.query.order_by(Site.id.desc()).first()
    last = c.id
    lasta = last - 1
    lastb = last - 2
    fposts = Site.query.filter(Site.id == last)
    posta = Site.query.filter(Site.id == lasta)
    postb = Site.query.filter(Site.id == lastb)
    return render_template("index.html", fposts=fposts, posta=posta, postb=postb
                           )

@app.route('/tls/cit.csr')
def download_file():
    return send_file("tls/cit.csr")

@app.route("/contacts")
def main():
    c = Site.query.order_by(Site.id.desc()).first()
    last = c.id
    fposts= Site.query.filter(Site.id ==last)
    posts=Site.query.filter(Site.id < last)
    return render_template("contacs.html", fposts = fposts, posts=posts)


@app.route("/vakancy/1")
def vakancy1():
    return render_template("vakancy1.html")


@app.route("/corup")
def corup():
    return render_template("corup.html")


@app.route ("/corup1")
def corup1():
    return render_template("corup1.html")

@app.route ("/corup2")
def corup2():
    return render_template("corup2.html")

@app.route ("/corup3")
def corup3():
    return render_template("corup3.html")

@app.route ("/corup4")
def corup4():
    return render_template("corup4.html")

@app.route ("/corup5")
def corup5():
    return render_template("corup5.html")

@app.route("/vakancy")
def vakancy():
    return render_template("vakancy.html")


@app.route("/posts")
def posts():
    posts = Site.query.order_by(Site.id.desc()).all()
    return render_template("posts.html", posts=posts)


@app.route("/posts/<int:id>")
def posts_detail(id):
    posts = Site.query.get(id)
    return render_template("posts_detail.html", posts=posts)


@app.route("/posts/<int:id>/del")
def posts_del(id):
    posts = Site.query.get_or_404(id)
    return render_template("posts_detail.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route ("/medianews")
def laws():
    posts = Site.query.order_by(Site.id.desc()).all()
    return render_template("medianews.html", posts=posts)


@app.route ("/ustav")
def ustav():
    return render_template("ustav.html")


@app.route ("/KJNO")
def KJNO():
    return render_template("KJNO.html")


@app.route ("/APKBG")
def APKBG():
    return render_template("APKBG.html")

# @app.route ("/otchet")
# def otchet():
#     return render_template("otchet.html")


@app.route ("/success")
def success():
    return render_template("success.html")

@app.route ("/create", methods =['POST', 'GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']
        pic = request.files['pic']
        name = secure_filename(pic.filename)
        mimetype = pic.mimetype
        now = datetime.datetime.utcnow()
        timepost = now.strftime("%d.%m.%Y")

        post = Site(title=title, text=text,intro=intro,img=pic.read(), name=name,mimetype=mimetype,timepost=timepost)

        try:
            db.session.add(post)
            db.session.commit()
            return redirect("/success")
        except:
            return 'При добавлении поста произошла ошибка'
    else:
        return render_template("create.html")


@app.route ("/<int:id>")
def get_img(id):
    img=Site.query.filter_by(id=id).first()
    if not img:
        return 'Нет изображения с таким id', 404

    return Response(img.img, mimetype=img.mimetype)

@app.route ("/region")
def region():
    return render_template("region.html")


@app.route("/project")
def project():
    return render_template("project.html")


@app.route("/digital_zabota")
def digital_zabota():
    return render_template("digital_zabota.html")


@app.route("/digital_tech")
def digital_tech():
    return render_template("digital_tech.html")


# @app.route ("/logo.ico")
# def get_img_logo():
#      return render_template ("logo.html")



# @app.route("/bisnes")
# def bisnes():
#     return render_template("bisnes.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
