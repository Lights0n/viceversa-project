from django.shortcuts import render


def home(request):
	return render(request, 'home.html')


def reverse(request):
	user_text = request.GET['usertext']
	words = user_text.split()
	words2 = 'ура, сучары'
	#print(words2)
	number_of_words = len(words)
	reversed_text = user_text[::-1]
	# ключ из reverse.html. Значения - переменные из функции
	return render(request, 'reverse.html', {'usertext':user_text, 
		'reversedtext':reversed_text, 'number_of_words':number_of_words, 'words22': words2}, )