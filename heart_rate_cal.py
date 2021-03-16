def heart_rate_calculation():
    RestingHR=int(input('RestingHR:'))
    Age=int(input('Age:'))
    print('Intensity|  Rate')
    print('---------|------')
    for intensity in range(55,100,5):
        TargetHeartRate = ((220 - Age) - RestingHR) * intensity/100 + RestingHR
        TargetHeartRate = TargetHeartRate // 1
        print('%d%%      |%dbpm'%(intensity,TargetHeartRate))