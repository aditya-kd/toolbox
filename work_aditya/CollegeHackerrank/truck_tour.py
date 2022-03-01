def truckTour(arr):
    # Write your code here
    pump=0
    petrol=0
    for i in range(len(arr)):
        petrol += arr[i][0]-arr[i][1]
        if petrol <0:
            # print(pump)
            pump=i+1
            petrol =0
            # print(pump)
            # petrol-=1
    return pump