from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from forms import  *
# Create your views here.





#just for demo purpose to be gotten from the DB
sample_bills = [
    "NEPA",
    "DSTV",
    "PHNC"
]

def index_page(request):
    context_dict = {
        'bills' : sample_bills
    }
    return render(request, template_name='app1/index.html', context=context_dict)


def checkout_payment(request):
    checkout_form = None
    if request.method == 'GET':
       checkout_form  = PayPalCheckoutForm()
    elif request.method == 'POST':
        checkout_form = PayPalCheckoutForm(request)

        if checkout_form.is_valid:
            print("print the form is valud")

            amount = checkout_form.clean('amount')
            print ("data of %s" % amount )

            return  HttpResponseRedirect(redirect_to='successfull')


    return render(request, template_name='app1/_payment_bill.html', context={'payment_form': checkout_form})



def successful_payment(request):
    return  render(request, template_name='app1/_successfull.html')