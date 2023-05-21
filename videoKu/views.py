from django.shortcuts import render

# Create your views here.

# key omdb (video) :  cb8d2a18

# Send all data requests to:
# http://www.omdbapi.com/?apikey=[yourkey]&

# Poster API requests:
# http://img.omdbapi.com/?apikey=[yourkey]&

# See symbol explanation on the official website

# r = requests.get('http://api.example.com/books?author=edwards&year=2009')
# =========================================================================
#  url = 'http://api.example.com/books' 
#  params = {'year': year, 'author': author}
#  r = requests.get(url, params=params)


import requests
def search(s):
        # pull data form third party rest api
    #response = requests.get('https://jsonplaceholder.typicode.com/users')
        # convert response data into json
    #users = response.json()
    #print(users)
    url = 'http://www.omdbapi.com'
    header = {
        'apikey':'cb8d2a18',
        's':s,
    }
    response = requests.get(url,header)
    result = response.json()
    #print(result['Search'][2]['Title'])
    #print(results)
    try:
        results = result['Search']
        return results
    except KeyError:
        results = False
        return results
        
    


def index(request):
    if request.method=='POST':
        s = request.POST.get('name')
        result = search(s)
        print(result)
        return render(request, 'videoKu/index.html', {'result':result})
            
    
    return render(request, 'videoKu/index.html', {})
