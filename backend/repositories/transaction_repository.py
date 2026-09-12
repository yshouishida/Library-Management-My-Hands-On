from backend.database.connection import get_connection


def add_transaction(book_id, borrower_id, date_due):
    conn = None

    try:
        conn = get_connection()

        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT id FROM tblBooks WHERE id = %s
                """,
                (book_id,)
            )
            if cursor.fetchone() is None:
                return False

            cursor.execute(
                """
                SELECT id FROM tblBorrowers WHERE id = %s
                """,
                (borrower_id,)
            )
            if cursor.fetchone() is None:
                return False

            cursor.execute(
                """
                INSERT INTO tblTransaction
                    (book_id, borrower_id, date_due)
                VALUES 
                    (%s, %s, %s)
                """,
                (
                     book_id,
                     borrower_id,
                     date_due
                )
            )
            conn.commit()
            return True

    except Exception as e:
        if conn: conn.rollback()
        print(f"Error: {e}")
    finally:
        if conn: conn.close()