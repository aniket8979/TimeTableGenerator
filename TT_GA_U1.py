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

    # print(fitness)
    return fitness



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



def updated_mutation(individual: list):
    hours_count = {subject: individual.count(subject) for subject in subjects}
    print(hours_count)

    loop = 0

    for subject, hour in subject_hours.items():
    
        # while hours_count[subject] <= hour:
                
        while time_table_update.count(subject) <= hour-1:
                slot = random.randint(0, len(individual)-1)
                
                if teacher_schedule[subject_teacher[subject]][slot] is None and time_table_update[slot] is None:

                    if individual[slot] == subject and time_table_update[slot] is None:
                        teacher_schedule[subject_teacher[subject]][slot] = subject 
                        # individual[slot] = subject
                        time_table_update[slot] = subject
                        hours_count[subject] = hours_count[subject]-1
                        
                    elif (slot+1)%num_hours == 0 and (individual[slot - 2] != subject):
                        teacher_schedule[subject_teacher[subject]][slot] = subject
                        time_table_update[slot] = subject
                        hours_count[subject] = hours_count[subject]-1

                    else:
                        if slot+2 <= (len(individual)-1):

                            if individual[slot - 2] == subject or individual[slot + 2] == subject:
                                slot = random.randint(0, len(individual)-1) 
                            
                            else:
                                teacher_schedule[subject_teacher[subject]][slot] = subject
                                individual[slot] = subject
                                time_table_update[slot] = subject
                                hours_count[subject] = hours_count[subject]-1
                        else:
                            slot = random.randint(0, len(individual)-1)
                else:
                    loop +=1
                    if loop < 5000:
                        slot = random.randint(0, len(individual)-1)
                    else:
                        # Create logic for break condition when subject is not being assinged.
                        # check which subjects are assigned more subjects.
                        # get their index value of more assinged subjects.
                        # compare values, and pick random index from extra.
                        # assign less subject into that random index.
                        break
                    

    return individual





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



# Print the working hours of each teacher
for teacher, hours in teachers_working_hours.items():
    print(teacher, "worked for", hours, "hours")

print("")

print("mutation to assign subjects to teachers")

a = updated_mutation(population[0])
print("")
print("New timetable")
print("")
print(a)


for j, k in teacher_schedule.items():
    print("")
    print(j,k)
    print("")


print("required: ", subject_hours.get("Subject1") ,"achived: ", teacher_schedule["teacher1"].count("Subject1"), "on Timetable: ",time_table_update.count("Subject1"))
print("required: ", subject_hours.get("Subject2") ,"achived: ", teacher_schedule["teacher2"].count("Subject2"), "on Timetable: ",time_table_update.count("Subject2"))
print("required: ", subject_hours.get("Subject3") ,"achived: ", teacher_schedule["teacher3"].count("Subject3"), "on Timetable: ",time_table_update.count("Subject3"))
print("required: ", subject_hours.get("Subject4") ,"achived: ", teacher_schedule["teacher4"].count("Subject4"), "on Timetable: ",time_table_update.count("Subject4"))
print("required: ", subject_hours.get("Subject5") ,"achived: ", teacher_schedule["teacher5"].count("Subject5"), "on Timetable: ",time_table_update.count("Subject5"))