from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from decouple import config
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
import stripe

stripe.api_key = config('STRIPE_KEY')

# Create your views here.

def index(request):
	return render(request, 'base/index.html')


def charge(request):
	if request.method == 'POST':
		print('Data:', request.POST)

		amount = int(request.POST['amount'])

		customer = stripe.Customer.create(
			email=request.POST['email'],
			name=request.POST['nickname'],
			source=request.POST['stripeToken']
			)

		charge = stripe.Charge.create(
			customer=customer,
			amount=amount*100,
			currency='usd',
			description="Donation"
			)

	return redirect('success')


def successMsg(request):
	return render(request, 'base/success.html', {})

def process_payment(request):
	form = PayPalPaymentsForm(initial=paypal_dict)
	# order_id = request.session.get('order_id')
	# order = get_object_or_404(Order, id=order_id)
	# host = request.get_host()
	paypal_dict = {
	'business': settings.PAYPAL_RECEIVER_EMAIL,
	'amount': '%.2f' % order.total_cost().quantize(
	Decimal('.01')),
	'item_name': '',#'Order {}'.format(order.id),
	'invoice': '',#str(order.id),
	'currency_code': 'USD',
	'notify_url': 'http://{}{}'.format(host,
	reverse('paypal-ipn')),
	'return_url': 'http://{}{}'.format(host,
	reverse('payment_done')),
	'cancel_return': 'http://{}{}'.format(host,
	reverse('payment_cancelled')),
	}

	form = PayPalPaymentsForm(initial=paypal_dict)
	return render(request, 'base/process_payment.html', {'order': order, 'form': form})

@csrf_exempt
def payment_done(request):
    return render(request, 'base/payment_done.html')


@csrf_exempt
def payment_canceled(request):
    return render(request, 'base/payment_cancelled.html')
