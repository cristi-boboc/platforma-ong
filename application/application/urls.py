from django.contrib import admin
from django.urls import path, include
from allauth.account.views import LoginView
from axes.decorators import axes_dispatch
from axes.decorators import axes_form_invalid
from django.utils.decorators import method_decorator

from account.forms import AllauthCompatLoginForm

LoginView.dispatch = method_decorator(axes_dispatch)(LoginView.dispatch)
LoginView.form_invalid = method_decorator(axes_form_invalid)(LoginView.form_invalid)

urlpatterns = [
    path('accounts/login/', LoginView.as_view(form_class=AllauthCompatLoginForm), name="account_login"),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
]
