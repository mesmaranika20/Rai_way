from database.payroll import db_get_all, db_create

def service_get_all():
    return db_get_all()

def service_create(data):
    return db_create(data)
