from data import db_session, f111_api
from flask import Flask
from data.categories import Category




app = Flask(__name__)

categories = ['mf', 'mm', 'ff', 'fm', 'massage']




@app.route('/')
@app.route('/index')
def index():
    return "Привет, Яндекс!"


def main():
    db_session.global_init("db/b_bd.db")
    db_sess = db_session.create_session()
    if not db_sess.query(Category).all():
        for i in categories:
            category = Category()
            category.name = i
            category.count = 0
            db_sess.add(category)
            db_sess.commit()
    app.register_blueprint(f111_api.blueprint)

    app.run(port=5000, host='127.0.0.1')




if __name__ == '__main__':
    main()
