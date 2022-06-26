This program is for creating random shift pattern
requirement
1. input_token.csv <- declare number of weekday and holiday shifts for each person
2. input parameters

How it works?
1. This program will iterate over each day from calendar, and each person slot within a day
2. list available persons with remaining shift count >0 for that day type (e.g. weekday, holiday)
3. Filter out person with shift in this day (already have been choosen)
4. Filter out person with shift in previous (can specify; 1, 2, ...) days
5. Randomly choose a person form the remaining list, add this person to today shift calenday
6. Subtract 1 from the choosen person shift count of the day type (e.g. weekday, holiday)
7. Move to next person in this day and repeat until day is full
8. Move to next day and repeat until calenday is full

if step 5 fail (no one is available to be choosen), this program will restart from step 1

if step 5 fail multiple times -> ~shift with current parameter settings may not be possible
solutions:
- decrease weekday/holiday interval
- wait longer (may be up to 10 minutes for each successful pattern)