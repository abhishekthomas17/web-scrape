from django import template


register = template.Library()

@register.filter
def index(List, i):
    return List[int(i)]

@register.filter
def index1(List, i):
    return List[int(i+1)]


@register.filter
def index2(List, i):
    return List[int(i+2)]


@register.filter
def index3(List, i):
    return List[int(i+3)]

@register.filter
def index4(List, i):
    return List[int(i+4)]


@register.filter
def index5(List, i):
    return List[int(i+5)]



@register.filter
def index6(List, i):
    return List[int(i+6)]


@register.filter
def index7(List, i):
    return List[int(i+7)]

@register.filter
def index8(List, i):
    return List[int(i+8)]

@register.filter
def indexm1(List, i):
    return List[int(i-1)]


@register.filter
def indexed(List, i):
    return List[int((i/5)-1)]

@register.filter
def indexed1(List, i):
    a=(i/9)-1
    return List[int(a)]
