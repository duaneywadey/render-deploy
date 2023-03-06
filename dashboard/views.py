from django.shortcuts import render
from .models import CountryData
from .forms import CountryDataForm, SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def index(request):
	countryInfo = CountryData.objects.all()

	if request.method == 'POST':
		form = CountryDataForm(request.POST)
		if form.is_valid():
			# Every post made must have the name of an author, 
			# commit=False because we don't save it yet 
			instance = form.save(commit=False) 
			instance.author = request.user


			# Save our form
			instance.save()
	else:
		form = CountryDataForm()


	context = {
		'countryInfo':countryInfo,
		'form':form,
	}
	return render(request, 'dashboard/index.html', context)

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			print(form)
			return redirect('dashboard/index.html')

	else:
		form = SignUpForm()


	context = {
		'form':form,
	}

	return render(request, 'dashboard/sign_up.html', context)

def logout_view(request):
	logout(request)
	return render(request, 'dashboard/logout.html')

def history(request):
	countryInfo = CountryData.objects.all()
	context = {
		'countryInfo':countryInfo
	}
	return render(request, 'dashboard/history.html', context)