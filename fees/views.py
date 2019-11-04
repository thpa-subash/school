from django.http import HttpResponse


def classfees(request):
    if request.is_ajax():
        classame =request.POST['classname']
        context={'classame':classame}
        print(classame)
        return HttpResponse('true')



