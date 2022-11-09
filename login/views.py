from django.contrib.auth import authenticate, login
from django.shortcuts import render

def user_login(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
    
        
        if user is not None:
            
            login(request, user) 
            return render(request, 'shop/index.html')
        else:
           
            return render(request, 'login/login.html', {'error_message': 'Incorrect username and / or password.'})
    else:
       
        return render(request, 'login/login.html')

    