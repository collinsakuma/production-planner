from app import app
from models import db, Route

if __name__ == '__main__':
    with app.app_context():
        print("seeding data...")
        Route.query.delete()
        print("data seeded...")

    route_one = Route(
        tool_type = "endmill",
        coating_type = "Varianta Supral (C09)",
        step_1 = "EMG",
        step_2 = "EP",
        step_3 = "PO",
    )

    db.session.add_all([route_one, ])
    db.session.commit()