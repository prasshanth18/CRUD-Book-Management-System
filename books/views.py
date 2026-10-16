
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book


def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')

        Book.objects.create(
            title=title,
            author=author,
            price=price
        )
        return redirect('book_list')

    return render(request, 'books/add_book.html')


def update_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        book.price = request.POST.get('price')
        book.save()
        return redirect('book_list')

    return render(request, 'books/update_book.html', {'book': book})


def delete_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        book.delete()
        return redirect('book_list')

    return render(request, 'books/delete_book.html', {'book': book})


# Create your views here.
