from backend.database.connection import get_connection
from backend.utils.api_response import error


def get_books_repo():
    conn = None

    try:
        conn = get_connection()

        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT
                    id, 
                    title,
                    author,
                    year_published,
                    genre
                FROM tblBooks
                """
            ),
        return cursor.fetchall()
    
    except Exception as e:
        error("Internal error", 500, e)
    finally:
        if conn: conn.close()

def get_by_id_repo(id):
    conn = None

    try:
        conn = get_connection()

        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT
                    id, 
                    title,
                    author,
                    year_published,
                    genre
                FROM tblBooks
                WHERE id = %s
                """,
                (id,)
            )
        return cursor.fetchone()
    
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn: conn.close()

def add_book_repo(title, author, year_published, genre):
    conn = None

    try:
        conn = get_connection()

        with conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO tblBooks
                    (title, author, year_published, genre)
                VALUES
                    (%s, %s, %s, %s)
                """,
                (
                    title, author, year_published, genre
                )
            )
        conn.commit()
        return True
    except Exception as e:
        if conn: conn.rollback()
        print(f"Error: {e}")
    finally:
        if conn: conn.close()


def update_book_repo(title, author, year_published, genre, id):
    conn = None

    try:
        conn = get_connection()

        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT id FROM tblBooks WHERE id = %s
                """,
                (id,)
            )
            if cursor.fetchone() is None:
                return False

            cursor.execute(
                """
                UPDATE tblBooks
                SET
                    title          = %s,
                    author         = %s,
                    year_published = %s,
                    genre          = %s
                WHERE id           = %s
                """,
                (
                    title,
                    author,
                    year_published,
                    genre,
                    id
                )
            )
            conn.commit()
            return True
        
    except Exception as e:
        if conn: conn.rollback()
        print(f"Error: {e}")
    finally:
        if conn: conn.close()


def delete_book_repo(id):
    conn = None

    try:
        conn = get_connection()

        with conn.cursor() as cursor:
            cursor.execute(
                """
                DELETE FROM tblBooks WHERE id = %s
                """,
                (id,)
            )
            conn.commit()
            return True
    except Exception as e:
        if conn: conn.rollback()
        print(f"Error: {e}")
    finally:
        if conn: conn.close()



        