from .sabad import Sabad


def sabad(request):
    return {'sabad': Sabad(request)}