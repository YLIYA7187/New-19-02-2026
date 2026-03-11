from book import Book

library=[
    Book ("Мастер и Маргарита", "Михаил Булгаков"),
    Book("1984", "Джордж Оруэлл"),
    Book("Преступление и наказание", "Фёдор Достоевский")
]
# Цикл для вывода всех книг в формате "<Название книги> - <Автор>"
for book in library:
    print(f"{book.title} - {book.author}")
