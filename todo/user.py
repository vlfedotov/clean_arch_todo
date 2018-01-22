# -*- coding: utf-8 -*-


class User(object):
    _first_name = None
    _last_name = None
    _todos = []

    @property
    def first_name(self):
        print('get first')
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        assert isinstance(value, str)
        print('set first', value)
        self._first_name = value

    @property
    def last_name(self):
        print('get last')
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        assert isinstance(value, str)
        print('set last', value)
        self._last_name = value

    def add_todo(self, todo):
        self._todos.append(todo)

    def del_todo(self, todo):
        self._todos.remove(todo)

    @property
    def undone_todos(self):
        return [todo for todo in self._todos if not todo.is_done]

    def __repr__(self):
        return '{self.first_name} {self.last_name}'.format(self=self)
