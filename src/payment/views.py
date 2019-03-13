import braintree
from django.shortcuts import render, redirect, get_object_or_404, reverse
from kids.models import Kid, Sponsorship, Payment

def payment_process(request, kid_id): 
    
    kidUrl = reverse('kids:kid_detail', args=(kid_id,))
    print(kidUrl)

    if(request.user.is_anonymous):
        return redirect( reverse('accounts:login') + '?next='+  kidUrl)

    kid = get_object_or_404(Kid, pk=kid_id)

    if request.method == 'POST':
        # retrieve nonce
        nonce = request.POST.get('payment_method_nonce', None)
        # create and submit transaction
        result = braintree.Transaction.sale({
            'amount': '100',
            'payment_method_nonce': nonce,
            'options': {
                'submit_for_settlement': True
            }
        })
        if result.is_success:
            sponsorship = get_object_or_404(Sponsorship, sponsor=kid.sponsor, kid=kid_id)
            Payment.objects.create(sponsorship=sponsorship, braintree_id=result.transaction.id, amount=100)
            return redirect('payment:done')
        else:
            return redirect('payment:canceled')
    else:
        # generate token 
        client_token = braintree.ClientToken.generate()
        return render(request, 
                      'payment/process.html', 
                      {'kid': kid,
                       'client_token': client_token})

def payment_done(request):
    return render(request, 'payment/done.html')

def payment_canceled(request):
    return render(request, 'payment/canceled.html')