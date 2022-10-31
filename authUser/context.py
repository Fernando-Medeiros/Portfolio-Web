from .models import UserModel


def user_detail(request):

    details = UserModel.objects.first

    if details == None or details == '':
        return {'userDetail': ''}

    return {'userDetail': details}