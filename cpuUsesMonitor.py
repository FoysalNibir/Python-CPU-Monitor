from Tkinter import *
import psutil
import datetime
from multiprocessing import cpu_count



def timeFunc():
    time = datetime.datetime.now().strftime("%I:%M:%S %p")
    date = datetime.datetime.now().strftime("%Y-%m-%d")

    Label(master, text="System Time").grid(row=16, columnspan=2, sticky='w')

    e13 = Entry(master)
    e13.grid(row=16, column=1)
    e13.insert(10, time)

    Label(master, text="System Date").grid(row=17, columnspan=2, sticky='w')

    e14 = Entry(master)
    e14.grid(row=17, column=1)
    e14.insert(10, date)


def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d (H:M:S)" % (hh, mm, ss)


def bat():
    if not hasattr(psutil, "sensors_battery"):
        # outputList.append("Platform not supported")
        Label(master, text="Status").grid(row=10, columnspan=2, sticky='w')
        e9 = Entry(master)
        e9.grid(row=11, column=1)
        e9.insert(10, "Platform not supported")
    batt = psutil.sensors_battery()
    if batt is None:
        # outputList.append("No battery is installed")
        Label(master, text="Status").grid(row=10, columnspan=2, sticky='w')
        e9 = Entry(master)
        e9.grid(row=11, column=1)
        e9.insert(10, "No battery is installed")

    # print("charge:     %s%%" % round(batt.percent, 2))
    if batt.power_plugged:
        Label(master, text="Charge").grid(row=11, columnspan=2, sticky='w')
        charge = "%s%%" % round(batt.percent, 2)
        e9 = Entry(master)
        e9.grid(row=11, column=1)
        e9.insert(10, charge)

        Label(master, text="Time Left").grid(row=12, columnspan=2, sticky='w')
        z = 'N/A'
        e10 = Entry(master)
        e10.grid(row=12, column=1)
        e10.insert(10, z)

        Label(master, text="Status").grid(row=13, columnspan=2, sticky='w')
        x = ("%s" % (
            "Charging" if batt.percent < 100 else "fully charged"
        ))

        e11 = Entry(master)
        e11.grid(row=13, column=1)
        e11.insert(10, x)

        Label(master, text="Plugged in").grid(row=14, columnspan=2, sticky='w')
        y = "Yes"

        e12 = Entry(master)
        e12.grid(row=14, column=1)
        e12.insert(10, y)

        # outputList.append(y)
        # print("plugged in: yes")
    else:
        Label(master, text="Charge").grid(row=11, columnspan=2, sticky='w')
        charge = "%s%%" % round(batt.percent, 2)
        e9 = Entry(master)
        e9.grid(row=11, column=1)
        e9.insert(10, charge)

        Label(master, text="          ").grid(row=12, columnspan=2, sticky='w')
        Label(master, text="Time Left").grid(row=12, columnspan=2, sticky='w')
        x = ("%s" % secs2hours(batt.secsleft))
        Label(master, text="                  ").grid(row=13, columnspan=2, sticky='w')
        Label(master, text="Status").grid(row=13, columnspan=2, sticky='w')
        y = "%s" % "discharging"
        Label(master, text="          ").grid(row=14, columnspan=2, sticky='w')
        Label(master, text="Plugged in").grid(row=14, columnspan=2, sticky='w')
        z = "No"

        e10 = Entry(master)
        e10.grid(row=12, column=1)
        e10.insert(10, x)

        e11 = Entry(master)
        e11.grid(row=13, column=1)
        e11.insert(10, y)

        e12 = Entry(master)
        e12.grid(row=14, column=1)
        e12.insert(10, z)

        # outputList.append(x)
        # print("Plugged in: no")


def main():
    global outputList

    totalRam = 1.0
    totalRam = psutil.virtual_memory()[0] * totalRam
    totalRam = str("{:.4f}".format(totalRam / (1024 * 1024 * 1024))) + ' GB'

    availRam = 1.0
    availRam = psutil.virtual_memory()[1] * availRam
    availRam = str("{:.4f}".format(availRam / (1024 * 1024 * 1024))) + ' GB'

    ramUsed = 1.0
    ramUsed = psutil.virtual_memory()[3] * ramUsed
    ramUsed = str("{:.4f}".format(ramUsed / (1024 * 1024 * 1024))) + ' GB'

    ramFree = 1.0
    ramFree = psutil.virtual_memory()[4] * ramFree
    ramFree = str("{:.4f}".format(ramFree / (1024 * 1024 * 1024))) + ' GB'

    core = cpu_count()
    ramUsages = str(psutil.virtual_memory()[2]) + '%'
    cpuPer = str(psutil.cpu_percent()) + '%'
    cpuMainCore = psutil.cpu_count(logical=False)

    outputList.append(cpuMainCore)
    outputList.append(core)
    outputList.append(cpuPer)
    outputList.append(totalRam)
    outputList.append(availRam)
    outputList.append(ramUsed)
    outputList.append(ramUsages)
    outputList.append(ramFree)


def clock():
    global outputList
    outputList = []
    main()
    bat()
    timeFunc()
    master.update_idletasks()
    e1 = Entry(master)
    e2 = Entry(master)
    e3 = Entry(master)
    e4 = Entry(master)
    e5 = Entry(master)
    e6 = Entry(master)
    e7 = Entry(master)
    e8 = Entry(master)

    e1.grid(row=1, column=1)
    e2.grid(row=2, column=1)
    e3.grid(row=3, column=1)
    e4.grid(row=5, column=1)
    e5.grid(row=6, column=1)
    e6.grid(row=7, column=1)
    e7.grid(row=8, column=1)
    e8.grid(row=9, column=1)

    e1.insert(10, outputList[0])
    e2.insert(10, outputList[1])
    e3.insert(10, outputList[2])
    e4.insert(10, outputList[3])
    e5.insert(10, outputList[4])
    e6.insert(10, outputList[5])
    e7.insert(10, outputList[6])
    e8.insert(10, outputList[7])

    master.after(1000, clock)


if __name__ == '__main__':
    master = Tk()
    master.title('System Monitor')
    Label(master, text="CPU Info").grid(row=0, columnspan=2, sticky='e')
    Label(master, text="Total CPU CORE").grid(row=1, columnspan=2, sticky='w')
    Label(master, text="Total Logical Processors").grid(row=2)
    Label(master, text="CPU Usages").grid(row=3, columnspan=2, sticky='w')
    Label(master, text="RAM Info").grid(row=4, columnspan=2, sticky='e')
    Label(master, text="Total RAM").grid(row=5, columnspan=2, sticky='w')
    Label(master, text="Available RAM").grid(row=6, columnspan=2, sticky='w')
    Label(master, text="RAM Used").grid(row=7, columnspan=2, sticky='w')
    Label(master, text="RAM Usages").grid(row=8, columnspan=2, sticky='w')
    Label(master, text="RAM Free").grid(row=9, columnspan=2, sticky='w')
    Label(master, text="Battery Info").grid(row=10, columnspan=2, sticky='e')
    Label(master, text="Additional").grid(row=15, columnspan=2, sticky='e')
    Label(master, text=u'\N{COPYRIGHT SIGN}' " foysal_nibir 2018", fg='red').grid(row=19, columnspan=2, sticky='n', )

    outputList = []

    clock()
    master.update_idletasks()

    master.mainloop()
