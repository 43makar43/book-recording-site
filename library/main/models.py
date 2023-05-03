from django.db import models

#Сущность Книги
class BookModel(models.Model):
    book_author = models.CharField("Автор книги", max_length=100)
    book_name = models.CharField("Название книги", max_length=50)

    def __str__(self):
        return f'{self.book_name}, {self.book_author}'

#Сущность Заказы
class OrderModel(models.Model):
    full_name_client = models.ForeignKey('ClientModel', on_delete=models.CASCADE, null=True)
    date_of_taking = models.DateField("Дата взятия книги")
    return_date = models.DateField("Дата возврата книги")
    full_name_librarian = models.ForeignKey("LibrarinModel", on_delete=models.CASCADE , null=True)
    book_models = models.ManyToManyField(BookModel)

    def __str__(self):
        return f'{self.book_models}, {self.full_name_client}'
    
#Сущность Библиотекарь
class LibrarinModel(models.Model):
    full_name = models.CharField("ФИО", max_length=100)
    phone_number = models.CharField("Номер телефона", max_length=11)
    passport_data = models.CharField("Паспортные данные", max_length=10)

    def __str__(self):
        return f'{self.full_name}, {self.phone_number}'
    
#Сущность Клиент
class ClientModel(models.Model):
    full_name = models.CharField("ФИО", max_length=100)
    phone_number = models.CharField("Номер телефона", max_length=11)

    def __str__(self):
        return f'{self.full_name}, {self.phone_number}'