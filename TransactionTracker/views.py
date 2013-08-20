# Create your views here.
from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
import datetime

from TransactionTracker.forms import EntryForm
from TransactionTracker.models import transaction, transaction_type


def debt(request):
    return render(request, 'debt.html')


def transactions(request):
    return render(request, 'transactions.html')


def home(request):

    return render(request, 'index.html')

    # transactions = transaction.objects.all()
    #
    # users = {1: {'paid': 0, 'owed': 0},
    #          2: {'paid': 0, 'owed': 0}}
    #
    # for trans in transactions:
    #     if not trans.user.username in users:
    #         users[trans.user.username] = {'paid': 0, 'owed': 0}
    #
    #     users[trans.user.username]['paid'] += trans.amount
    #     users[trans.user.username]['owed'] += trans.amount * trans.transaction_type.multiplier
    #
    # u2sum = users['Tom']['owed']
    # u1sum = users['Sean']['owed']
    #
    # users['diff'] = u1sum - u2sum
    #
    # money = users
    #
    # return render(request, 'home.html', {"money": money})


def view(request):
    all_trans = transaction.objects.order_by('-date').all()

    return render(request, 'view.html', {'transactions': all_trans})


def add(request):
    return render(request, 'add.html')

    # #adding new transaction
    # if request.method == "POST":
    #     transaction_form = EntryForm(request.POST)
    #     if transaction_form.is_valid():
    #         user = User.objects.get(pk=transaction_form.data['user'])
    #         trans_type = transaction_type.objects.get(pk=transaction_form.data['type'])
    #
    #         trans = transaction(user=user,
    #                             amount=transaction_form.data['amount'],
    #                             description=transaction_form.data['description'],
    #                             transaction_type=trans_type)
    #
    #         trans.date = datetime.date.today()
    #         trans.save()
    #
    # transaction_form = EntryForm()
    #
    # return render(request, 'add.html', {'t_form': transaction_form})