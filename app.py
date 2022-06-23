from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class Config(object):
    """配置参数"""
    # sqlalchemy的配置参数
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/django_test1"

    # 设置sqlalchemy自动更新跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 连接池大小
    SQLALCHEMY_POOL_SIZE = 10

    # 调试模式，SQLAlchemy 将会记录所有发到标准输出(stderr)的语句，这对调试很有帮助
    SQLALCHEMY_ECHO = True

    # 设置这一项是每次请求结束后都会自动提交数据库中的变动
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


app = Flask(__name__)

# 连接数据库
app.config.from_object(Config)

# 创建数据库aqlalchemy工具对象
db = SQLAlchemy(app)


class Book(db.Model):
    __tablename__ = "test_app1_book"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False)
    pages = db.Column(db.Integer)
    price = db.Column(db.DECIMAL, unique=False)
    publisher_id = db.Column(db.Integer, unique=False)

    def __init__(self, name, pages, price, publisher_id):
        self.name = name
        self.pages = pages
        self.price = price
        self.publisher_id = publisher_id

    def __repr__(self):
        return '<User %r>' % self.name

    def to_json(self):
        json_student = {
            'student_id': self.id,
            'name': self.name,
            'pages': self.pages,
            'price': self.price,
            'publisher_id': self.publisher_id
        }
        return json_student


@app.route('/')
def hello_world():  # put application's code here
    book = db.session.query(Book).first()
    data = book.to_json()
    return data


if __name__ == '__main__':
    app.run()
