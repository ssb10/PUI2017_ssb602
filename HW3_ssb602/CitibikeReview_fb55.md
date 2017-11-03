** NUll Hypothesis **

Null hypothesis: Citi Bike usage is same or more for weekdays than weekends
Alternative hypothesis: Citi Bike usage is more on weekends

The null and alternatives are not clear: what is the bike usage? number of rides? total riding time? average trip duration? this must be specified clearly. The null/alt should also be expressed as formulae. 

The significance should be stated early on w the null/alt

** Data **
it may be ok but it depends on the definition of the null/alt

** test ** 
same as data: it depends on the null/alt
if average trip duration: then  a Mann Whitney u test is a non paraetric way to compare means, and a z test is a simpler, but parametri solution. however the distributions may not satisfies the assumptions (normality)

if number of trips then you are testing counts, but parametric tests would not be good cause they assume poisson, but Moods test of median can be used.

** state whi it is interesting!

