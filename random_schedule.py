import numpy as np
from numpy import loadtxt
import csv
from tqdm import tqdm

print('\n=== Welcome to Random-Shift-Generator ===\n')

#import input token
file = open('input_token.csv')
input_token = loadtxt(file, delimiter = ",")

#insert parameters
calandar = 'WWWWWHHHWW'
person_per_day = 5
weekday_interval = 2
holiday_interval = 2

#generate random
def Generate_random(input_token, weekday_interval, holiday_interval):
	token=np.array(input_token)
	calander_filled = [[-1]*person_per_day]*10
	
	for day in calandar:
		today_shift = np.array([])
		if  day == 'W': #day=weekday
			for t in [1]*person_per_day:
				filtered_token = token[token[:,t]>0] #filter out available day = 0
				filtered_token = filtered_token[np.invert(np.isin(filtered_token[:,0], today_shift))] #filter out choosen person
				filtered_token = filtered_token[np.invert(np.isin(filtered_token[:,0], calander_filled[-weekday_interval:]))] #filter out consecutive shift
				selected_person_num = np.random.choice(filtered_token[:,0])
				today_shift = np.append(today_shift, selected_person_num)
				token[int(selected_person_num-1)][t] -= 1
		elif day == 'H': #day=holiday
			for t in [2]*person_per_day:
				filtered_token = token[token[:,t]>0] #filter out available day = 0
				filtered_token = filtered_token[np.invert(np.isin(filtered_token[:,0], today_shift))] #filter out choosen person
				filtered_token = filtered_token[np.invert(np.isin(filtered_token[:,0], calander_filled[-holiday_interval:]))] #filter out consecutive shift
				selected_person_num = np.random.choice(filtered_token[:,0])
				today_shift = np.append(today_shift, selected_person_num)
				token[int(selected_person_num-1)][t] -= 1
		calander_filled.append(today_shift)
	return calander_filled

print('\nStarting program!\n')
for iteration in tqdm(range(100000)) :
	try:
		#try creating shift schedule
		result = np.array(Generate_random(input_token, weekday_interval, holiday_interval))

		#have results! -> save schedule to file
		with open('results/pattern_{}.csv'.format(str(iteration)), 'w', newline='') as file:
			writer = csv.writer(file)
			for line in result[10:, :]:
				writer.writerow(line)

	except Exception as error:
		pass

#WWWWWHHWWWWH





