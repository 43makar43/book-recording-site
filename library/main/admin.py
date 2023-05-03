from django.contrib import admin

from .models import OrderModel, BookModel, ClientModel, LibrarinModel

@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin): 
    list_display = ('full_name_client', 'date_of_taking', 'return_date', 'full_name_librarian',)

@admin.register(LibrarinModel)
class LibrarinAdmin(admin.ModelAdmin): 
    list_display = ('full_name', 'phone_number')

@admin.register(ClientModel)
class ClientAdmin(admin.ModelAdmin): 
    list_display = ('full_name', 'phone_number')

@admin.register(BookModel)
class BookAdmin(admin.ModelAdmin): 
    list_display = ('book_name', 'book_author')