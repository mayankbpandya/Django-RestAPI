from django.http import HttpResponse, JsonResponse


def home_page(request):
    print("Home Page Requested")
    friends = ['AC','BB','CC']
    #return HttpResponse("This is Home Page")
    return JsonResponse(friends,safe=False)
    