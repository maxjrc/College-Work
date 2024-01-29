import datetime
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Task4.csv')


# Main Menu for choice selection
def mainmenu():
  print("\t\t****Welcome to the Dashboard****")
  print('1) Return all current data')
  print('2) Return data for a specific region')
  print('3) Return data for a specific house type')
  print("4) Returns the highest region increase")
  return int(input(" "))


# Prints all the data in the csv file
def alldata():
  print(df)


# Returns data given a specific type of property
def specific_property_type(property_type):
  specific_type = df[df['Property Type'] == property_type]
  print(specific_type)


# This function calculates and visualizes the region with the highest overall increase in property value

def find_region_highest_increase():
    # Calculate the percentage change in property value for each region
    region_increase = df.iloc[:, 4:].pct_change(axis=1).sum()

    # Find the region with the highest overall increase in property value
    max_increase_region = region_increase.idxmax()

    # Print the region with the highest overall increase
    print("Region with the highest overall increase in property value:",
          max_increase_region)

    # Calculate the average increase in property value for each region
    region_avg_increase = df.iloc[:, 4:].pct_change(axis=1).mean()

    # Plot a line graph to visualize the average increase in property value for each region
    plt.plot(region_avg_increase.index, region_avg_increase.values)
    plt.title('Average increase in property value for each region')
    plt.xlabel('Region')
    plt.ylabel('Average increase')
    plt.xticks(rotation=45)  # Rotate x-axis labels for readability
    plt.show()



# Checks the region
def region_check(region, startdate, enddate):  # region, startdate, enddate

  df1 = df.loc[:, startdate:enddate]
  df2 = df.loc[:, 'Region Code':'Rooms']

  result = pd.concat([df2, df1], axis=1,
                     join='inner').where(df2["Region"] == region)
  result = pd.DataFrame(result)
  result.dropna(inplace=True)
  print(result)
  ave = df1.mean()
  ave.plot()
  plt.show()
  return result


# Runs our options
x = mainmenu()
while x == 1 or x == 2 or x == 3 or x == 4:
  if x == 1:
    alldata()

  elif x == 2:
    while True:
      print()
      # Region Checker
      region = input(
          "Please enter the name of the region you would like to check: ")
      region = region.capitalize()
      if region in df.Region.values:
        while True:
          startdate = input(
              "PLEASE ENTER A START DATE AS MONTH-YEAR e.g. JAN-20 ")
          startdate = startdate.capitalize()
          if startdate not in df.columns:
            print("Error start date not found")
          else:
            while True:
              enddate = input(
                  "PLEASE ENTER AN END DATE AS MONTH-YEAR e.g. JAN-20 ")
              enddate = enddate.capitalize()
              if enddate not in df.columns:
                print("Error end date not found")
              else:
                region_check(region, startdate, enddate)
                break
            break
        break
      else:
        print("Region not found")
  elif x == 3:
    property_type = input("Please enter a property type: ")
    specific_property_type(property_type)
  elif x == 4:
    find_region_highest_increase()
  x = mainmenu()
