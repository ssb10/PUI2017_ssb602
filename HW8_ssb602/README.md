I have chosen the Restaurant Inspection Dataset from open NYC for plotting. The dataset has Grades and Critical Flag (Leval of Violation).
If you look at the original dataset there are various values of Grades - A,B,C,Z,P - where Z and P stand for not reported and pending respectively. I have dropped these columns. Also for critical flag I have removed all rows having 'Not Applicable' as the critical flag.

Therfore my final dataset has three values of Grades - A,B,C and two values for Critical Flag(Violation) - Critcal and Not Critical.
I have plotted the counts of these two borough-wise which look like the figure shown below. the code for the same is in the iPython notebook which is in the same directory.

![Restuarant Inspectiion Graph](https://github.com/ssb10/PUI2017_ssb602/blob/master/HW8_ssb602/restaurant_inspections_graph.png "analysis of Restaurant Inspection Results where Borough is shown on x-axis and y-axis has counts of various different types of Grades (A,B,C) and level of violations(Critical, Not Critical)")
