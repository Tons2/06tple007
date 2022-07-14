print('Implenetasi Logika Fuzzy')

x_temp = input('Maukan Nilai Temperature (F) = ')
y_cloud = input('Maukan Nilai Cloud Cover (%) = ')

temp = int(x_temp)
cloud = int(y_cloud)

#Proses Fuzziffikasi (temperature)
if temp <= 30 :
	value_frezzing = 1
	value_cool = 0
	value_warm = 0
	value_hot = 0
if temp > 30 and temp <50 :
	value_frezzing = (50 - temp)/(50-30)
	value_cool = (temp - 30)/(50-30)
	value_warm = 0
	value_hot = 0
if temp == 50 :
	value_frezzing = 0
	value_cool = 1
	value_warm = 0
	value_hot = 0
if temp > 50 and temp <70 :
	value_frezzing = 0
	value_cool = (70 - temp)/(70-50)
	value_warm = (temp - 50)/(70-50)
	value_hot = 0
if temp == 70 :
	value_frezzing = 0
	value_cool = 0
	value_warm = 1
	value_hot = 0
if temp > 70 and temp <90 :
	value_frezzing = 0
	value_cool = (90 - temp)/(90-70)
	value_warm = (temp - 70)/(90-70)
	value_hot = 0
if temp == 90 :
	value_frezzing = 0
	value_cool = 0
	value_warm = 0
	value_hot = 1
print('Maka Temperature dalam variabel linguistik, derajat keanggotaan adalah')
print('Freezing', value_freezing)
print('cool', value_cool)
print('warm', value_warm)
print('Hot', value_hot)

#Proses Fuzziffikasi (cloud cover)
if cloud <=20 :
	value_sunny = 1
	value_partlycloudy = 0
	value_overcast = 0
if cloud > 20 and cloud <40 :
	value_sunny = (40 - cloud)/(40-20)
	value_overcast = 0
if cloud > 20 and cloud <50 :
	value_partlycloudy = (cloud - 20)/(50 - 20)
if cloud ==50 :
	value_sunny = 0
	value_partlycloudy = 1
	value_overcast = 0
if cloud > 50 and cloud <80 :
	value_sunny = 0
	value_partlycloudy = (80 - cloud)/(80-50)
if cloud > 60 and cloud <80 :
	value_sunny = 0
	value_overcast = (cloud - 60)/(80-60)
if cloud >=80 :
	value_sunny = 0
	value_partlycloudy = 0
	value_overcast = 1

print('Maka Cloud Cover dalam variabel linguistik, derajat keanggotaan adalah')
print('Sunny', value_sunny)
print('Partly Cloudy', value_partlycloudy)
print('Overcast', value_overcast)

# Proses Inferensi
speed=[]
def fungsiinferensislow (variabel_temp, variabel_cloud):
	if variabel_temp != 0:
		if variabel_cloud !=0:
			hasil_output = min(variabel_temp, variabel_cloud)
			speed.append([hasil_output,75])

fungsiinferensislow(value_freezing, value_sunny)
fungsiinferensislow(value_freezing, value_partlycloudy)
fungsiinferensislow(value_freezing, value_overcast)
fungsiinferensislow(value_cool, value_sunny)
fungsiinferensislow(value_cool, value_partlycloudy)
fungsiinferensislow(value_cool, value_overcast)
fungsiinferensislow(value_warm, value_sunny)
fungsiinferensislow(value_warm, value_partlycloudy)
fungsiinferensislow(value_warm, value_overcast)
fungsiinferensislow(value_hot, value_sunny)
fungsiinferensislow(value_hot, value_partlycloudy)
fungsiinferensislow(value_hot, value_overcast)

print ('Maka Speed Adalah', speed)

perkalian_new =0
pembagian_new =0

for j in range (0, len(speed)):
	perkalian = speed[j][0]*speed[j][1]
	pembagian = speed[j][0]
	perkalian_new = perkalian_new + perkalian
	pembagian_new = pembagian_new + pembagian
z = perkalian_new / pembagian_new
print('Kecepatan Mobil Adlah (z) ', z, '[mph]')