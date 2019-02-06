from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import ListView, DetailView

class KidListView(ListView):
    queryset = Kid.available.all()
    context_object_name = 'kids'
    paginate_by = 5
    template_name = 'kids/kid/list.html'

class MyKidsListView(ListView):

    def get_queryset(self):
        queryset = super(MyKidsListView, self).get_queryset()
        queryset = queryset.filter(sponsor = self.request.user)
        return queryset
    
    context_object_name = 'kids'
    paginate_by = 5
    template_name = 'kids/kid/list.html'
    model = Kid


class KidDetailView(DetailView):
    model = Kid
    template_name = 'kids/kid/detail.html'

def sponsor(request, kid_id):

    kid = get_object_or_404(Kid, pk=kid_id)
    kid.sponsor = request.user
    kid.save()
    Sponsorship.objects.create(kid=kid, sponsor= kid.sponsor)

    return render(request,
                  'kids/kid/sponsored.html',
                  {'kid': kid,})   

def unsponsor(request, kid_id):
    message = ''

    kid = get_object_or_404(Kid, pk=kid_id)
    if(kid.sponsor == request.user):
        kid.sponsor = None
        kid.save()
        s = Sponsorship.objects.filter(kid=kid, sponsor= request.user, action = Sponsorship.SP_CHOICES[0][0])\
            .order_by('-created')\
            .first()

        Sponsorship.objects.filter(id = s.id)\
            .update(action=Sponsorship.SP_CHOICES[1][0])
        #s.update()
        message = "The kid has been unsponsored"
    else :
        message = 'You do not have the right to do this'

    return render(request,
                  'kids/kid/sponsored.html',
                  {'kid': kid, 'message': message})   

def kid_detail(request, pk):
    kid = get_object_or_404(Kid, pk=pk)

    return render(request,
                  'kids/kid/sponsored.html',
                  {'kid': kid,})
