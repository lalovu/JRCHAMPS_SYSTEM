from website import create_app, db  # Import the create_app function and db from your package
from flask_migrate import Migrate

app = create_app()  # Initialize the app using the create_app function
migrate = Migrate(app, db)  # Initialize Migrate with the app and db instances

if __name__ == '__main__':
    app.run(debug=True)
