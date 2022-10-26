from accounts.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', CustomerView,name="customers"),
    path('accounts', AccountsView,name="accounts"),
    path('withdraw', WithdrawView,name="withdraw"),
    path('admin/', admin.site.urls),
]
