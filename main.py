from pyscript import display, document
import numpy as np
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

import matplotlib.pyplot as plt

plt.figure()
plt.plot([0, 1,], [0, 1])
plt.close()

days = []
absences = []


def displaying(e):
    Day = document.getElementById('Day').value
    absence = int(document.getElementById('absences').value)
    days.append(Day)
    absences.append(absence)
    converted_absences = np.array(absences)


    plt.clf()
    plt.plot(days, converted_absences)
    plt.title('Weekly Attendance (Absences)')
    plt.xlabel('Days')
    plt.ylabel('Absences')
    display(plt.gcf(), target="output", append=False)



absences_data = np.array([0, 2, 4, 6, 8])
days_data = np.array(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])

plt.figure()
sapphire_graph = plt.plot(days_data, absences_data)
plt.plot(days_data, absences_data)
plt.title('Weekly Attendance (Absences)')
plt.xlabel('Days')
plt.ylabel('Absences')