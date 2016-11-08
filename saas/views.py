from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from saas.forms import FirstStepRegistration, ParentRegistration, SchoolRegistration, \
    JudgesRegistration, ChairRegistration, VolunteerRegistration, PTABoardRegistration, TaskRegistration
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from saas.models import Parent, School, Judge, Admin, Volunteer, PTABoard, Task
from django.contrib.sessions.models import Session

from saas.models import NEW, IN_PROGRESS, DONE


def home(request):
    context = {}

    # if request.method == 'POST' and request.POST['post']:
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     user, created = User.objects.get_or_create(username=email, password=password)
    #     if not created:
    #         print "not created"
    #         logout(request)
    #         user.backend = 'django.contrib.auth.backends.ModelBackend'
    #         user.save()
    #         auth = authenticate(username=email, password=password)
    #         login(request, user)
    #         return redirect("/main")
    #     else:
    #         context = {'er1': 'yes'}
    return render(request, "landing.html", context)

def main_logout(request):
    request.session.flush()
    Session.objects.all().delete()
    for key in list(request.session.keys()):
        del request.session[key]
    return redirect('/main_login')

def main_login(request):
    # if request.user.is_authenticated():
    #     return redirect("/main")
    context = {}
    if request.method == 'POST' and request.POST['post']:
        email = request.POST['email']
        password = request.POST['password']
        user, created = User.objects.get_or_create(username=email, password=password)
        if not created:
            print "not created"
            logout(request)
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            user.save()
            auth = authenticate(username=email, password=password)
            login(request, user)
            return redirect("/main")
        else:
            context = {'er1': 'yes'}
    return render(request, "auth/login.html", context)

def register(request):
    context = {}
    if request.method == 'POST' and request.POST['post']:
        form = FirstStepRegistration(request.POST)
        if form.is_valid():
            try:
            # role = request.POST['role']
                password = form.cleaned_data['password']
                email = form.cleaned_data['email']
                user, created = User.objects.get_or_create(username=email, password=password)
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                user.save()
                auth = authenticate(username=user.username, password=user.password)
                if not created:
                    login(request, auth)
                    return redirect("/main")

                login(request, user)
                return redirect("/intermid")
            except:
                context = {'er1': 'yes'}
    return render(request, "auth/register.html", context)

def forgot_password(request):
    context = {}
    return render(request, "auth/forgot_password.html", context)

@login_required
def intermid(request):
    context = {}
    # if request.method == 'POST' and request.POST['post']:
    #     form = FirstStepRegistration(request.POST)
    #     if form.is_valid():
    #         role = request.POST['role']
    #         password = form.cleaned_data['password']
    #         email = form.cleaned_data['email']
    #         user, created = User.objects.get_or_create(username=email, password=password)
    #         user.backend = 'django.contrib.auth.backends.ModelBackend'
    #         user.save()
    #         auth = authenticate(username=user.username, password=user.password)
    #         if not created:
    #             login(request, auth)
    #             return redirect("/main")
    #
    #         login(request, user)
    #         path = "%s_register" % role
    #
    #         return redirect(path)
    return render(request, "itermid_registr_page.html", context)


@login_required
def parent_register(request):
    print "request.userrequest.userrequest.userrequest.userrequest.userrequest.user", request.user
    schools = School.objects.all()
    context = {"schools": schools}
    if request.method == 'POST' and request.POST['post']:
        form = ParentRegistration(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            school = School.objects.get(name=form.cleaned_data['school'])
            mailing_address_1 = form.cleaned_data['address1']
            mailing_address_2 = form.cleaned_data['address2']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            phone = form.cleaned_data['phone']
            parent, created = Parent.objects.get_or_create(user=request.user, defaults = {'first_name': first_name, 'last_name': last_name, 'mailing_address_1': mailing_address_1, 'mailing_address_2': mailing_address_2, 'state': state, 'city': city, 'zipcode': zipcode, 'phone': phone})
            parent.school.add(school)
            parent.save()
            return redirect('/main')
    return render(request, "auth/parent_register.html", context)

@login_required
def judges_register(request):
    context = {}
    if request.method == 'POST' and request.POST['post']:
        form = JudgesRegistration(request.POST)
        if form.is_valid():
            organisation = form.cleaned_data['organisation']
            phone = form.cleaned_data['phone']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            judge, created = Judge.objects.get_or_create(user=request.user,
                                                           defaults={'organisation': organisation,
                                                                     'first_name': first_name,
                                                                     'last_name': last_name,
                                                                     'phone': phone,
                                                                     })
            judge.save()
            return redirect('/main')
    return render(request, "auth/judges_register.html", context)

@login_required
def chair_register(request):
    context = {}
    if request.method == 'POST' and request.POST['post']:
        form = ChairRegistration(request.POST)
        if form.is_valid():
            address_1 = form.cleaned_data['address_1']
            address_2 = form.cleaned_data['address_2']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            phone = form.cleaned_data['phone']
            pta_paid_date = form.cleaned_data['pta_paid_date']
            pta_paid = form.cleaned_data['pta_paid']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            school = School(name=form.cleaned_data['school'], pta_paid=pta_paid, pta_paid_date=pta_paid_date, address_1=address_1, address_2=address_2, city=city, state=state, zipcode=zipcode)
            school.save()
            admin, created = Admin.objects.get_or_create(user=request.user, defaults={'phone': phone,
                                                                                      'first_name': first_name,
                                                                                      'last_name': last_name,
                                                                                      })
            admin.school.add(school)
            admin.save()

            return redirect('/main')
    return render(request, "auth/chair_register.html", context)

@login_required
def main(request):
    context = {}
    print "request.userrequest.userrequest.userrequest.userrequest.userrequest.user", request.user
    try:
        if Parent.objects.get(user=request.user):
            return render(request, "auth/parent.html", context)
    except:
        pass
    try:
        if Judge.objects.get(user=request.user):
            return render(request, "auth/judges.html", context)
    except:
        pass
    try:
        if Admin.objects.get(user=request.user):
            chair = Admin.objects.get(user=request.user)
            context = {
                "first_name": chair.first_name,
                "last_name": chair.last_name,
            }
            return render(request, "auth/chair.html", context)
    except:
        pass
    return redirect("/intermid")

@login_required
def volunteers(request):
    context = {}
    volunteers = None
    last_modification = None
    old_email = None
    counter = 0
    try:
        chair = Admin.objects.get(user=request.user)
        school = School.objects.get(id=chair.school.all()[0].id)
        try:
            volunteers = Volunteer.objects.filter(school=school).order_by('-created')
            last_modification = volunteers.order_by('updated')[0].updated
            counter = volunteers.count()
        except:
            pass
        try:
            old_email = request.POST['old_email']
        except:
            pass
        context = {
            "first_name": chair.first_name,
            "last_name": chair.last_name,
            'volunteers': volunteers,
            'school': school,
            'last_modification': last_modification,
            'counter': counter,
        }
        if request.method == 'POST' and request.POST['volunteer']:
            form = VolunteerRegistration(request.POST)
            if form.is_valid():
                phone = form.cleaned_data['phone']
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                email = form.cleaned_data['email']

                if not old_email:
                    volunteer, created = Volunteer.objects.get_or_create(email=email, defaults={'phone': phone,
                                                                                              'first_name': first_name,
                                                                                              'last_name': last_name,
                                                                                              })
                    volunteer.school.add(school)
                    volunteer.save()

                else:
                    volunteer = Volunteer.objects.get(email=old_email)
                    Volunteer.objects.filter(id=volunteer.id).update(email=email, phone=phone, first_name=first_name, last_name=last_name,)
                return redirect('/volunteers')
    except:
        pass
    return render(request, "volunteers.html", context)


@login_required
def pta_board(request):
    context = {}
    pta_board = None
    last_modification = None
    old_email = None
    counter = 0
    try:
        chair = Admin.objects.get(user=request.user)
        school = School.objects.get(id=chair.school.all()[0].id)
        try:
            pta_board = PTABoard.objects.filter(school=school).order_by('-created')
            last_modification = pta_board.order_by('updated')[0].updated
            counter = pta_board.count()
        except:
            pass
        try:
            old_email = request.POST['old_email']
        except:
            pass
        context = {
            "first_name": chair.first_name,
            "last_name": chair.last_name,
            'volunteers': pta_board,
            'school': school,
            'last_modification': last_modification,
            'counter': counter,
        }
        if request.method == 'POST' and request.POST['pta_board']:
            form = PTABoardRegistration(request.POST)
            if form.is_valid():
                phone = form.cleaned_data['phone']
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                email = form.cleaned_data['email']
                role = form.cleaned_data['last_name']

                if not old_email:
                    volunteer, created = PTABoard.objects.get_or_create(email=email, defaults={
                                                                                              'role':role,
                                                                                              'phone': phone,
                                                                                              'first_name': first_name,
                                                                                              'last_name': last_name,
                                                                                              })
                    volunteer.school.add(school)
                    volunteer.save()

                else:
                    pta_board = PTABoard.objects.get(email=old_email)
                    PTABoard.objects.filter(id=pta_board.id).update(role=role, email=email, phone=phone, first_name=first_name, last_name=last_name,)
                return redirect('/pta_board')
    except:
        pass
    return render(request, "pta_board.html", context)


def school(request):

    chair = Admin.objects.get(user=request.user)
    school = School.objects.get(id=chair.school.all()[0].id)
    last_modification = school.updated
    context = {
        'school': school,
        'last_modification': last_modification,
    }
    try:
        # try:
        #
        # except:
        #     pass
        try:
            old_email = request.POST['old_email']
        except:
            pass
        context = {
            "first_name": chair.first_name,
            "last_name": chair.last_name,
            # 'school_info': school,
            'school': school,
            'last_modification': last_modification,
            # 'counter': counter,
        }
        if request.method == 'POST' and request.POST['school']:
            form = SchoolRegistration(request.POST)
            if form.is_valid():
                address_1 = form.cleaned_data['address_1']
                address_2 = form.cleaned_data['address_2']
                city = form.cleaned_data['city']
                state = form.cleaned_data['state']
                zipcode = form.cleaned_data['zipcode']
                pta_paid_date = form.cleaned_data['pta_paid_date']
                pta_paid = form.cleaned_data['pta_paid']
                name = form.cleaned_data['school']

                School.objects.filter(id=school.id).update(name=name, pta_paid=pta_paid, pta_paid_date=pta_paid_date,
                                                           state=state, city=city, address_1=address_1, address_2=address_2, zipcode=zipcode )
                return redirect('/school')
    except:
        pass
    return render(request, "school.html", context)


def tasks(request):
    context = {}
    tasks = None
    last_modification = ''
    counter = 0
    task_id = None
    asignee_id = None
    try:
        chair = Admin.objects.get(user=request.user)
        school = School.objects.get(id=chair.school.all()[0].id)
        try:
            tasks = Task.objects.filter(school=school).order_by('-created')
            last_modification = tasks.order_by('updated')[0].updated
            counter = tasks.count()
        except:
            pass
        context = {
            "first_name": chair.first_name,
            "last_name": chair.last_name,
            'tasks': tasks,
            'school': school,
            'last_modification': last_modification,
            'counter': counter,
            'asignees': Volunteer.objects.filter(school=school),
        }
        if request.method == 'POST' and request.POST['tasks']:
            form = TaskRegistration(request.POST)
            if form.is_valid():

                task_category = form.cleaned_data['task_category']
                task_description = form.cleaned_data['task_description']
                task_exp_start_date = form.cleaned_data['task_exp_start_date']
                task_exp_end_date = form.cleaned_data['task_exp_end_date']
                task_actual_start_date = form.cleaned_data['task_actual_start_date']
                task_actual_end_date = form.cleaned_data['task_actual_end_date']
                status = form.cleaned_data['status']

                # if status == '1':
                #     status = NEW
                # if status == '2':
                #     status = IN_PROGRESS
                # if status == '3':
                #     status = DONE
                # TASK_STATUS = [NEW, IN_PROGRESS, DONE]
                # status = TASK_STATUS[int(status)]
                comments = form.cleaned_data['comments']
                # asignee = form.cleaned_data['asignee']

                try:#if edit
                    task_id = request.POST['task_id']
                except:
                    pass
                try:
                    asignee_id = request.POST['asignee_id']
                except:
                    pass
                if not task_id:
                    task = Task(task_description=task_description, task_category=task_category, task_exp_start_date=task_exp_start_date,
                                                                task_exp_end_date=task_exp_end_date,
                                                           task_actual_start_date=task_actual_start_date,
                                                           task_actual_end_date=task_actual_end_date,
                                                           status=status,
                                                           comments=comments,
                                                           )
                    task.save()
                    try:
                        task.asignee.add(Volunteer.objects.filter(id=int(asignee_id)))
                    except:
                        pass
                    task.school.add(school)
                    # task.save()
                else:
                    task = Task.objects.filter(id=task_id)
                    try:
                        task.asignee.add(Volunteer.objects.filter(id=int(asignee_id)))
                    except:
                        pass
                    task.update(task_description=task_description, task_category=task_category, task_exp_start_date=task_exp_start_date,
                                                                task_exp_end_date=task_exp_end_date,
                                                           task_actual_start_date=task_actual_start_date,
                                                           task_actual_end_date=task_actual_end_date,
                                                           status=status,
                                                           comments=comments,
                                                           )
                    # task.save()

                return redirect('/tasks')
    except:
        pass
    return render(request, "tasks.html", context)