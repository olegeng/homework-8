logins=['log123', 'log111', 'loger']
passwords=['oleg2005', '12345678', '1111']
auth=False
def sign_in(sign_log):
	global auth
	numb=-1
	for x in logins:
		if sign_log==x:
			z=0
			while z==0:
				print('Такий логін вже існує, спробуйте придумати інший.')
				sign_log=input('Введіть логін:\n- ')
				for x in logins:
					if sign_log==x:
						break
					elif sign_log!=x:
						z+=1
	if sign_log!=x:
		sign_pass=input('Придумайте пароль:')
		logins.append(sign_log)
		passwords.append(sign_pass)
		auth=True
		zyk=10
		return zyk
def log_in(a,b):
	global auth
	number=-1
	for z in logins:
		number+=1
		if z==a:
			if b==passwords[number]:
				print('Ви успішно авторизувались')
				auth=True
				print(passwords[number])
				return auth
			if b!=passwords[number]:
				x=0
				while x==0:
					number= -1
					a=input('Введите логин:')
					for z in logins:
						number+=1
						if z==a:
							b=input('Введите пароль:')
							if b==passwords[number]:
								print('Ви успішно авторизувались')
								auth=True
								x+=5
								zyk=10
								return zyk
		if z!=a:
			print('Вы ввели неверный логин.')
			x=0
			while x==0:
				number= -1
				a=input('Введите логин:')
				for z in logins:
					number+=1
					if z==a:
						b=input('Введите пароль:')
						if b==passwords[number]:
							print('Ви успішно авторизувались')
							auth=True
							x+=5
							zyk=10
							return zyk
				if z!=a:
					print('Попробуйте ещё раз')
vibir1=input('Авторизація/Регістрація:\n- ')
if vibir1=='Авторизація':
	log=input('Введите логин:')
	pas=input('Введите пароль:')
	log_in(log,pas)
if vibir1=='Регістрація':
	sign_log=input('Введіть логін')
	sign_in(sign_log)
	print(logins)
def rivn(fx):
	spisok=range(-10000,10000)
	for z in spisok:
		fx1=fx.replace('x', str(z))
		fx2=fx1.replace('=', '==')
		numb=fx2.find('==')
		if eval(fx2[0:numb])==eval(fx2[numb+2::]):
			print(z)
			return z
def lomka():
	symbols=["a", "b", "c", "d", "e", 'f', 'g', "h", 'i', "j", 'k', 'l', 'm','n','o','p','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
	parol=input('Введіть пароль який потрібно вгадати: ')
	x=0
	n=0
	word=''
	while x==0:
		for y in symbols:
			if y==str(parol[n]):f
				word+=y
				n+=1
			print('Шукаємо: '+word)
			if word==str(parol):
				print('Пароль:'+word)
				x+=5
				return word
if auth==True:
	vibir2=input('Що робимо?\n-' )
	if vibir2=='Взлом':
		lomka()
	if vibir2=='Рівняння':
		fx=str(input('Введіть рівняння:'))
		rivn(fx)