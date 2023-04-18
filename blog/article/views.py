from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from blog.user.views import get_username

article = Blueprint('article', __name__, url_prefix='/articles', static_folder='../static')

ARTICLES = {
    1: {
        "title": "Time for time",
        "text": "many texts",
        "author": 2
    },
    2: {
        "title": "Time for relax",
        "text": "more texts",
        "author": 2
    },
    3: {
        "title": "Cry In floor",
        "text": "not many texts",
        "author": 1
    },
    4: {
        "title": "Crying floor",
        "text": "fantasy is end",
        "author": 3
    }
}


@article.route('/')
def article_list():
    return render_template('articles/list.html', articles=ARTICLES)


@article.route('/<int:pk>')
def get_article(pk: int):
    try:
        article_raw = ARTICLES[pk]
    except:
        raise NotFound(f'Article id:{pk} not found')
    context = {
        'title': article_raw['title'],
        'text': article_raw['text'],
        'author': get_username(article_raw['author']),
        'id': article_raw['author']
    }
    return render_template('articles/details.html', context=context)
