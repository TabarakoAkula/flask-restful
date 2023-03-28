from flask import Flask
from data import db_session
from data.works import Works

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init('db/blogs.db')
    db_sess = db_session.create_session()
    works = Works()
    db_sess.add(works)
    db_sess.commit()


if __name__ == '__main__':
    main()