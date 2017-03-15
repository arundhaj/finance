from django.shortcuts import render
from finance_app.models import NseStockQuote
from django.http.response import JsonResponse

import json
from datetime import datetime

# Create your views here.
def index(request):
    icici_records = NseStockQuote.objects.values_list('scriptdate', 'close').filter(symbol='ICICIBANK').order_by('-scriptdate')
    context = {
        'icici_records': icici_records
    }

    return render(request, 'finance_app/index.html', context)

def get_quote(request):
    # http://localhost:8000/analytics/api/compressor_cycle/D_a6-c9?startdate=1476489600&enddate=1479168000
    symbol = request.GET.get('symbol')
    
    quotes = NseStockQuote.objects.values('scriptdate', 'close').filter(symbol=symbol).order_by('-scriptdate')
    
    quotes_list = [[quote['scriptdate'].timestamp(), quote['close']] for quote in quotes]

    return JsonResponse(quotes_list, safe=False)