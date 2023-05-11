import random, string

from flask import Blueprint, render_template, jsonify, request, url_for, redirect, session
from exts import mail
from flask_mail import Message
from models import EmailCaptchaModel, db, UserModel
from .forms import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash

# /auth
bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/login", methods=["GET","POST"])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if not user:
                print("邮箱在数据库中不存在")
                return redirect(url_for("auth.login"))
            if check_password_hash(user.password, password):
                # cookie中不适合存储太多数据，一般用来存放登录授权的东西
                session['user_id'] = user.id
                return redirect("/")
            else:
                print("密码错误!")
                return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for("auth.register"))

        return redirect(url_for("auth.register"))

@bp.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@bp.route("/register", methods=["GET","POST"])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = UserModel(email=email, username=username, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for("auth.register"))

@bp.route("/captcha/email", methods=["GET"])
def get_email_captcha():
    # /captcha/email/<email>
    # /captcha/email?email=xxx@qq.com
    email = request.args.get("email")
    source = string.digits*4
    captcha = random.sample(source, 4)
    captcha = "".join(captcha)
    message = Message(subject="知了传课注册验证码", sender="826329938@qq.com", recipients=["1639796799@qq.com"],
                      body=f"您的验证码是:{captcha}")
    mail.send(message)
    email_captcha = EmailCaptchaModel(email=email, captcha=captcha)
    db.session.add(email_captcha)
    db.session.commit()
    # RESTful API
    # {code: 200/400/500, message: "", data: {}}
    return jsonify({"code":"200", "message":"", "data":None})

@bp.route("/mail/test")
def mail_test():
    message = Message(subject="邮箱测试", sender="826329938@qq.com", recipients=["1639796799@qq.com"], body="这是一条测试邮件")
    mail.send(message)
    return "邮件发送成功"