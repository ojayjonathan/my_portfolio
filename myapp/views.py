from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

class HomeView(View):

    @staticmethod
    def get(request):
        if request.session.test_cookie_worked():
            print("TEST COOKIE WORKED!")
            request.session.delete_test_cookie()
        else:
            print('no cookie')    
        return render(request, 'home.html',{})
        

class AboutView(View):

    @staticmethod
    def get(request):
        return render(request, 'about.html')

class ServicesView(View):

    @staticmethod
    def get(request):
        return render(request, 'services.html')

class ContactsView(View):

    @staticmethod
    def get(request):
        return render(request, 'contacts.html')

    @staticmethod
    def post(request):
        return JsonResponse({'message':'message send'})    

class WorkView(View):

    @staticmethod
    def get(request):
        return render(request, 'work.html')        