# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

# Create your views here.

def index(request):
    return render(request, 'index.html')

def buy(request):
    if 'total_quant' not in request.session:
        request.session['total_quant'] = 0
    if 'total_amt' not in request.session:
        request.session['total_amt'] = 0.0

    request.session['order_amt'] = 0.0

    if request.GET['product_id'] == '69':
        request.session['total_quant'] += int(request.GET['shirt_quant'])
        request.session['order_amt'] = int(request.GET['shirt_quant']) * 19.99

    if request.GET['product_id'] == '420':
        request.session['total_quant'] += int(request.GET['sweater_quant'])
        request.session['order_amt'] = int(request.GET['sweater_quant']) * 29.99

    if request.GET['product_id'] == '6969':
        request.session['total_quant'] += int(request.GET['cup_quant'])
        request.session['order_amt'] = int(request.GET['cup_quant']) * 4.99        

    if request.GET['product_id'] == '420420':
        request.session['total_quant'] += int(request.GET['book_quant'])
        request.session['order_amt'] = int(request.GET['book_quant']) * 49.99

    request.session['total_amt'] += request.session['order_amt']
    return redirect('/amadon/checkout')

def checkout(request):
    return render(request, 'result.html')
