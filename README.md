# titanic_visualization
data visualization in d3


## Dataset


The used Dataset: https://docs.google.com/document/d/1w7KhqotVi5eoKE3I_AZHbsxdr-NmcWsLTIiZrpxWx4w/pub?embedded=true

Description of the Dataset: https://www.kaggle.com/c/titanic

The dataset (titanic_data.csv) is already in a tidy format. However, for ease of presentation, it was still cleaned and put in a shape where visualization can easily take place. The cleaning was done using a Python script clean_transform.py.

Two .csv data files were generated from the cleaning and reshaping process: Titanic.csv and titanic_compound.csv. Both files contain 892 data points (same as the original data set), but have shaped the features in a different ways that allowed for easy presentation in d3.

The cleaned data set, titanic.csv, has the following features:

* Passenger Class: Class of the Titanic Passengers. Possible Classes: 1,2,3. 1 is the most expensive, 3 is the least expensive.
* Outcome: Survival outcome of the Passenger: Survived or Perished
* Sex: female or male
* Age: Child (<12), Youth (12-29), Adult (30-49), Senior (Age > 50), and Unknown
* Embarked: Port of Embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)

Note that all of the features are categorical after processing. Note that even though age is a numerical, continous variable, I have transformed and binned this variable into a categorical variable. The motivation is that there is not so much difference between age 12 and 16 in this analysis, but there is a difference between 12 and 50. For this reason, I have buckedted Age into bins listed above for comparison.

## Summary

I analyzed the survivorship by passenger class, by sex, by age, and by embarked port. The analysis start by analyzing the count of survivors by these variables, then I analyed the survivorship probability by these variables. 

The count analysis is illuminating, however, the survivorship probability is even more so - this is because the relationship between survivor by count is often different from survivorship by percentage. 

In addition, I have constructed a compound features from passenger class, sex, and age. Then I showed the survivor by counts based on the new, constructed features, as well as the survivorship probability. This step is important since it shows the marginal probability, however, examining conditional probability might be more interesing and may shed more light on the passenger's survival outcome on the Titanic. 


## Design

As a data visualiation choice, I have chosen the bar plot design in general, given the categorial nature of the features. A bar chart is used since comparing a distance on a straight line can be interpreted by human eye with the greated amount of ease and accuracy.

I used stacked Bar Charts for this Data Visualization. It allows to represent different groups in one stacked bar and allow for quick comparison. Additionally, data labels were added inside each of the stacked bars. For example, the values of 136 and 80 inside the first stacked bar chart represent 136 survivors and 80 deceased from Class 1 passengers. 

Survivors are shown in a light blue, while deceased are shown in a light red for easy contrast. The color choice was consistent with the normal interpretation of red being associated with warnings. A low value of saturation was used to tone down the sharp color for easy reading. 

Related infromation is also displayed in the page when a mouse hovers over the relevant portion of the stacked bar. In addition, legends are displayed at the top right corner.


## Feedback

#### First version of index.html

* Visualization may benefit from adding more body (description) to the charts
* Only marginal probability was shown - suggested showing conditional probability for intelligent comparison
* Label text for graph 5 and 6 are cut off

#### Second version of index.html

* Consider set up buttons to interactively show graphs based on counts or percentage - reduce length of page


## Resources
    

https://en.support.wordpress.com/markdown-quick-reference/

https://github.com/michaelstrobl/Project-5-Data-Visualization-with-D3-JS

https://bl.ocks.org/bmokk/0c7c97e9e52fc9acf3fb260166b56cb0

http://dimplejs.org/examples_index.html