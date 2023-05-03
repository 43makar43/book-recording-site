from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from .models import ClientModel, OrderModel, BookModel, LibrarinModel
from django.views.generic.base import View
from .forms import ClientForm, OrderForm
from django.core import serializers
import json


class Home(View):
    def get(self, request):
        return render(request, "home/home.html")

class Order(View):
    def get(self, request):
        objectsOrder = OrderModel.objects.order_by('-full_name_client')
        return render(request, "order/order.html", {'objectsOrder': objectsOrder})

class Client(View):
    def get(self, request):
        objectsClient = ClientModel.objects.order_by('-full_name')
        return render(request, "client/client.html", {'objectsClient': objectsClient})
    
class createClient(View):
    def get(self, request):
        if request.method =='POST':
            form = ClientForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('client')
            
        form = ClientForm()

        data = {
            'form': form
        }

        return render(request, "addClient/addClient.html", data)
    
    def post(self, request):
        if request.method =='POST':
            form = ClientForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('client')
            
        form = ClientForm()

        data = {
            'form': form
        }

        return render(request, "addClient/addClient.html", data)
    
class createOrder(View):
    def get(self, request):
        if request.method =='POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('order')

        form = OrderForm()

        data = {
            'form': form
        }

        return render(request, "addOrder/addOrder.html", data)
    
    def post(self, request):
        if request.method =='POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('order')

        form = OrderForm()

        data = {
            'form': form
        }

        return render(request, "addOrder/addOrder.html", data)


class GetClient(View):
    def get(self, request):
        data = request.GET

        id = int(data.get('id'))
        client = ClientModel.objects.filter(id=id)

        context = serializers.serialize('json', client)
        return HttpResponse(context, content_type="application/json")

class UpdateClient(View):
    def get(self, request):
        data = request.GET

        id = int(data.get('id'))
        full_name = data.get('fullName')
        phone_number = data.get('number')

        client = ClientModel.objects.get(id=id)
        client.full_name = full_name
        client.phone_number = phone_number
        client.save()

        return HttpResponse("Ok")
    
    # сделать заказ
class GetOrder(View):
    def get(self, request):
        data = request.GET

        id = int(data.get('id'))

        order = OrderModel.objects.filter(id=id)
        client = order[0].full_name_client
        librarin = order[0].full_name_librarian


        array_books = []
        books = order[0].book_models

        for book in books.all():
            info = {
                'id' : id,
                'book_author' : book.book_author,
                'book_name': book.book_name
            }
            array_books.append(info)


        context = [
            {'order' : json.loads(serializers.serialize('json', [order[0]]))},
            {'client' : json.loads(serializers.serialize('json', [client]))},
            {'librarin' : json.loads(serializers.serialize('json', [librarin]))}
        ]

        context.append(array_books)

        return JsonResponse(context, safe=False)

