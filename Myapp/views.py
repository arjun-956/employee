from django.shortcuts import render,redirect
from django.views.generic import View

from Myapp.models import Employee,Work
from Myapp.forms import WorkForm

class EmployeeListView(View):
    def get(self,request,*args,**kwargs):

        #fecthing all employee recodes

        qs= Employee.objects.all()



        return render(request,"employee_list.html",{"employee":qs})

#Employee create
#url:lhs:8000/employee/add/
#method:post,get

class EmployeeCreateView(View):
    def get(self,request,*args,**kwargs):

        return render(request,'employee_create.html')
    #print(slary='salaryBox','''''''''''''''')
    #modelname render(request,post.get)
    def post(self,request,*args,**kwargs):
        name_Box_value=request.POST.get("nameBox")
        age_Box_value=request.POST.get("ageBox")
        salary_Box_value=request.POST.get("salaryBox")
        designation_Box_value=request.POST.get("designationBox")
        email_Box_value=request.POST.get("emailBox")
        phone_Box_value=request.POST.get("phoneBox")

       #ORM QUERY  FOR CREATING
       #ModelName.objects,create(field=value)

        Employee.objects.create(name=name_Box_value,age=age_Box_value,salary=salary_Box_value,designation=designation_Box_value,email=email_Box_value,phone=phone_Box_value )
        #django>shortcuts>function redirect(name)
         #return render(request,'employee_create.html')
        return redirect("emp-list")

        #render=>templite serve,context
        #redirect=>redirect to view


        #Employee details
#url:lolhost:8000/employees/{pk}/

class EmployeeDetailView(View):
    def get(self,request,*args,**kwargs): #kwargs recive url parameter as dictionarykwargs={'pk-2'}

        id=kwargs.get("pk")

        #omr query for fetching employee with id

        qs=Employee.objects.get(id=id)

        return render(request,"employee_detail.html",{"employee":qs})

class EmployeeDeleteView(View):

    def get(self,request,*args,**kwargs):
        
        id=kwargs.get('pk')

        qs=Employee.objects.get(id=id).delete()

        return redirect("emp-list")

class EmployeeUpdateView(View):
    def get(self,request,*args,**kwargs):

        id=kwargs.get('pk')

        qs=Employee.objects.get(id=id)

        return render(request,'employee_edit.html',{'employee':qs})


    def post(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Employee.objects.filter(id=id).update(
            name=request.POST.get("name"),
            age=int(request.POST.get("age")),
            salary=int(request.POST.get("salary")),
            designation=request.POST.get("designation"),
            email=request.POST.get("email"),
            phone=int(request.POST.get("phone")),
        )

        return  redirect('emp-list')


#1)work create

#url:localhost:8000/work/add/
#methode:get,post


class WorkCreateView(View):

    def get(self,request,*args,**kwargs):

        form_instance=WorkForm()

        return render(request,"work_add.html",{"form":form_instance})

    def post(self,request,*args,**kwargs):

        form_instance=WorkForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            Work.objects.create(**data)

        return render(request,"work_add.html")


#work list
#url:localhost:8000/works/all

class WorkListView(View):

    def get(self,request,*args,**kwargs):

        qs=Work.objects.all()

        return render(request,"work_list.html" ,{"works":qs})


#url:localhost/8000/change/

class WorkUpdateView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        work_object=Work.objects.get(id=id)

        data={
            "title":work_object.title,
            "description":work_object.description,
            "start_date":work_object.start_date,
            "end_date":work_object.end_date,
            "status":work_object.status
        }

        form_instance=WorkForm(initial=data)

        return render(request,"work_edit.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        id= kwargs.get("pk")

        form_instance=WorkForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            Work.objects.filter(id=id).update(**data)

            return redirect("work-all")
        else:
            return render(request,"work_edit.html",{"form":form_instance})
        

class WorkDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Work.objects.get(id=id).delete()

        return redirect("work-all")