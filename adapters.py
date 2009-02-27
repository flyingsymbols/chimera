import psycopg2
import psycopg2.extensions
from psycopg2.extensions import adapt, register_adapter

class AsIs(object):
    def __init__(self, s):
        self.s = s

    def getquoted(self):
        return self.s

class SQL_IN(object):
    def __init__(self, iterable):
        self.iterable = iterable

#    def prepare(self, conn): #included as doc
#        pass

    def getquoted(self):
        quoted_iter = [str(adapt(o).getquoted()) for o in self.iterable]
        return '(' + ', '.join(quoted_iter) + ')'

class PsqlBareString(str):
    pass

class PsqlInList(list):
    pass

register_adapter(PsqlBareString, AsIs)
register_adapter(PsqlInList, SQL_IN)
