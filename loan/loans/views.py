from django.shortcuts import render
from .models import Loan,Interest
import datetime
from crontab import CronTab


# Create your views here.
loans=Loan.objects.all()
def index(request):
    
    
    return render(request,"index.html")

    

def calculate_interest(request):
    
    interest=0
    r=0.5
    for loan in loans:
        interest_obj=Interest.objects.filter(loan_id=loan.id)
        print(interest_obj)
        for i in interest_obj:

            if loan.id==i.loan_id:

                amount=loan.amount_required
                interest=amount*r
                interest_obj.update(interest=interest)
                print(amount)
            else:
                amount=i.interest
                interest=amount*r
                print(amount)
                interest_obj.create(loan_id=loan.id,interest=interest)
    
    

        
    return render(request,'index.html')


    



     