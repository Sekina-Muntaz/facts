from django.db import models
from django.utils.timezone import now
from crontab import CronTab

# Create your models here.
class Client(models.Model):

    name = models.CharField(max_length=255)
    # def __str__(self) -> str:
    #     return str(self.id)
class Loan(models.Model):
    client= models.ForeignKey(Client, on_delete=models.CASCADE)
    amount_required = models.IntegerField() 
    time_issued = models.DateTimeField(default=now)
class Interest(models.Model):
    loan=models.ForeignKey(Loan,on_delete = models.CASCADE)
    interest=models.IntegerField(default=0)
    time=models.DateTimeField(default=now)

    def set_interest(self,interest):
        self.__interest = interest

    def set_loan(self,loan):
        self.__loan = loan

    def set_time(self, time):
        self.__time = time
      
