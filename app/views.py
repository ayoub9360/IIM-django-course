from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, response, Http404,HttpResponseRedirect

from .models import Product
from .forms import UpdateProductForm, AddProductForm #ajouter à
from django.utils import timezone

# liste
def index(request):
    product = Product()

    if request.method == 'POST':
        form = AddProductForm(request.POST, instance=product)
        if form.is_valid(): #Enregistrer si la validation est OK
            product = form.save(commit=False)
            product.save()
            return redirect('app:index')

    products = Product.objects.all().order_by('id') #Obtenez de la valeur
    form = AddProductForm()
    return render(request, 'app/members/index.html', {'products':products, 'form': form}) #Passer une valeur au modèle

#Nouveau et modifier
def edit(request, id=None):

    if id: #Lorsqu'il y a un identifiant (lors de l'édition)
        #Rechercher par identifiant et renvoyer les résultats ou erreur 404
        product = get_object_or_404(Product, pk=id)
    else: #Quand il n'y a pas d'identifiant (quand neuf)
        #Créer un membre
        product = Product()

    #Au POST (lorsque le bouton d'enregistrement est enfoncé, que ce soit nouveau ou modifier)
    if request.method == 'POST':
        #Générer un formulaire
        form = UpdateProductForm(request.POST, instance=product)
        if form.is_valid(): #Enregistrer si la validation est OK
            product = form.save(commit=False)
            product.save()
            return redirect('app:index')
    else: #Au moment de GET (générer un formulaire)
        form = UpdateProductForm(instance=product)

    #Afficher un nouvel écran / modifier l'écran
    return render(request, 'app/members/edit.html', dict(form=form, id=id))

#Détails
def detail(request, id=id):
	product = get_object_or_404(Product, pk=id)

	if request.method == 'POST':
		#Générer un formulaire
		form = UpdateProductForm(request.POST, instance=product)
		if form.is_valid(): #Enregistrer si la validation est OK
			product = form.save(commit=False)
			product.save()
			return redirect('app:index')
	form = UpdateProductForm(instance=product)
	return render(request, 'app/members/detail.html', {'product':product, 'form': form})