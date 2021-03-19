import json
import csv

books = [json.loads(line) for line in open("books.json", "r")]

# filtered_books = {"Python": 0, "Java": 0, "PHP": 0}

# for book in books:
#     if "Python" in book["categories"]:
#         filtered_books["Python"] = (filtered_books["Python"] or 0) + 1

# print(filtered_books)


def category_percentage(category, books):
    total_number_of_books = len(books)
    n_of_books_with_category = len(
        [book for book in books if category in book["categories"]]
    )
    percentage = n_of_books_with_category / total_number_of_books
    return (category, percentage)


percentage_python_books = category_percentage("Python", books)

percentage_java_books = category_percentage("Java", books)

percentage_php_books = category_percentage("PHP", books)

with open("categories_and_percentages.csv", "w") as file:
    writer = csv.writer(file)
    header = ["categoria", "porcentagem"]

    writer.writerow(header)
    writer.writerow(percentage_python_books)
    writer.writerow(percentage_java_books)
    writer.writerow(percentage_php_books)


# Código abaixo dá books dá JSONDecodeError: Extra data

# with open("books.json") as file:
#     books = json.load(file)
#     # print("books")


# Para resolver:
# https://stackoverflow.com/questions/21058935/python-json-loads-shows-valueerror-extra-data/51830719
