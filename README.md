# QueueingSystem

# Problem Statement
Assume there are 3 pipes coming into a building. They each supply ingredients needed to make a cake. 
The eggs arrive at the rate of 30/hour, the flour arrives at 1kg every 2 hours, and the milk arrives at 500mL per 45 minutes. 
A cake requires 2 eggs, 200g of flour, and 150mL of milk. Assume there are three ovens operating at different temperatures and can bake cakes in 17, 30  and 45 minutes.  How many cakes can be made?


# Assumptions
1. In this scenario we assume that there are no left over ingredients from the previous day available to be used for baking
2. The building where we will be baking opens at 4am and closes at 8pm
3. Time for delivery for all ingredients start at 4am and are supplied accordingly
4. The ingredient that arrives latest is flour every 2 hours. So, for the first 2 hours no baking is possible
5. Eventhough working hours are 16, the actual time used to bake cakes is 14 hours

# Functions defined
1. time_to_minutes
This function takes in the opening hours and closing hours of the bakery and converts it to minutes to get the total time the process is to run

2. check_stock
This function checks if there are enough ingredients available to make a cake. It checks the supply for eggs, flour and milk.

3. modify_supplies
The amount of supplies we have for every ingredient in the bakery keeps changing due to 2 reason:	
			1. When the supply of eggs, milk and flour arrive, it's stock increases
			2. When we bake a cake, the stock decreases

4. bake_cake
This is the main function that bakes a cake. The restrictions provided to this function involve:	
			1. Amount of ingredients available in stock
			2. Waiting time for the ovens to complete there current bake
			3. Bottleneck ingredient and it's effect on the process
			4. Idle time of the ovens due to limiting ingredients and their low availability in stock
			5. Functioning of all 3 ovens parallalely to optimize the number of cakes bakes as most time efficient

5. price_calculation
This calculates the cost it takes to bake a single cake considering the costs of all 3 ingredients


# ConclusionConsider we have three ovens now, that is,
Oven 1:bakes the cake in 17 minutes
Oven 2:bakes the cake in 30 minutes
Oven 3:bakes the cake in 45 minutes

Arrival time of the ingredients are: eggs at the rate of 30/hour,the flour at the rate of 500g/hr and 500mL/minutes.

That is flour takes 120 minutes to arrive which is the longest waiting time of the ingredient,there are 30 eggs and 1000ml of milk at this point. Flour is our bottleneck.

At the 121st minute, the cake started to bake in all the three ovens and the amount of ingredients get used up to make the first 3 cake(eggs=60-3(2)=54,flour=(1000-3(200)=400g & milk=1000-(3(150)=550mL).

All the three ovens are busy till the 17th minute from 120th minute. After the 17th minute, i.e. in the 137th minute, oven 1 becomes free and then the next round of baking starts for the same. The same takes place with the other 2 ovens in the 150th and 165th minute.

After the 2nd round in the first 2 ovens and the first round in 3rd oven, eventhough the oven is available no cakes are baked, as the minimum required flour is not available(flour is zero) till the 240th minute and the number of cakes baked is 5.

In the 241st minute the flour arrives and the baking begins once again. Again after 2 round in 1st 2 oven and the first round of 3rd oven no cakes are baked till 360th minute due to the unavailability of the flour. This gets repeated.

The last cakes in all oven are at 858, 871 and 841 th minute respectively.At the end,there are 35 cakes baked in total.

In conclusion, there was a lot of time wasted where no cakes were baked in any of the three oven due to the lack of flour. So in order to increase the number of cakes the shop should provide more quantity of flour and reduce the waiting time for this ingredient.

