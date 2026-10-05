available_budget = 10000.0

print('What type of event is it (type exactly as shown)?')
print()
print('Birthday')
print('Date')
print('Wedding')
print('Reunion')
print('Grad Party')
print('Dance')

selection = input("\nYour selection: ").strip()

if selection.lower() == "birthday":
    print("The typical budget for birthdays is between $100 and $500.")
elif selection.lower() == "date":
    print("The typical budget for dates is between $50 and $200.")
elif selection.lower() == "wedding":
    print("The typical budget for weddings is between $5,000 and $20,000.")
elif selection.lower() == "reunion":
    print("The typical budget for reunions is between $1,000 and $5,000.")
elif selection.lower() == "grad party":
    print("The typical budget for grad parties is between $200 and $1,000.")
elif selection.lower() == "dance":
    print("The typical budget for dances is between $500 and $2,500.")
else:
    print("Event type not recognized, using standard estimates.")

print()
requested_budget = float(input('What budget did you have in mind (number only)? '))
expected_attendees = int(input('How many people will you be expecting? '))
event_duration = int(input('How long will the event last (in hours)? '))

remaining_budget = available_budget - requested_budget
cost_per_person = requested_budget / expected_attendees if expected_attendees > 0 else 0
total_time = expected_attendees * event_duration

if requested_budget > available_budget:
    decision = "Sorry, I can't do your event"
    reason = "budget exceeded"
elif expected_attendees < 10:
    decision = "I'll have to put you on the waiting list"
    reason = "not enough people"
elif cost_per_person > 25:
    decision = "I might consider taking on the event"
    reason = "budget per person meets requirements"
else:
    decision = "Worth my time"
    reason = "can't wait to get started"

event_type = input('\nWhat category is it (academic/social/other)? ').strip().lower()

if event_type == "academic":
    priority_score = 3
elif event_type == "social":
    priority_score = 2
else:
    priority_score = 1

print(f"\nMy decision is: {decision}. The reason is {reason}, so priority tier is set to {priority_score}.")