# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User
import datetime

from TransactionTracker.forms import EntryForm
from TransactionTracker.models import transaction, transaction_type


def home(request):

    transactions = transaction.objects.all()
    sean_trans = transactions.filter(user=User.objects.get(username="Sean"))
    tom_trans = transactions.filter(user=User.objects.get(username="Tom"))

    s_owed = 0
    t_owed = 0
    s_paid = 0
    t_paid = 0

    for trans in sean_trans:
        s_owed += trans.amount * trans.transaction_type.multiplier
        s_paid += trans.amount

    s_tot = s_paid - s_owed

    for trans in tom_trans:
        t_owed += trans.amount * trans.transaction_type.multiplier
        t_paid += trans.amount

    t_tot = t_paid - t_owed

    money = {
        't_tot': t_tot,
        's_tot': s_tot,
        'diff': t_tot - s_tot,
    }


    return render(request, 'home.html', {"money": money})


def view(request):
    all_trans = transaction.objects.order_by('-date').all()

    return render(request, 'view.html', {'transactions': all_trans})


def add(request):

    #adding new transaction
    if request.method == "POST":
        transaction_form = EntryForm(request.POST)
        if transaction_form.is_valid():
            user = User.objects.get(pk=transaction_form.data['user'])
            trans_type = transaction_type.objects.get(pk=transaction_form.data['type'])

            trans = transaction(user=user,
                                amount=transaction_form.data['amount'],
                                description=transaction_form.data['description'],
                                transaction_type=trans_type)

            trans.date = datetime.date.today()
            trans.save()

    transaction_form = EntryForm()

    return render(request, 'add.html', {'t_form': transaction_form})