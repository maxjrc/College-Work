def calculate_speed(distance, time):
    # Convert distance from km to meters
    distance_m = distance * 1000
    
    # Convert time from seconds to hours
    time_h = time / 3600
    
    # Calculate average speed in meters per second
    speed_mps = distance_m / time
    
    # Convert average speed to km/h
    speed_kph = (distance / 1000) / time_h
    
    return speed_kph


def main():
    distance = float(input("Enter the distance between the sensors (in km): "))
    time = float(input("Enter the time taken to travel the distance (in seconds): "))
    
    speed = calculate_speed(distance, time)
    
    print("Average Speed: {:.2f} km/h".format(speed))

main()