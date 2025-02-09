# I got the data in dictionary from chatgpt

library_catalog = {
    "978-0143126560": {"title": "Sapiens: A Brief History of Humankind", "author": "Yuval Noah Harari", "year": 2015},
    "978-0062316097": {"title": "The Alchemist", "author": "Paulo Coelho", "year": 1993},
    "978-0451524935": {"title": "1984", "author": "George Orwell", "year": 1949},
    "978-0743273565": {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    "978-0307474278": {"title": "The Road", "author": "Cormac McCarthy", "year": 2006}
}

# Example:
isbn = "978-0062316097"
print(f"Title: {library_catalog[isbn]['title']}")
print(f"Author: {library_catalog[isbn]['author']}")
print(f"Year: {library_catalog[isbn]['year']}")
