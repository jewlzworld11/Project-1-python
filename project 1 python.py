#project 1
    
event_name = input("what's the name of your event ")    
requested_budget = float(input('what budget did you have in mind '))
available_budget = float(input("WHat's your available budget for this event? "))
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
    

    
    
    


