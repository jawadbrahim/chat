from database.postgres import db
from helpers.app_creation import create_app
from flask_migrate import Migrate

app=create_app(db)
migrate=Migrate(app,db)
if __name__ == "__main__":
    app.run(debug=True)
