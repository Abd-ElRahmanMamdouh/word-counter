from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    context = {
    	"title":"home",
    	"content":"Welcome to Home Page"
	}
    return render(request, 'home.html',context)


def count(request):
    fulltext = request.POST['fulltext']
    wordlist = fulltext.split()
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            #Increase
            worddictionary[word] +=1
        else:
            #add to the dictionary
            worddictionary[word] = 1
    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    context = {
    	"title":"Count",
    	"content":"Counting!",
        'fulltext':fulltext,
        'count':len(wordlist),
        'sortedwords':sortedwords,
	}
    return render(request, 'count.html',context)

def about(request):
    context = {
    	"title":"about",
    	"content":"About the website"
	}
    return render(request, 'about.html',context)
