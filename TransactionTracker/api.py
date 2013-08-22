from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from models import transaction, transaction_type
from django.contrib.auth.models import User
from tastypie import fields


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        fields = ['username', 'id']
        allowed_methods = ['get']


class TransactionTypeResource(ModelResource):
    class Meta:
        queryset = transaction_type.objects.all()
        resource_name = 'transaction_type'
        fields = ['description', 'id']


class TransactionResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user', full=True)
    transaction_type = fields.ForeignKey(TransactionTypeResource, 'transaction_type', full=True)

    class Meta:
        queryset = transaction.objects.all().order_by('-date')
        resource_name = 'transaction'
        authorization = Authorization()