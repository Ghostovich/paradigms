#Коэффициент корреляции
#Расчет коэффициента корреляции в чистом Python
var_x = sum((item - mean_x)**2 for item in x) / (n - 1)
var_y = sum((item - mean_y)**2 for item in y) / (n - 1)
std_x, std_y = var_x ** 0.5, var_y ** 0.5
r = cov_xy / (std_x * std_y)
print(f'Расчет коэффициента корреляции в чистом Python: {r}')
#Расчет коэффициента корреляции с помощью scipy.stats
r, p = scipy.stats.pearsonr(x_, y_)
print(f'Расчет коэффициента корреляции и p-value, используя функцию pearsonr() в scipy.stats: {r} и {p} ')
scipy.stats.linregress(x_, y_)
print(f'Расчет коэффициента корреляции с помощью scipy.stats.linregress(): {scipy.stats.linregress(x_, y_)}')
result = scipy.stats.linregress(x_, y_)
r = result.rvalue
print(f'Получение доступа к определенным значениям из результата linregress(), включая коэффициент корреляции, используя точечную запись: {r}')
#Расчет коэффициента корреляции с помощью Pandas
r = x__.corr(y__)
r1 = y__.corr(x__)
print(f'Расчет коэффициента корреляции методом .corr() библиотеки Pandas: {r} и {r1}')