from backend.repositories.borrower_repository import (
    get_borrowers_repo,
    get_by_id_repo,
    add_borrower_repo,
    update_borrower_repo,
    delete_borrower_repo
)

def get_borrowers_service():
    borrowers = get_borrowers_repo()

    if not borrowers:
        return None

    return borrowers

def get_by_id_service(id):
    borrower = get_by_id_repo

    if not borrower:
        return None

    return borrower


def add_borrower_service():
    result = add_borrower_repo

    if not result:
        return None

    return result

def update_borrower_service():
    result = update_borrower_repo()

    if not result:
        return None

    return result

def delete_borrower_service():
    result = delete_borrower_repo()

    if not result:
        return None

    return result