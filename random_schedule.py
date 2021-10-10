import numpy as np
from numpy import loadtxt
import csv

print('\n=== Welcome to Random-Shift-Generator ===\n')

#import input token
file = open('input_token.csv')
input_token = loadtxt(file, delimiter = ",")
#insert parameters
calandar = input('Calandar: ').upper()
person_per_day = int(input('Person per day: '))
weekday_interval = int(input('Interval before weekday shift: '))
holiday_interval = int(input('Interval before holiday shift: '))
max_results = int(input('Max results to save: '))


#generate random
def Generate_random(input_token, weekday_interval, holiday_interval):
	token=np.array(input_token)
	calander_filled = [[-1]*person_per_day]*100
	
	for day in calandar:
		today_shift = np.array([])
		if  day == 'W': #day = weekday
			for t in [1]*person_per_day:
				filtered_token = token[token[:,1]>0] #filter out available day = 0
				filtered_token = filtered_token[np.invert(np.isin(filtered_token[:,0], today_shift))] #filter out choosen person
				filtered_token = filtered_token[np.invert(np.isin(filtered_token[:,0], calander_filled[-weekday_interval:]))] #filter out consecutive shift
				selected_person_num = np.random.choice(filtered_token[:,0])
				today_shift = np.append(today_shift, selected_person_num)
				token[int(selected_person_num-1)][1] -= 1	
		elif day == 'H': #day=holiday
			for t in [2]*person_per_day:
				filtered_token = token[token[:,2]>0] #filter out available day = 0
				filtered_token = filtered_token[np.invert(np.isin(filtered_token[:,0], today_shift))] #filter out choosen person
				filtered_token = filtered_token[np.invert(np.isin(filtered_token[:,0], calander_filled[-holiday_interval:]))] #filter out consecutive shift
				selected_person_num = np.random.choice(filtered_token[:,0])
				today_shift = np.append(today_shift, selected_person_num)
				token[int(selected_person_num-1)][2] -= 1	
		
		today_shift.sort()
		calander_filled.append(today_shift)
	return calander_filled

print('\nStarting program!\n')
saved_results = 0
random_count = 0
while saved_results < max_results :
	random_count += 1
	try:
		#try creating shift schedule
		result = np.array(Generate_random(input_token, weekday_interval, holiday_interval))
		#have results! -> save schedule to file
		saved_results += 1
		with open('results/pattern_{}.csv'.format(str(saved_results)), 'w', newline='') as file:
			writer = csv.writer(file)
			for line in result[100:, :]:
				writer.writerow(line)
		print('Try count: {} || Success count: {}/{} ||'.format(random_count, saved_results, max_results))
	except Exception as error:
		print('Try count: {} || Success count: {}/{} || Error: {}'.format(random_count, saved_results, max_results, error))
		pass

#WWWWWHHWWWWH





