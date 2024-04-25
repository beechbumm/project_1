# Project_1

Group Members: Owen Wang, Nathanael Whipple, Rudi Espinoza, Aaron Pen-Kruger, and Addie Dehmlow

Welcome to our very first project!  This was a culmination of everything we have learned so far.  It was really fulfilling to see all of the skills we had learned come together; it was also fairly obvious that our skills developed more while we were getting it done.

We started by reading a csv file that we obtained from Census.gov containing population statistics for each year from 2020-2023.  From here we were able to make calculations and add to the data table.  We pulled the top 100 counties by population growth numbers, as well as another 100 counties by population growth percentage and merged them using an outer merge, then dropped the duplicates, creating about 164 counties that would be our starting point for comparing data.  We pulled the latitude and longitude details by utilizing the geoapify API, and mapped them out as well.

We noticed there were some discrepancies in the latitude and longitude for some of the counties because we mapped them out, so we added code to make those corrections.

From Census.gov, we were able to pull in Median Household Income for all US counties.  Utilizing a left merge, we were able to add to our table the information for the counties we were interested in.  

We practiced making scatter plots to see if there was any correlation between several factors, like the population growth numbers and percentages, as well as the population growth numbers and median household income, but we saw little to no correlation in these.  

After we had our dataframe started, we began formulating the meat of our project, how we were going to determine the best county to invest in.  We decided to choose several factors, including Mortgage advantage, Poverty, Affordability, and Demand, as ways to calculate this.  Some of these ideas came about because we consulted a real estate agent to see what factors they looked for when buying or selling a home. 

The Mortgage advantage we calculated by finding the average mortgage and the average rent for each county, then subtracting them to see how much more expensive renting was in each county.  For the poverty statistic, we explored figuring out how to use the Census API.  This was very fulfilling when we got it to work.  One challenge we had was that the Census API provided the county name and state in separate columns, and the state was provided in abbreviated form.  We figured out a way to easily convert the state abbreviations for all of the rows using dictionaries and concatenated the columns to match our other data. Affordability was calculated by taking the median household income, and dividing it by the median home prices, which we had obtained from HUD.  Finally, our Demand ratio was calculated by taking the population growth in numbers and dividing it by the total number of homes built after 2020, which was also located in the US Census data.

We utilized the Pandas binning ability to separate and apply a score to each statistic, then adding the scores together we had a winner.

Rockwall County, Texas, had the highest overall score.  It was really interesting to see that the top counties all passed our gut-check, these were all areas near busy cities that would have a lot of job availability.  We checked the weather in Rockwall County, Texas using the OpenWeather API just for fun, and it gave us a description of clear skies.  

Overall, we really enjoyed working on this project. We feel a lot more comfortable using the skills that we've learned so far! We also took some time to learn new skills, like how to make our tables colorful, using gradients to show how large or small the values were.

Please see in this repository our analysis.docx for a more detailed analysis.

Thank you for looking at our project!