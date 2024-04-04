from django.shortcuts import render
from blog.models import User, Publisher
import datetime

def welcome(request):
    if request.method == 'POST':
        blogdata = Publisher.objects.all()
        return render(request, 'welcome.html', {'blogdata':blogdata})
    else:
        blogdata = Publisher.objects.all()
        return render(request, 'welcome.html', {'blogdata': blogdata})


def about(request):
    return render(request, 'about.html')
def snapchat(request):
    return render(request, 'snap.html')

def instagram(request):
    return render(request, 'insta.html')

def registration(request):
    if request.method == 'GET':
     return render(request, 'registration.html')

    else:
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        mail = request.POST['email']
        contact = request.POST['phone']
        user_name = request.POST['user']
        Pwd = request.POST['pwd']
        if User.objects.filter(Username=user_name).exists():
            mes = 'Username is already in use. Please try using another Username'
            return render(request, 'display2.html', {'msg': mes})

        elif User.objects.filter(Email=mail).exists():
                mes = 'Mail ID is already in use. Please try using another Email'
                return render(request, 'display2.html', {'msg': mes})

        elif User.objects.filter(Phone=contact).exists():
                mes = 'Phone Number is already in use. Please try using another mobile number'
                return render(request, 'display2.html', {'msg': mes})

        else:
                User.objects.create(Firstname=first_name, Lastname=last_name, Email=mail, Phone=contact, Username=user_name, Password=Pwd)
                message = 'THANK YOU FOR REGISTERING. NOW YOU CAN LOGIN'
                return render(request, 'display.html', {'msg': message})


def login(request):
    if request.method == "POST":
        user_name = request.POST['user']
        password = request.POST['pwd']
        if(User.objects.filter(Username=user_name, Password=password)):
            return render(request, 'blog.html', {'user':user_name})
        else:
            message = 'YOUR LOGIN DETAILS ARE INVALID, PLEASE TRY AGAIN'
            return render(request, 'display.html', {'msg': message})

    else:
        return render(request, 'login.html')

def blog(request):
    return render(request, 'blog.html')

def Create_blog(request):
    if request.method == 'GET':
        dt = datetime.datetime.now()
        date = datetime.date.today()
        return render(request, 'createblog.html', {'date': date, 'dt': dt})

    else:
        author_name = request.POST['author']
        title_name = request.POST['title']
        content = request.POST['area']
        date = request.POST['date']
        time = request.POST['time']
        blog_name = request.POST['blogname']
        Message = ' Blog name already exists or taken by some other author. Please choose another name. '
        if Publisher.objects.filter(Blog_name=blog_name).exists():
                return render(request, 'display2.html', {'msg': Message})
        else:
                Publisher.objects.create(Authorname=author_name, Titlename=title_name, Content=content, Published_date=date, Published_time=time, Blog_name=blog_name)
                blogdata = Publisher.objects.filter(Authorname=author_name)
                return render(request, 'blogdata.html', {'blogdata': blogdata})

def blog_details(request):
    if request.method == 'GET':
        data = Publisher.objects.all()
        return render(request, 'blogdetails.html', {'data': data})
    else:
        name = request.POST['blog']
        if (Publisher.objects.filter(Blog_name=name)):
            details = Publisher.objects.filter(Blog_name=name)
            return render(request, 'blogdetails.html', {"data": details})

        else:
            message = "Invalid Blog Name"
            return render(request, 'display1.html', {"msg": message})

def EditBlog(request):
    if request.method == 'GET':
        return render(request, 'editblog.html')
    else:
        if 'submit' in request.POST:
            name = request.POST['given_name']
            if (Publisher.objects.filter(Blog_name=name)):
                details = Publisher.objects.filter(Blog_name=name)
                return render(request, 'changeblog.html', {'data': details})
            else:
                message = "Invalid Blog Name"
                return render(request, 'display1.html', {"msg": message})
        else:
            a_name = request.POST['author_name']
            u_name = request.POST['user_name']
            if (Publisher.objects.filter(Authorname=a_name) and User.objects.filter(Username=u_name)):
                details = Publisher.objects.filter(Authorname=a_name)
                return render(request, 'blognames.html', {'data': details})
            else:
                message = "Invalid Author Name or User Name"
                return render(request, 'display1.html', {"msg": message})
def Changeblog(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        if 'edit' in request.POST:
            author_name = request.POST['author']
            title_name = request.POST['title']
            content = request.POST['area']
            Date = datetime.date.today()
            Time = datetime.datetime.now()
            blog_name = request.POST['blogname']
            data = Publisher.objects.filter(Blog_name=blog_name)
            for dt in data:
                dt.Authorname = author_name
                dt.Titlename = title_name
                dt.Content = content
                dt.Published_date = Date
                dt.Published_time = Time
                dt.Blog_name = blog_name
                dt.save()
                all_data = Publisher.objects.filter(Blog_name=blog_name)
                return render(request, 'updatedblog.html', {"all_data": all_data})
        else:
            blog_name = request.POST['blogname']
            data = Publisher.objects.filter(Blog_name=blog_name)
            for d in data:
                d.delete()
                Message = "Your Blog is Deleted Successfully"
                return render(request, 'delete.html', {"msg": Message})


def blogupdated(request):
    if request.method == 'GET':
        return render(request, 'login.html')

def blogdelete(request):
    return render(request, 'login.html')



