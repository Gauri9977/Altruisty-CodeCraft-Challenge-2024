def is_valid_strength(value):
    """Check if the strength value is between 1 and 200."""
    return 1 <= value <= 200

def find_strongest_trainee():
    # List to store the strength levels for each trainee across 3 rounds
    trainees = [[], [], [], []]
    
    # Input for 3 rounds of strength values
    for round_num in range(3):
        for trainee_num in range(4):
            try:
                strength = int(input(f"Enter strength for Trainee {trainee_num + 1}, Round {round_num + 1}: "))
                
                # Validate strength value
                if not is_valid_strength(strength):
                    print("INVALID INPUT")
                    return
                
                trainees[trainee_num].append(strength)
            except ValueError:
                print("INVALID INPUT")
                return

    # Calculate average strength for each trainee
    averages = []
    for trainee in trainees:
        avg_strength = round(sum(trainee) / 3)
        averages.append(avg_strength)

    # Debugging output to check averages
    print("Averages:", averages)

    # Find the highest average strength
    max_avg = max(averages)

    # If the highest average is below 100, print "All trainees are unfit"
    if max_avg < 100:
        print("All trainees are unfit.")
        return

    # Output the trainees with the highest average strength
    for i, avg in enumerate(averages):
        if avg == max_avg:
            print(f"Trainee Number : {i + 1}")

# Call the function to execute the program
find_strongest_trainee()
