import psutil
# print psutil.cpu_times()
# # for x in range(3):
# #     print psutil.cpu_percent(interval=1, percpu=True)
#
# print psutil.cpu_count(logical=False)
#
# print psutil.cpu_freq()
# print psutil.sensors_battery()
# print psutil.net_connections(kind='inet4')


import sys

import psutil


def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d (H:Min:Sec)" % (hh, mm, ss)


def main():
    if not hasattr(psutil, "sensors_battery"):
        return sys.exit("platform not supported")
    batt = psutil.sensors_battery()
    if batt is None:
        return sys.exit("no battery is installed")

    #print("charge:     %s%%" % round(batt.percent, 2))
    if batt.power_plugged:
        x = ("charge:     %s%%" % round(batt.percent, 2)+
            "\nStatus:     %s" % (
            "Charging" if batt.percent < 100 else "fully charged"
            )+"\nPlugged in: Yes")
        print (x)
        #print("plugged in: yes")
    else:
        x = ("Charge:     %s%%" % round(batt.percent, 2)+
             "\nLeft:       %s\n" % secs2hours(batt.secsleft) +
             "Status:     %s" % "discharging \n"+
             "Plugged in: No")
        print(x)
        #print("Plugged in: no")


if __name__ == '__main__':
    main()
    #print(psutil.sensors_temperatures(fahrenheit=False))
