from app.database import SessionLocal, engine, Base
from app import models
from app.auth import get_password_hash

Base.metadata.create_all(bind=engine)

db = SessionLocal()

# create departments
sales = models.Department(name='Sales')
cs = models.Department(name='CustomerService')
hr = models.Department(name='HR')

for d in [sales, cs, hr]:
    db.add(d)

db.commit()

# create keywords
kws = [
    models.Keyword(word='mua', department_id=sales.id),
    models.Keyword(word='bảo hành', department_id=cs.id),
    models.Keyword(word='nghỉ', department_id=hr.id),
]
for k in kws:
    db.add(k)

# create admin user
admin = models.User(username='admin', full_name='Administrator', hashed_password=get_password_hash('adminpass'), role=models.RoleEnum.admin)
manager = models.User(username='manager', full_name='Manager', hashed_password=get_password_hash('managerpass'), role=models.RoleEnum.manager, department_id=cs.id)
staff1 = models.User(username='staff1', full_name='Staff One', hashed_password=get_password_hash('staff1pass'), role=models.RoleEnum.staff, department_id=cs.id, kpi_score=95.0)
staff2 = models.User(username='staff2', full_name='Staff Two', hashed_password=get_password_hash('staff2pass'), role=models.RoleEnum.staff, department_id=sales.id, kpi_score=88.0)

for u in [admin, manager, staff1, staff2]:
    db.add(u)

db.commit()
print('Seeded DB')
