from django.contrib import admin

from Student.models import Department, Course, Student

# Register your models here.



class Department_Admin(admin.ModelAdmin):
    # list_display = ['D_name', 'Vacancy']
    prepopulated_fields = {'D_slug': ('D_name',)}
    # list_editable = ['Vacancy']


admin.site.register(Department, Department_Admin)

class CourseAdmin(admin.ModelAdmin):
     # list_display = ['Course','C_slug']
     # list_editable = ['Course']
    prepopulated_fields = {'C_slug':('name',)}
admin.site.register(Course, CourseAdmin)
admin.site.register(Student)
