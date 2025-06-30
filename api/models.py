from django.db import models

# Create your models here.
class Employees(models.Model):
    e_id = models.CharField(max_length=50)
    e_name = models.CharField(max_length=255)
    e_email = models.EmailField()
    e_contact = models.IntegerField(default=None)

    def __str__(self):    # How object will be displayed as a string
        return self.e_name
    class Meta:
        db_table = 'api_employees'
        managed = False 

class students(models.Model):
    stu_id= models.IntegerField(primary_key=True)
    stu_name= models.CharField(max_length=100)
    stu_marks = models.IntegerField()
    stu_city = models.CharField(max_length=100)

    def __str__(self):    
        return self.stu_name
    class Meta:
        db_table = 'students'
        managed = False 

class departments(models.Model):
    Depart_id= models.IntegerField(primary_key=True)
    Depart_name = models.CharField(max_length=255)

    def __str__(self):    
        return self.Depart_name
    class Meta:
        db_table = 'departments'
        managed = False 

class courses(models.Model):
    Course_id= models.IntegerField(primary_key=True)
    Course_name= models.CharField(max_length=255)
    student_id = models.IntegerField()

    student_id = models.ForeignKey(
        students,
        on_delete=models.CASCADE,
        db_column= 'student_id'
    )

    def __str__(self):   
        return self.Course_name
    
    class Meta:
        db_table = 'courses'
        managed = False 
