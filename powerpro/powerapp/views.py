from django.shortcuts import render
from django.http import HttpResponse
import math
def testing(request):
	a=5
	s=math.pow(a,3)
	x='<h1><font color="red">VALUE IS...'+str(a)+'POWER VALUE IS...'+str(s)+'</font></h1>'
	return HttpResponse(x)