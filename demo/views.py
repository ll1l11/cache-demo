# -*- coding: utf-8 -*-
import random
from flask import Blueprint

from .ext import cache


bp = Blueprint('views', __name__)


class UserCache(object):

    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return '{0}({1})'.format(self.__class__.__name__, self.id)

    @cache.memoize(timeout=5)
    def get_x(self, a):
        return a + random.random()

    @cache.memoize(timeout=5)
    def get_y(self, a):
        return a + random.random()


@bp.route('/')
def index():
    u = UserCache(3)
    key1 = u.get_x.make_cache_key(u.get_x.uncached, u, 2)
    key2 = u.get_y.make_cache_key(u.get_y.uncached, u, 2)
    print(u.get_x(1), u.get_y(2))
    cache.delete_memoized_verhash(u.get_x)
    print(u.get_x(1), u.get_y(2))
    print('*' * 20, key1, key2)
    return 'index'
