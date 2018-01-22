# -*- coding: utf-8 -*-


from datetime import datetime

from .user import User


class Todo(object):
    _todo = None
    _user = None
    _is_done = False
    _created = None

    @property
    def user(self):
        print('get user')
        return self._user

    @user.setter
    def user(self, value):
        print('set user', value)
        assert isinstance(value, User)
        value.add_todo(self)
        self._user = value

    @property
    def todo(self):
        print('get todo')
        return self._todo

    @todo.setter
    def todo(self, value):
        print('set todo', value)
        assert isinstance(value, str)
        self._todo = value

    @property
    def created(self):
        print('get created')
        return self._created

    @created.setter
    def created(self, value):
        print('set created', value)
        assert isinstance(value, datetime)
        self._created = value

    @property
    def is_done(self):
        print('get is_done')
        return self._is_done

    @is_done.setter
    def is_done(self, value):
        print('set is_done', value)
        assert isinstance(value, bool)
        self._is_done = value

    def __repr__(self):
        return '{self.todo} {self.user}'.format(self=self)
