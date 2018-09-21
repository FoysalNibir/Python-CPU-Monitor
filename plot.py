import psutil
print psutil.cpu_times()
for x in range(3):
    print psutil.cpu_percent(interval=1, percpu=True)

print psutil.cpu_count(logical=False)

print psutil.cpu_freq()
print psutil.sensors_temperatures()
