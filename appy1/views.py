from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from .models import User

def create_user(request):
    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        user=User.objects.create(name=name,email=email,age=age)
        return JsonResponse({'status':'User added successfully','user':user.id})
    return render(request,'appy1/add_user.html')



def update_user(request,user_id):
    user=get_object_or_404(User,id=user_id)
    if request.method =="POST":
        user.name=request.POST.get('name')
        user.email=request.POST.get('email')
        user.age=request.POST.get('age')
        user.save()
        return JsonResponse({'status':'User updated successfully'})
    return render(request,'appy1/update_user.html',{'user':user})



def get_users(request):
    users=list(User.objects.values())
    return JsonResponse(users,safe=False)



def get_user_by_id(request,user_id):
    user=get_object_or_404(User,id=user_id)
    return JsonResponse({'id':user.id , 'name':user.name , 'email':user.email , 'age':user.age})




def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return JsonResponse({'status': 'User deleted successfully'})