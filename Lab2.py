def display_main_menu():
    print("Enter some numbers seperated by commas (e.g. 5, 67, 32)")
    return


    
def calc_average(floatlist):
    average = sum(floatlist) / len(floatlist)
    print("Average:", average)
    return average

def get_user_input():
    x=input()
    splitlist=x.split(',')
    floatlist = [float(num) for num in splitlist]
    print(floatlist)
    return floatlist
    
def find_min_max(floatlist):
    if len(floatlist) == 0:  # Check if the list is empty
        print("No numbers provided.")
        return None, None
    min_temp = min(floatlist)
    max_temp = max(floatlist)
    print("Minimum Temperature:", min_temp)
    print("Maximum Temperature:", max_temp)
    return min_temp, max_temp


def sort_temperature():
    print("sort_temperature")


def calc_median_temperature():
    print("calc_median_temperature")


display_main_menu()
floatlist = get_user_input()
calc_average(floatlist)
find_min_max(floatlist)