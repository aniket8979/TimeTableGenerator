import random


num_subjects = 5
num_days = 5
num_hours = 5

subjects = ["Subject" + str(i) for i in range(1, num_subjects + 1)]

teacher_max_working_hours = 25

teachers_working_hours = {

    "teacher1": 14,
    "teacher2": 19,
    "teacher3": 0,
    "teacher4": 14,
    "teacher5": 7,

}

subject_teacher = {

    "Subject1": "teacher1",
    "Subject2": "teacher2",
    "Subject3": "teacher3",
    "Subject4": "teacher4",
    "Subject5": "teacher5"

}

# Define the number of hours for each subject
subject_hours = {

    "Subject1": 10,
    "Subject2": 6,
    "Subject3": 3,
    "Subject4": 4,
    "Subject5": 2,

}



# def time_slots():
#     my_list = ['other_subjects']*10 + [None]*15
#     random.shuffle(my_list)
#     return my_list

# time_table_update = [None] * 25




def time_slots():
    my_list =  [None]*25
    return my_list

time_table_update = [None] * 25

t1 = list(time_slots())
t2= list(time_slots())
t3 = list(time_slots())
t4 = list(time_slots())
t5 = list(time_slots())

teacher_schedule = {
    
    "teacher1": t1,
    "teacher2": t2,
    "teacher3": t3,
    "teacher4": t4,
    "teacher5": t5
}




final_timetable = []


    #         "day1": [None, "SomeData", None, None, "SomeData"],
    #         "day2": ["SomeData", None, "SomeData", None, None],
    #         "day3": [None, None, None, None, None],
    #         "day4": [None, None, None, "SomeData", None],
    #         "day5": ["SomeData", "SomeData", None, None, None]


# def mutation():
    
#     timetable = population[0]


#     for subject, hours in subject_hours.keys():
#         teacher = subject_teacher[subject]
#         # login can be implemented of comparing hours of teachers who is working less can be assigned
#         teacher_hour = (teacher_max_working_hours - int(teachers_working_hours[teacher]))
#         if hours <= teacher_hour :
#             # day = 0
#             # tea_hour = 0
#             # for sub in range(timetable):
#             #     if sub == subject and teacher_schedule[day][tea_hour] == None:
            
#             currentLeftHours = timetable.count(subject)

#             for day in range(num_days):
#                 teacher_time = teacher_schedule[teacher][day]
#                 for hour in range(num_hours):

#                     if timetable[hour] == subject and teacher_time[num_hours] == None:
#                         teacher_time[num_hours] = subject
#                         currentLeftHours = currentLeftHours - 1
#                     else:
#                         continue


#                     left_hours = hours
#                     while left_hours >= 1:



#         else:
#             # change teacher



# def mutation(individual):
#     hours_count = {subject: individual.count(subject) for subject in subjects}

#     for subject, hour in subject_hours.items():

#         if hours_count[subject] < hour:
#             pos = random.randint(0, len(individual) - 1)
#             while individual[pos] == subject:
#                 if pos > 1 and individual[pos-2] == subject:
#                     if
#                 else:
#                     print("logic")
               
                
#                 pos = random.randint(0, len(individual) - 1)
            
#             individual[pos] = subject

#             break
#     return individual




    # hours_count = {subject: timetable.count(subject) for subject in subjects}


    # # div = num_days/num


    # for subject, hour in subject_hours.items():


    #     # day1 = best_timetable[:5]
    #     # day2 = best_timetable[5:10]
    #     # day3 = best_timetable[10:15]
    #     # day4 = best_timetable[15:20]
    #     # day5 = best_timetable[20:25]



    #     if hours_count[subject] < hour:

    #         pos = random.randint(0, len(timetable) - 3)

    #         while timetable[pos] == subject or (
    #             pos > 2
    #             and timetable[pos - 2] == subject
    #             and timetable[pos + 2] == subject
    #         ):
    #             pos = random.randint(0, len(timetable) - 3)
            
    #         timetable[pos] = subject            

    #         break 


        # for day in range(num_days):

        #     for hour in range(num_hours):
        #         subject = individual[day][hour]
        #         teacher = subject_teacher[subject]
        #         tea_schedule = teacher_schedule[teacher]
        #         teacher_hours = tea_schedule["day"+(hour+1)]




    # return timetable





def mutation(individual):
    hours_count = {subject: individual.count(subject) for subject in subjects}

    for subject, hour in subject_hours.items():

        if hours_count[subject] < hour:
            pos = random.randint(0, len(individual) - 3)


            while pos%num_hours == 0 and individual[pos] == subject or (
                pos > 1
                and individual[pos - 2] == subject
                and individual[pos + 2] == subject
            ):
                
                # Mutation logic to be written here.
                
                pos = random.randint(0, len(individual) - 3)

            
            individual[pos] = subject
        

            break
    return individual






def get_indices(lst, element):
    return [i for i, x in enumerate(lst) if x == element]



def updated_mutation(individual: list):
    hours_count = {subject: individual.count(subject) for subject in subjects}

    for subject, hour in subject_hours.items():

        while hours_count[subject] < hour:

            slot = random.randint(0, len(individual)-1)
            
            if teacher_schedule[subject_teacher[subject]][slot] is None and time_table_update[slot] is None:

                if individual[slot] == subject and time_table_update[slot] is None:
                    teacher_schedule[slot] = subject
                    # individual[slot] = subject
                    time_table_update[slot] = subject
                    hours_count[subject] -=1

                elif (slot+1)%num_hours == 0 and (individual[slot - 2] != subject):
                    teacher_schedule[slot] = subject
                    time_table_update[slot] = subject
                    hours_count[subject] -=1

                else:
                    if slot+2 <= (len(individual)-1):

                        if individual[slot - 2] == subject and individual[slot + 2] == subject:
                            slot = random.randint(0, len(individual)-1) 
                        
                        else:
                            teacher_schedule[slot] = subject
                            individual[slot] = subject
                            time_table_update[slot] = subject
                            hours_count[subject] -=1
                    else:
                        slot = random.randint(0, len(individual)-1)
            else:
                slot = random.randint(0, len(individual)-1)

    return individual







def create_individual():
    individual = []
    for subject, hours in subject_hours.items():
        individual += [subject] * hours
    random.shuffle(individual)
    return individual






def selection(population):
    return random.choice(population)




def crossover(ind1, ind2):
    pos = random.randint(0, len(ind1) - 1)
    return ind1[:pos] + ind2[pos:], ind2[:pos] + ind1[pos:]




def fitness(individual):
    fitness = 0

    for i in range(len(individual) - 2):
        # I can add more logic here such as availability of teahcer,
        # More logic can be added to check things such as if time collapse.
        if individual[i] != individual[i + 2]:
            fitness += 1

    return fitness






































population = [create_individual() for _ in range(1000)]


for generation in range(1001):
    print("Generation: ", generation)
    population = sorted(population, key=fitness, reverse=True)

    if fitness(population[0]) == num_days * num_hours - 1:
        break
    next_generation = population[:20]
    for _ in range(80):
        ind1 = selection(population)
        ind2 = selection(population)
        child1, child2 = crossover(ind1, ind2)
        child1 = mutation(child1)
        child2 = mutation(child2)
        next_generation += [child1, child2]
    population = next_generation




# Print the best timetable
best_timetable = population[0]
timet = updated_mutation(best_timetable)

print(timet)

print(teacher_schedule)


