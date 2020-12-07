from django.shortcuts import render,redirect, get_object_or_404
from .models import Courses
from .forms import CoursesForm
from .models import SameTimeCourses
from .forms import SameTimeCoursesForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import pandas as pd
import numpy as np
import pickle
from assistants.models import Assistants
from assistants.forms import AssistantsForm
from classrooms.models import Classrooms
from classrooms.forms import ClassroomsForm
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        course_informations = Courses.objects.filter(authorized=request.user)[:5]

        classroom_informations = Classrooms.objects.filter(authorized=request.user)[:5]

        same_time_informations = SameTimeCourses.objects.filter(authorized=request.user)[:5]

        assistant_informations = Assistants.objects.filter(authorized=request.user)[:5]

        context = {
            "info": course_informations,
            "class_info": classroom_informations,
            "same_time_info": same_time_informations,
            "assistant_info": assistant_informations,

        }

        return render(request, "main_dashboard.html", context=context)
    return render(request, "index.html")

@login_required(login_url="user:loginUser")
def main_dashboard(request):
    course_informations = Courses.objects.filter(authorized = request.user)[:5]

    classroom_informations = Classrooms.objects.filter(authorized=request.user)[:5]

    same_time_informations = SameTimeCourses.objects.filter(authorized=request.user)[:5]

    assistant_informations = Assistants.objects.filter(authorized=request.user)[:5]

    context = {
        "info": course_informations,
        "class_info": classroom_informations,
        "same_time_info": same_time_informations,
        "assistant_info": assistant_informations,

    }

    return render(request, "main_dashboard.html", context=context)


#buraya bir about sayfası koyarız, hem websitesinin hem de inputların açıklamasını yazarız.
#buraya da bir decorator koymalıyız, kullanıcı giriş yapmadıysa bu url hata versin ---authorized = request.user.
@login_required(login_url="user:loginUser")
def dashboard_courses(request):
    informations = Courses.objects.filter(authorized = request.user) 
    context = {
        "info":informations
    }
    
    return render(request, "dashboard_courses.html", context)




@login_required(login_url="user:loginUser")
def add_course(request):
    form = CoursesForm(request.POST or None)
    if form.is_valid():
        info = form.save(commit=False)
        info.authorized = request.user
        info.save()
        messages.info(request,"New Course Added Successfully")

        return redirect("courses:dashboard_courses")
    return render(request,"add_course.html",{"form":form})


@login_required(login_url="user:loginUser")
def detail_course(request,id):
    course=Courses.objects.filter(id=id).first()
    return render(request,"detail_course.html",{"course":course})




@login_required(login_url="user:loginUser")
def add_sametime_course(request):
    form = SameTimeCoursesForm(request.POST or None)
    if form.is_valid():
        info = form.save(commit=False)
        info.authorized = request.user
        info.save()
        messages.info(request,"New Information Added Successfully")

        return redirect("courses:dashboard_sametime_courses")
    return render(request,"add_sametime_course.html",{"form":form})


@login_required(login_url="user:loginUser")
def dashboard_sametime_courses(request):
    informations = SameTimeCourses.objects.filter(authorized = request.user) 
    context = {
        "info":informations
    }
    
    return render(request, "dashboard_sametime_courses.html", context)



@login_required(login_url="user:loginUser")
def update_course(request,id):
    course= get_object_or_404(Courses, id=id)
    form= CoursesForm(request.POST or None,instance=course)
    if form.is_valid():
        info=form.save(commit=False)
        info.authorized = request.user
        info.save()
        messages.success(request,"Course Information Has Been Updated Successfully")
        
        return redirect("courses:dashboard_courses")

    return render(request,"update_course.html",{"form":form})


@login_required(login_url="user:loginUser")
def delete_course(request,id):
    course= get_object_or_404(Courses, id=id)
    course.delete()
    messages.success(request,"Course Successfully Deleted")
    return redirect("courses:dashboard_courses")


@login_required(login_url="user:loginUser")
def delete_sametime_course(request,id):
    sametime_course= get_object_or_404(SameTimeCourses, id=id)
    sametime_course.delete()
    messages.success(request,"Courses Successfully Deleted")
    return redirect("courses:dashboard_sametime_courses")

@login_required(login_url="user:loginUser")
def initial_load(request):
    if request.POST.get('check'):
        file = request.FILES['excel_file']
        user_info = request.user.id
        course_table = pd.read_excel(file, sheet_name='course_table')
        for _, row in course_table.iterrows():
            course_code = 'IU' + str(row['course_code'])
            course_name = row['course_name']
            course_capacity = row['course_capacity']
            sixty_more = row['sixty_more']
            slot_number = row['slot_number']
            lab_or_not = row['lab_or_not']
            department = row['department']
            desired_day = row['desired_day']
            desired_slot = row['desired_slot']

            if np.isnan(desired_day) and np.isnan(desired_slot):
                course = Courses(course_code=course_code, course_name=course_name, course_capacity=course_capacity,
                              sixty_more=sixty_more,  slot_number=slot_number,
                              lab_or_not=lab_or_not,  department=department,
                               authorized_id=user_info)

            elif np.isnan(desired_day):
                course = Courses(course_code=course_code, course_name=course_name, course_capacity=course_capacity,
                              sixty_more=sixty_more,  slot_number=slot_number,
                              lab_or_not=lab_or_not,  department=department,
                               desired_slot=desired_slot, authorized_id=user_info)
            elif np.isnan(desired_slot):
                course = Courses(course_code=course_code, course_name=course_name, course_capacity=course_capacity,
                              sixty_more=sixty_more,  slot_number=slot_number,
                              lab_or_not=lab_or_not,  department=department,
                               desired_day=desired_day, authorized_id=user_info)
            else:
                course = Courses(course_code=course_code, course_name=course_name, course_capacity=course_capacity,
                              sixty_more=sixty_more,  slot_number=slot_number,
                              lab_or_not=lab_or_not,  department=department,
                               desired_day=desired_day, desired_slot=desired_slot,
                              authorized_id=user_info)



            

            course.save()
        assistant_table = pd.read_excel(file, sheet_name='assistant_table')
        for _, row in assistant_table.iterrows():
            assistant_code = 'INS' + str(row['assistant_code'])
            assistant_name = row['assistant_name']
            seniority = row['seniority']
            total_assignment = row['total_assignment']
            if not pd.isnull(row['undesired_days']):
                undesired_days = row['undesired_days'] 
            else:
                undesired_days = row['undesired_days']
            if not pd.isnull(row['undesired_slots']):
                undesired_slots = row['undesired_slots']
            else:
                undesired_slots = row['undesired_slots']


            if pd.isnull(undesired_days) and pd.isnull(undesired_slots):
                assistant = Assistants(assistant_code=assistant_code, assistant_name=assistant_name, seniority=seniority,
                            total_assignment=total_assignment,
                            authorized_id=user_info)
        
            elif pd.isnull(undesired_days):
                assistant = Assistants(assistant_code=assistant_code, assistant_name=assistant_name, seniority=seniority,
                                    total_assignment=total_assignment, undesired_slots = undesired_slots ,
                                    authorized_id=user_info)
            elif pd.isnull(undesired_slots):
                assistant = Assistants(assistant_code=assistant_code, assistant_name=assistant_name, seniority=seniority,
                                    total_assignment=total_assignment, undesired_days = undesired_days ,
                                    authorized_id=user_info)
            else:
                assistant = Assistants(assistant_code=assistant_code, assistant_name=assistant_name, seniority=seniority,
                                    total_assignment=total_assignment, undesired_days = undesired_days , undesired_slots = undesired_slots,
                                    authorized_id=user_info)
            assistant.save()
        classroom_table = pd.read_excel(file, sheet_name='classroom_table')
        for _, row in classroom_table.iterrows():
            classroom_code = 'C' + str(row['classroom_code'])
            classroom_name = row['classroom_name']
            classroom_capacity = row['classroom_capacity']
            lab_or_not = row['lab_or_not']
            classroom = Classrooms(classroom_code=classroom_code, classroom_name=classroom_name, classroom_capacity=classroom_capacity,
                                lab_or_not=lab_or_not, authorized_id=user_info)
            classroom.save()


        same_time_course_table = pd.read_excel(file, sheet_name='same_time_course_table')
        for _, row in same_time_course_table.iterrows():
            course1_code = 'IU' + str(row['course1_code'])
            course2_code = 'IU' + str(row['course2_code'])
            cost = row['cost']
            course_1_code = Courses.objects.get(course_code = course1_code,authorized_id=user_info)
            course_2_code = Courses.objects.get(course_code = course2_code,authorized_id=user_info)
            same_time_course = SameTimeCourses(course1_code = course_1_code, course2_code = course_2_code , cost = cost, authorized_id = user_info)
            same_time_course.save()
        return redirect("index")


    return render(request, 'initial_load.html')





def exam_schedule(request):

    a_file = open("output_exam.pkl", "rb")
    output = pickle.load(a_file)

    list_1 = []
    for course_id, output2 in output.items():
        for classroom_id, output3 in output2.items():
            for day_id, output4 in output3.items():
                for time_id, _ in output4.items():
                    if output[course_id][classroom_id][day_id][time_id][0] > 0:
                        list_1.append([course_id, classroom_id, day_id, time_id,
                                       output[course_id][classroom_id][day_id][time_id][1]])

    df = pd.DataFrame(list_1, columns=['Ders', 'Sınıf', 'Gün', 'Zaman', 'Population'])

    df['Sınıf-Population'] = df['Sınıf'] + '(' + df['Population'].astype(int).astype(str) + ' Student)'

    df = df.groupby(['Gün', 'Zaman', 'Ders'])['Sınıf-Population'].apply(list).reset_index()

    df['Sınıf-Population'] = df['Sınıf-Population'].str.join('-')

    df['Ders-Sınıf-Population'] = [[i, j] for i, j in zip(df['Ders'].values, df['Sınıf-Population'].values)]

    df['Ders-Sınıf-Population'] = df['Ders-Sınıf-Population'].str.join(', ')

    day_list = []
    for i in list(range(1, 9)):
        for j in list(range(1, 8)):
            day_list.append((i, j))

    day_list_df = pd.DataFrame(day_list, columns=['Gün', 'Zaman'])

    df = pd.merge(day_list_df, df, on=['Gün', 'Zaman'], how='left').fillna('-')

    main_output = df.groupby(['Gün', 'Zaman'])['Ders-Sınıf-Population'].apply(list).reset_index().values

    context = {
        'days': [1, 2, 3, 4, 5, 6, 7, 8],
        'slots': [1, 2, 3, 4, 5, 6, 7],
        'model_sonuc': main_output
    }

    return render(request, 'exam_schedule_results.html', context=context)




def assistant_schedule(request):

    a_file = open("output_asistants.pkl", "rb")
    output = pickle.load(a_file)

    list_1 = []
    for course_id, output2 in output.items():
        for classroom_id, output3 in output2.items():
            for day_id, output4 in output3.items():
                for time_id, _ in output4.items():
                    if output[course_id][classroom_id][day_id][time_id] > 0:
                        list_1.append([course_id, classroom_id, day_id, time_id])


    df = pd.DataFrame(list_1, columns=['Asistan', 'Sınıf', 'Gün', 'Zaman'])

    df = df.groupby(['Gün', 'Zaman', 'Sınıf'])['Asistan'].apply(', '.join).reset_index()

    df['Sınıf-Asistan'] = [[i, j] for i, j in zip(df['Sınıf'].values, df['Asistan'].values)]

    df['Sınıf-Asistan'] = df['Sınıf-Asistan'].str.join(' - ')

    df = df.groupby(['Gün', 'Zaman'])['Sınıf-Asistan'].apply(list).reset_index()

    day_list = []
    for i in list(range(1, 9)):
        for j in list(range(1, 8)):
            day_list.append((i, j))

    day_list_df = pd.DataFrame(day_list, columns=['Gün', 'Zaman'])

    df = pd.merge(day_list_df, df, on=['Gün', 'Zaman'], how='left').fillna('-')

    main_output = df.values

    context = {
        'days': [1, 2, 3, 4, 5, 6, 7, 8],
        'slots': [1, 2, 3, 4, 5, 6, 7],
        'model_sonuc': main_output
    }

    return render(request, 'assistant_schedule_results.html', context=context)

