from .models import Stack


def all_stacks(request):

    stacks = Stack.objects.all().order_by('created_at')
    
    if stacks == None or stacks == '':
        return {'allStacks': ''}

    return {'allStacks': stacks}
