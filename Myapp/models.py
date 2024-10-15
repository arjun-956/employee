from django.db import models

class Employee(models.Model):

    name=models.CharField(max_length=30)
    age=models.PositiveIntegerField()
    salary=models.PositiveBigIntegerField()
    designation=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.IntegerField()

    def _str_(self):
        return self.name
        
class Work(models.Model):

    title = models.CharField(max_length=200)

    description=models.CharField(max_length=200)

    start_date=models.DateField(null=True)

    end_date=models.DateField(null=True)

    status_options=(
        ("created","created"),
        ("wip","wip"),
        ("completed","completed"),
        ("due","due")
    )

    status=models.CharField(max_length=200,choices=status_options,default="created")


    def _str_(self):

        return self.title