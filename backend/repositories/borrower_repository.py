from backend.database.connection import get_connection


def get_borrowers_repo():
    conn = None

    try:
        conn = get_connection()

        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT 
                    id,
                    first_name,
                    last_name,
                    contact
                FROM tblBorrowers
                """
            )
            return cursor.fetchall()
    except Exception as e:
        print(f"Error: {e}")
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
                    first_name,
                    last_name,
                    contact
                FROM tblBorrowers
                WHERe id = %s
                """,
                (id,)
            )
            return cursor.fetchone()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn: conn.close()


def add_borrower_repo(first_name, last_name, contact):
    conn = None

    try:
        conn = get_connection()

        with conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO tblBorrowers
                    (first_name, last_name, contact)
                VALUES 
                    (%s, %s, %s)
                """,
                (
                    first_name, 
                    last_name,
                    contact
                )
            )
            conn.commit()
            return True
        
    except Exception as e:
        if conn: conn.rollback()
        print(f"Error: {e}")
    finally:
        if conn: conn.close()

def update_borrower_repo(first_name, last_name, contact, id):
    conn = None

    try:
        conn = get_connection()

        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT id FROM tblBorrowers WHERE id = %s
                """,
                (id,)
            )
            if cursor.fetchone() is None:
                return False

            cursor.execute(
                """
                UPDATE tblBorrowers
                SET
                    first_name = %s,
                    last_name  = %s,
                    contact    = %s
                WHERE id       = %s
                """,
                (
                    first_name,
                    last_name,
                    contact,
                    id
                )
            )
            conn.commit()
            return True
    except Exception as e:
        if conn: conn.commit()
        print(f"Error: {e}")
    finally:
        if conn: conn.close()


def delete_borrower_repo(id):
    conn = None

    try:
        conn = get_connection()

        with conn.cursor() as cursor:
            cursor.execute(
                """
                DELETE FROM tblBorrowers WHERE id = %s
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

        
        
        
