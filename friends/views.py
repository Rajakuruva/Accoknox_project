from django.shortcuts import render,redirect
# Create your views here.
from friends.forms import *
from django.http import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def Signup(request):
    user_form = UserForm()
    profle_form = ProfileForm()
    d = {'user_form': user_form,'profle_form': profle_form}
    if request.method == 'POST' and request.FILES:
        UOO = UserForm(request.POST)
        POO = ProfileForm(request.POST,request.FILES)
        if UOO.is_valid() and POO.is_valid():
            NUO = UOO.save(commit=False)
            password = UOO.cleaned_data['password']
            NUO.set_password(password)
            NUO.save()
            NPO = POO.save(commit=False)
            NPO.user_name = NUO
            NPO.save()
            return redirect('user_login')
        else:
            return render(request, 'signup.html', {'user_form': UOO})
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'signup.html',d)


def user_login(request):
    error_message = None
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            UO = User.objects.get(email=email)
            if UO:
                username = UO.username
                AUO = authenticate(username=username, password=password)
                if AUO and AUO.is_active:
                    login(request, AUO)
                    request.session['username'] = username
                    return redirect('Display_profile')
                else:
                    error_message = 'Invalid username or password'
            else:
                error_message = 'Invalid username or password'
        except User.DoesNotExist:
            error_message = 'Invalid username or password'
    return render(request, 'user_login.html', {'error_message': error_message})


@login_required
def Display_profile(request):
    username = request.session.get('username')
    UO = User.objects.get(username = username)
    PO = Profile_class.objects.get(user_name = UO)

    d = {'UO':UO, 'PO':PO}
    return render(request,'Display_profile.html',d)


@login_required
def Show_users(request):
    current_username = request.session.get('username')
    UO = User.objects.exclude(username=current_username)
    PO = Profile_class.objects.all()
    FO = Frined_request_class.objects.filter(User=current_username)
    sender_data = [friends.Request_user for friends in FO if friends.Pending == 'yes' and friends.Accept == 'yes']
    UO_data = UO[1:]
    PO_filtered = PO.filter(user_name__in=UO_data)
    
    d = {'UO': UO_data, 'PO': PO_filtered, 'username': current_username, 'Friends_data': sender_data}
    return render(request, 'show_users.html', d)


@login_required
def Friend_Request(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        username = request.POST.get('username')
        user = User.objects.get(id=user_id)
        friend_request = Frined_request_class(
            User=request.user.username,
            Request_user=user.username,
            Pending="yes",
            Accept="no",
            Decline="no"
        )
        friend_request.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'}, status=400)


@login_required
def Messages(request):
    current_username = request.session.get('username')
    FO = Frined_request_class.objects.filter(Request_user = current_username, Pending="yes", Accept="no")
    PO = Profile_class.objects.all()
    UO = User.objects.all()
    user_dict = {user.username: user for user in UO}
    
    d = {'FO': FO, 'PO': PO, 'user_dict': user_dict, 'username': current_username}
    return render(request, 'Messages.html', d)


@login_required
def handle_accept(request, friend_request_id):
    try:
        friend_request = Frined_request_class.objects.get(id=friend_request_id)
        friend_request.Pending = 'yes'
        friend_request.Accept = 'yes'
        friend_request.save()
        return redirect('Messages')
    except Frined_request_class.DoesNotExist:
        pass


@login_required
def handle_reject(request, friend_request_id):
    try:
        friend_request = Frined_request_class.objects.get(id=friend_request_id)
        friend_request.delete()
        return redirect('Messages')
    except Frined_request_class.DoesNotExist:
        pass


@login_required
def Frineds_list(request):
    current_username = request.session.get('username')
    FO = Frined_request_class.objects.filter(User=current_username, Pending='yes', Accept='yes')
    sender_data = [friends.Request_user for friends in FO if friends.Pending == 'yes' and friends.Accept == 'yes']
    PO = Profile_class.objects.all()
    UO = User.objects.filter(username__in=sender_data)
    
    d = {'FO': sender_data, 'PO': PO, 'user_dict': UO, 'username': current_username}
    return render(request, 'Frineds_list.html', d)
