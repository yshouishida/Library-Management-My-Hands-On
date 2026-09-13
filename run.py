from backend import create_app
from backend.database.connection import get_connection

app = create_app()



if __name__ == "__main__":
    app.run(debug=True)