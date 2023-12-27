# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
# Need to rework this function
def time_to_minutes(time_str):
    # Split the time string into hours and minutes
    hours, minutes = map(int, time_str[:-2].split(':'))
    # Add 12 to the hour if it's PM
    if time_str[-2:].lower() == 'pm':
        hours += 12
    # Convert the time to minutes
    return hours * 60 + minutes

# %%
def check_stock(counts, cake_requirements):
    # Check if there are enough ingredients to make a cake
    for ingredient in cake_requirements.keys():
        if counts[ingredient] >= cake_requirements[ingredient]:
            continue
        else:
            return False
    return True

# %%
def bake_cake(current_time, counts, cake_requirements, total_time, oven_clocks):
    if check_stock(counts, cake_requirements):
        for oven in oven_clocks.keys():
            # checks if oven is available based on the oven clock  
            if oven_clocks[oven]['current_time'] % oven_clocks[oven]['bake_time'] == 0:
                # Make a cake by reducing ingredient quantities
                if (total_time - current_time) >= oven_clocks[oven]['bake_time'] and check_stock(counts, cake_requirements):
                    oven_clocks[oven]['available'] = False
                    oven_clocks[oven]['start_time'] = current_time
                    counts['cakes'] += 1
                    modify_supplies(current_time, supply_arrival_delay, cake_requirements, counts, add_supplies=False)
            else:
                # if oven will be available in the next min reset it
                if ((current_time - oven_clocks[oven]['start_time']) + 1) == oven_clocks[oven]['bake_time']:
                    oven_clocks[oven]['available'] = True
                    oven_clocks[oven]['current_time'] = 0
            
            # if oven is being used increment it's clock
            if not oven_clocks[oven]['available']:
                oven_clocks[oven]['current_time'] += 1
    else:
        # if we don't have any supplies left we still need to check if oven is baking and if it needs resetting
        for oven in oven_clocks.keys():
            # if oven will be available in the next min reset it
            if ((current_time - oven_clocks[oven]['start_time']) + 1) == oven_clocks[oven]['bake_time']:
                    oven_clocks[oven]['available'] = True
                    oven_clocks[oven]['current_time'] = 0
                    
            # if oven is being used increment it's clock      
            if not oven_clocks[oven]['available']:
                oven_clocks[oven]['current_time'] += 1

# %%
def modify_supplies(current_time, supply_arrival_delay, quantities, counts, add_supplies=True):
    for ingredient in quantities.keys():
        if add_supplies:
            if current_time % supply_arrival_delay[ingredient] == 0:
                    counts[ingredient] += quantities[ingredient]
        else:
            counts[ingredient] -= quantities[ingredient]
            if counts[ingredient] < 0:
                counts[ingredient] = 0

# %%
counts = {'cakes': 0, 'eggs': 0, 'flour': 0, 'milk': 0}
counts_df = pd.DataFrame(counts, index=[0])

total_time = abs(time_to_minutes('4:00AM') - time_to_minutes('8:00PM'))
supply_arrival_delay = {'eggs': 60, 'flour': 120, 'milk': 45}
supply_quantities = {'eggs': 30, 'flour': 1000, 'milk': 500}
cake_requirements = {'eggs': 2, 'flour': 200, 'milk': 150}

oven_clocks = {
               'oven_1': {'bake_time':17, 'current_time':0, 'available': True, 'start_time': 0},
               'oven_2': {'bake_time':30, 'current_time':0, 'available': True, 'start_time': 0},
               'oven_3': {'bake_time':45, 'current_time':0, 'available': True, 'start_time': 0},
              }

# Loop through each minute in the 16 hours (960 min)
for i, current_time in enumerate(range(0, total_time)):

    if i != 0:
        modify_supplies(current_time, supply_arrival_delay, supply_quantities, counts, add_supplies=True)
    bake_cake(current_time, counts, cake_requirements, total_time, oven_clocks)
    
    if current_time % 1 == 0:
        counts_df = pd.concat([counts_df, pd.DataFrame(counts, index=[0])], ignore_index=True)


# %%
fig, axs = plt.subplots(2, 2, figsize=(8, 8))

# Histogram for 'cakes'
sns.histplot(counts_df['cakes'], kde=True, ax=axs[0, 0])
axs[0, 0].set_title('Cakes')

# Histogram for 'flour'
sns.histplot(counts_df['flour'], kde=True, ax=axs[0, 1])
axs[0, 1].set_title('Flour')


# Histogram for 'milk'
sns.histplot(counts_df['milk'], kde=True, ax=axs[1, 0])
axs[1, 0].set_title('Milk')

# Histogram for 'eggs'
sns.histplot(counts_df['eggs'], kde=True, ax=axs[1, 1])
axs[1, 1].set_title('Eggs')

# Display the plot
plt.tight_layout()
plt.show()


# %%
sns.set_style("darkgrid")
fig, axs = plt.subplots(2, 2, figsize=(8, 8))
    
    
# Plot for 'cakes'
axs[0, 0].plot(counts_df['cakes'])
axs[0, 0].set_title('Cakes')
axs[0, 0].set_xlabel('Time in minutes')
axs[0, 0].set_ylabel('Cake count')

# Plot for 'flour'
axs[0, 1].plot(counts_df['flour'])
axs[0, 1].set_title('Flour')
axs[0, 1].set_xlabel('Time in minutes')
axs[0, 1].set_ylabel('Flour count')

# Plot for 'milk'
axs[1, 0].plot(counts_df['milk'])
axs[1, 0].set_title('Milk')
axs[1, 0].set_xlabel('Time in minutes')
axs[1, 0].set_ylabel('Milk count')

# Plot for 'eggs'
axs[1, 1].plot(counts_df['eggs'])
axs[1, 1].set_title('Eggs')
axs[1, 1].set_xlabel('Time in minutes')
axs[1, 1].set_ylabel('Eggs count')

# Display the plot
plt.tight_layout()
plt.show()



