from django import template
register=template.Library()


@register.filter()
def swap(data):
    return data.swapcase()


@register.filter('removing')
def remove(data,arg):
    return data.replace(arg,'')

@register.filter()
def counting(data,arg):
    c=0
    for i in range(len(data)):
        if value[i:i+len(arg):]==arg:
            c+=1
    return c
@register.filter()
def changecase(data):
    L=data.split()
    x=[]
    for i in range(1,len(L)-1):
        a=L[i].lower()
        x.append(a)

    return L[0] + ' ' + ' '.join(x) + ' '+L[-1]