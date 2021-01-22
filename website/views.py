from django.shortcuts import render, redirect


def home(request):
	return render(request, 'home.html', {})


def blueprint(request):
	return render(request, 'blueprint.html', {})


def calc(request):
	if request.method == 'POST':
		a = request.POST['vala']
		b = request.POST['valb']
		c = request.POST['valc']
		d = request.POST['vald']
		e = request.POST['vale']
		f = request.POST['valf']
		g = request.POST['valg']
		h = request.POST['valh']

		if a and b and c and f and d and g and e and h:
			try:
				val1 = float(f)/(((float(b)+float(f))/float(c))-(float(b)/float(a)))
				val2 = ((float(a)-float(d))*float(b)*float(g))/((float(d)-float(g))*float(a))
				val3 = ((float(b)+float(h))/(float(b)/float(a)+float(h)/float(e)))
			except ValueError:
				pass
			return render(request, 'calc.html', {'a':a, 'b':b, 'c':c, 'f':f, 'd':d, 'g':g, 'e':e, 'h':h, 'val1': "%.2f" % val1, 'val2': "%.2f" % val2, 'val3': "%.2f" % val3})

		elif a and b and c and f and d and g:
			try:
				val1 = float(f)/(((float(b)+float(f))/float(c))-(float(b)/float(a)))
				val2 = ((float(a)-float(d))*float(b)*float(g))/((float(d)-float(g))*float(a))
			except ValueError:
				pass
			return render(request, 'calc.html', {'a':a, 'b':b, 'c':c, 'f':f, 'd':d, 'g':g, 'val1': "%.2f" % val1, 'val2': "%.2f" % val2})

		elif a and b and c and f and e and h:
			try:
				val1 = float(f)/(((float(b)+float(f))/float(c))-(float(b)/float(a)))
				val3 = ((float(b)+float(h))/(float(b)/float(a)+float(h)/float(e)))
			except ValueError:
				pass
			return render(request, 'calc.html', {'a':a, 'b':b, 'c':c, 'f':f, 'e':e, 'h':h, 'val1': "%.2f" % val1, 'val3': "%.2f" % val3})

		elif a and b and d and g and e and h:
			try:
				val2 = ((float(a)-float(d))*float(b)*float(g))/((float(d)-float(g))*float(a))
				val3 = ((float(b)+float(h))/(float(b)/float(a)+float(h)/float(e)))
			except ValueError:
				pass
			return render(request, 'calc.html', {'a':a, 'b':b, 'd':d, 'g':g, 'e':e, 'h':h, 'val2': "%.2f" % val2, 'val3': "%.2f" % val3})

		elif a and b and c and f:
			try:
				val1 = float(f)/(((float(b)+float(f))/float(c))-(float(b)/float(a)))
			except ValueError:
				pass
			return render(request, 'calc.html', {'a':a, 'b':b, 'c':c, 'f':f, 'val1': "%.2f" % val1})

		elif a and b and d and g:
			try:
				val2 = ((float(a)-float(d))*float(b)*float(g))/((float(d)-float(g))*float(a))
			except ValueError:
				pass
			return render(request, 'calc.html', {'a':a, 'b':b, 'd':d, 'g':g, 'val2': "%.2f" % val2})

		elif a and b and e and h:
			try:
				val3 = ((float(b)+float(h))/(float(b)/float(a)+float(h)/float(e)))
			except ValueError:
				pass
			return render(request, 'calc.html', {'a':a, 'b':b, 'e':e, 'h':h, 'val3': "%.2f" % val3})

		else:
			return render(request, 'calc.html', {'val1': print('error'), 'val2': print('error'), 'val3': print('error')})

	else:
		return render(request, 'calc.html', {})


def calc_en(request):
	if request.method == 'POST':
		a1 = request.POST['val1']
		b1 = request.POST['val2']
		c1 = request.POST['val3']
		d1 = request.POST['val4']
		e1 = request.POST['val5']
		f1 = request.POST['val6']
		g1 = request.POST['val7']
		h1 = request.POST['val8']

		if a1 and b1 and c1 and f1 and d1 and g1 and e1 and h1:
			try:
				vala = float(f1)/(((float(b1)+float(f1))/float(c1))-(float(b1)/float(a1)))
				valb = ((float(a1)-float(d1))*float(b1)*float(g1))/((float(d1)-float(g1))*float(a1))
				valc = ((float(b1)+float(h1))/(float(b1)/float(a1)+float(h1)/float(e1)))
			except ValueError:
				pass
			return render(request, 'calc_en.html', {'a1':a1, 'b1':b1, 'c1':c1, 'f1':f1, 'd1':d1, 'g1':g1, 'e1':e1, 'h1':h1, 'vala': "%.2f" % vala, 'valb': "%.2f" % valb, 'valc': "%.2f" % valc})

		elif a1 and b1 and c1 and f1 and d1 and g1:
			try:
				vala = float(f1)/(((float(b1)+float(f1))/float(c1))-(float(b1)/float(a1)))
				valb = ((float(a1)-float(d1))*float(b1)*float(g1))/((float(d1)-float(g1))*float(a1))
			except ValueError:
				pass
			return render(request, 'calc_en.html', {'a1':a1, 'b1':b1, 'c1':c1, 'f1':f1, 'd1':d1, 'g1':g1, 'vala': "%.2f" % vala, 'valb': "%.2f" % valb})

		elif a1 and b1 and c1 and f1 and e1 and h1:
			try:
				vala = float(f1)/(((float(b1)+float(f1))/float(c1))-(float(b1)/float(a1)))
				valc = ((float(b1)+float(h1))/(float(b1)/float(a1)+float(h1)/float(e1)))
			except ValueError:
				pass
			return render(request, 'calc_en.html', {'a1':a1, 'b1':b1, 'c1':c1, 'f1':f1, 'e1':e1, 'h1':h1, 'vala': "%.2f" % vala, 'valc': "%.2f" % valc})

		elif a1 and b1 and d1 and g1 and e1 and h1:
			try:
				valb = ((float(a1)-float(d1))*float(b1)*float(g1))/((float(d1)-float(g1))*float(a1))
				valc = ((float(b1)+float(h1))/(float(b1)/float(a1)+float(h1)/float(e1)))
			except ValueError:
				pass
			return render(request, 'calc_en.html', {'a1':a1, 'b1':b1, 'd1':d1, 'g1':g1, 'e1':e1, 'h1':h1, 'valb': "%.2f" % valb, 'valc': "%.2f" % valc})

		elif a1 and b1 and c1 and f1:
			try:
				vala = float(f1)/(((float(b1)+float(f1))/float(c1))-(float(b1)/float(a1)))
			except ValueError:
				pass
			return render(request, 'calc_en.html', {'a1':a1, 'b1':b1, 'c1':c1, 'f1':f1, 'vala': "%.2f" % vala})

		elif a1 and b1 and d1 and g1:
			try:
				valb = ((float(a1)-float(d1))*float(b1)*float(g1))/((float(d1)-float(g1))*float(a1))
			except ValueError:
				pass
			return render(request, 'calc_en.html', {'a1':a1, 'b1':b1, 'd1':d1, 'g1':g1, 'valb': "%.2f" % valb})

		elif a1 and b1 and e1 and h1:
			try:
				valc = ((float(b1)+float(h1))/(float(b1)/float(a1)+float(h1)/float(e1)))
			except ValueError:
				pass
			return render(request, 'calc_en.html', {'a1':a1, 'b1':b1, 'e1':e1, 'h1':h1, 'valc': "%.2f" % valc})

		else:
			return render(request, 'calc_en.html', {'vala': print('error'), 'valb': print('error'), 'valc': print('error')})

	else:
		return render(request, 'calc_en.html', {})


def mystyle(request):
	return render(request, 'mystyle.html', {})