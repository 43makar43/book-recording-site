from .models import ClientModel, OrderModel
from django.forms import ModelForm, TextInput, DateInput
    
class ClientForm(ModelForm):
    class Meta:
        model = ClientModel
        fields = ['full_name', 'phone_number']

        widgets = {
            "full_name": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'ФИО'
            }),

            "phone_number": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Номер телефона'
            }),
        }

class OrderForm(ModelForm):
    class Meta:
        model = OrderModel
        fields = ['full_name_client', 'date_of_taking', 'return_date', 'full_name_librarian', 'book_models']

        widgets = {

            "date_of_taking": DateInput(attrs={
            'type': 'date',
            'class': 'form-control',
            'placeholder': 'Дата взятия кинги'
            }),

            "return_date": DateInput(attrs={
            'type': 'date',
            'class': 'form-control',
            'placeholder': 'Дата возврата кинги'
            }),
        }