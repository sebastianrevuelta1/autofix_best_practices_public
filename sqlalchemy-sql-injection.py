# ruleid: sqlalchemy-sql-injection
def bad1(var):
    session.query(MyClass).distinct("foo={}".format(var))
