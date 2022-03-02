from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, response, Http404,HttpResponseRedirect

from .models import Question
from .models import Member
from .forms import MemberForm #ajouter à
from django.utils import timezone

#liste
def index(request):
  members = Member.objects.all().order_by('id') #Obtenez de la valeur
  return render(request, 'app/members/index.html', {'members':members}) #Passer une valeur au modèle

#Nouveau et modifier
def edit(request, id=None):

	if id: #Lorsqu'il y a un identifiant (lors de l'édition)
		#Rechercher par identifiant et renvoyer les résultats ou erreur 404
		member = get_object_or_404(Member, pk=id)
	else: #Quand il n'y a pas d'identifiant (quand neuf)
		#Créer un membre
		member = Member()

	#Au POST (lorsque le bouton d'enregistrement est enfoncé, que ce soit nouveau ou modifier)
	if request.method == 'POST':
		#Générer un formulaire
		form = MemberForm(request.POST, instance=member)
		if form.is_valid(): #Enregistrer si la validation est OK
			member = form.save(commit=False)
			member.save()
			return redirect('app:index')
	else: #Au moment de GET (générer un formulaire)
		form = MemberForm(instance=member)
	
	#Afficher un nouvel écran / modifier l'écran
	return render(request, 'app/members/edit.html', dict(form=form, id=id))

def delete(request, id):
	# return HttpResponse("Effacer")
	member = get_object_or_404(Member, pk=id)
	member.delete()
	return redirect('app:index')


#Détails
def detail(request, id=id):
  member = get_object_or_404(Member, pk=id)
  return render(request, 'app/members/detail.html', {'member':member})