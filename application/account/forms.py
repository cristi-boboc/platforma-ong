from allauth.account.forms import LoginForm


class AllauthCompatLoginForm(LoginForm):
    def user_credentials(self):
        credentials = super(AllauthCompatLoginForm, self).user_credentials()
        credentials['login'] = credentials.get('email') or credentials.get('username')
        return credentials
