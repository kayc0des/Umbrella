from basemodel import Admin
from persisting import session as db_session

superadmin = Admin(username="kayc0des", email="k.boafo@alustudent.com", password="umbrella")
db_session.add(superadmin)
db_session.commit()
