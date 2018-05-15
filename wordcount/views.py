from django.http import HttpResponse
from django.shortcuts import render


def home(request):
	return render(request,'home.html')


def count(request):
	fulltext=request.GET['fulltext']
	count= len(fulltext.split())
	word_list=fulltext.split()

	counts={}
	for word in word_list:
		if word not in counts:
			counts[word]=1
		else:
			counts[word]+=1
	my_list=list(counts.items())
	my_list.sort(key=lambda x: x[1], reverse=True)



	return render(request,'count.html', {'fulltext': fulltext,'count': count, 'counts': my_list})


def about(request):
	return render(request, 'about.html')