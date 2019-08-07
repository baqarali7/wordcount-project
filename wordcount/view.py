from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    fullTextBox = request.GET["fullTextBox"]
    wordlist = fullTextBox.split()

    worddictionery = {}
    for word in wordlist:
        if word in worddictionery:
            worddictionery[word] += 1
        else:
            worddictionery[word] = 1
        
    sortedwords = sorted(worddictionery.items(), key= operator.itemgetter(1), reverse = True)

    return render(request, 'count.html', {'fullTextBox': fullTextBox, "count": len(wordlist), "sortedwords": sortedwords})
    
def about(request):
    return render(request, 'about.html')