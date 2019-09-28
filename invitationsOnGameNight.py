def add_gamer(gamer, gamers_list):
    if gamer.get('name') and gamer.get('availability'):
        gamers_list.append(gamer)

def build_daily_frequency_table():
    return {
        "Monday":    0,
        "Tuesday":   0,
        "Wednesday": 0,
        "Thursday":  0,
        "Friday":    0,
        "Saturday":  0,
        "Sunday":    0,
           }

def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
        for day in gamer['availability']:
            available_frequency[day] += 1

def find_best_night(availability_table):
    best_availability = 0
    for day, availability in availability_table.items():
        if availability > best_availability:
            best_night = day
            best_availability = availability
    return best_night

def available_on_night(gamers_list, day):
    attending_game_night = []
    for gamer in gamers_list:
        for days in gamer['availability']:
            if day in days:
                attending_game_night.append(gamer['name'])
    return attending_game_night

form_email = '''
Dear {name},
I invite you to participate in the {game} Night, so come by on {day_of_week} and win!
See you soon.
'''

def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        print(form_email.format(name = gamer, game = game, day_of_week = day))



# What's a game we will play?
game = 'Munchkin'

# Creating a players' list
gamers = []

# Adding new players
kimberly = {'name': 'Kimberly Warner', 'availability': ['Monday', 'Tuesday', 'Friday']}
add_gamer(kimberly, gamers)
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

# Build daily frequency table
count_availability = build_daily_frequency_table()

# Calculate availability on each day
calculate_availability(gamers, count_availability)

# Choise of the evening with the greatest availability
game_night = find_best_night(count_availability)

# List of players available that night
attending_game_night = available_on_night(gamers, game_night)

# Sending e-mails with information to available players
send_email(attending_game_night, game_night, game)


print(f'\n---------{game.upper()} will let you know---------\n')
#print(gamers)
#print(count_availability)
print(f'Most would like to play on {game_night}')
print(f'And they are {attending_game_night}')




unable_to_attend_best_night = [gamer for gamer in gamers if gamer['name'] not in attending_game_night]
second_night_availability = build_daily_frequency_table()
calculate_availability(unable_to_attend_best_night, second_night_availability)
second_night = find_best_night(second_night_availability)
available_second_game_night = available_on_night(gamers, second_night)
send_email(available_second_game_night, second_night, game)

