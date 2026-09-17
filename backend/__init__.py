from flask import Flask


def create_app():
    app = Flask(__name__)

    try:
        from backend.route.book_route import book_bp
        from backend.route.borrower_route import borrowers_bp
        from backend.route.transation_route import transaction_bp

        app.register_blueprint(book_bp)
        app.register_blueprint(borrowers_bp)
        app.register_blueprint(transaction_bp)

        return app
    except Exception as e:
        print(f"Error: {e}")