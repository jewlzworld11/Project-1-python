#project 1
print('What type of event is it (type exactly as shown)?')
print()
print('Birthday')
print('Date')
print('Wedding')
print('Reunion')
print('Grad Party')
print('Dance')

input("Your selection:")
if input("What type of event is it?") == Birthday:
     print("The typical budget for birthdays is between $100 and $500")
if input("What type of event is it?") == Date
     print("The typical budget for dates is between $50 and $200")
if input("What type of event is it?") == Wedding
     print("The typical budget for weddings is between $5,000 and $20,000")
if input("What type of event is it?") == Reunion
     print("The typical budget for reunions is between")
if input("What type of event is it?") == Wedding
     print("The typical budget for birthdays is between")
if input("What type of event is it?") == Wedding
     print("The typical budget for birthdays is between")
requested_budget = float(input('what budget did you have in mind (number only) '))
expected_attendees = int(input('How many people will you be expecting? '))
event_duration = int(input('How long will the event last? '))
                        
remaining_budget = (available_budget - requested_budget)
cost_per_person = (requested_budget / expected_attendees)
total_time = (expected_attendees * event_duration)

if requested_budget > available_budget:
    decision = "Sorry i cant do your event"
    reason =  "budget exceeded"

elif expected_attendees < 10:
    decision = "I'll have to put you on the waiting list "
    reason = "Not enough people"
        
elif cost_per_person > 25:
    decision = 'I might consider taking on the event'
    reason = "There's enough people"

else:
    decision = "Worth my time"
    reason = "Cant wait to get started"
    
    
event_type = input('What kind of event is it going to be? ')

if event_type == "academic":
    priority_score = 3
elif event_type == "social":
    priority_score = 2
else:
    priority_score = 1
    
print(f"My decision is {decision}. The reason is {reason}, so i'll make sure you're {priority_score}. ")    
    

    
    
    

