from django.shortcuts import render
from .models import Employee
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.
class EmployeeList(ListView):
    model = Employee
    queryset = Employee.objects.all()
    template_name = 'employee/employee-list.html'

    def get_queryset(self):
        result = super(EmployeeList, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(first_name__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(email_address__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(city__icontains=q) for q in query_list))
            )

        return result

class EmployeeDetailView(DetailView):
    template_name = "employee/employee_detail.html"
    member = Employee.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Employee, id=id_)


class EmployeeCreateView(CreateView):
    model = Employee
    fields = ['first_name', 'last_name','address','city','birth_date',
    'state','zip','phone_number','email_address','title','start_date','salary',
    'department','work_location','supervisor','emergency_contact_name','emergency_contact_number',
    ]

class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = ['first_name', 'last_name','address','city',
    'state','zip','phone_number','email_address','title',
    'department','work_location','supervisor','emergency_contact_name','emergency_contact_number',
    ]

    def get_absolute_url(self):
        return reverse('employee:Employee_detail', args=[str(self.id)])

class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = '/portal/'
