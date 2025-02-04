# ruleid: sqlalchemy-sql-injection
def bad1(var):
    session.query(MyClass).distinct("foo={}".format(var))

# ruleid: sqlalchemy-sql-injection
def bad2(var):
    query = cls.query.join(DeploymentPermission).having(
        "oops{}".format(var)
    )

# ruleid: sqlalchemy-sql-injection
def bad3(var):
    query = cls.query.group_by(
        "oops{}".format(var)
    )
