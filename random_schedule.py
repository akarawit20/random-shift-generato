import numpy as np
from numpy import loadtxt
import csv
from tqdm import tqdm

#input parameters
calandar = 'WHH'+'WWWWWHH'+'WWWWWHH'+'XXXX'+'WHH' #W=weekday, H=holiday
person_per_day = 2
weekday_interval = 1 #days between each shift
holiday_interval = 1

#import input token ([person num, weekday shift count, holiday shift count])
file = open('input_token.csv')
input_token = loadtxt(file, delimiter = ", ")


#generate random -> check if pattern passes criteria -> if passed then save to file / if not then repeat
def Generate_random(input_token, weekday_interval, holiday_interval):
	token=np.array(input_token)
	calander_filled = [[-1]*person_per_day]*10 #placeholder
	
	for day in calandar:
		today_shift = np.array([])

		#day = weekday
		if  day == 'W':
			for t in [1]*person_per_day:
				filtered_token = token[token[:,t]>0] #filter out available day = 0
				filtered_token = filtered_token[np.invert(np.isin(filtered_token[:,0], today_shift))] #filter out choosen person
				filtered_token = filtered_token[np.invert(np.isin(filtered_token[:,0], calander_filled[-weekday_interval:]))] #filter out consecutive shift
				selected_person_num = np.random.choice(filtered_token[:,0])
				today_shift = np.append(today_shift, selected_person_num)
				token[int(selected_person_num-1)][t] -= 1
		
		#day = holiday
		elif day == 'H':
			for t in [2]*person_per_day:
				filtered_token = token[token[:,t]>0] #filter out available day = 0
				filtered_token = filtered_token[np.invert(np.isin(filtered_token[:,0], today_shift))] #filter out choosen person
				filtered_token = filtered_token[np.invert(np.isin(filtered_token[:,0], calander_filled[-holiday_interval:]))] #filter out consecutive shift
				selected_person_num = np.random.choice(filtered_token[:,0])
				today_shift = np.append(today_shift, selected_person_num)
				token[int(selected_person_num-1)][t] -= 1
		
		 #day = blank day
		elif day == 'X':
			today_shift = [0.0]*person_per_day
		calander_filled.append(today_shift)
	return calander_filled

for iteration in tqdm(range(10)):
	try:
		#create random pattern -> result
		result = np.array(Generate_random(input_token, weekday_interval, holiday_interval))

		with open('results/pattern_{}.csv'.format(str(iteration)), 'w', newline='') as file:
			writer = csv.writer(file)
			for line in result[10:, :]: #remove placeholder
				writer.writerow(line)

	except Exception as error:
		pass





