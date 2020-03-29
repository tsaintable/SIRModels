# Epidemic Models

Compartmental modeling has been a subject of interest since the early 1900s. Among the ﬁrst to mathematically model the spread of epidemics in the early twentieth century were William Hamer and Ronald Ross. They achieved this by using the law of mass action by which they explained the epidemic behavior of disease. In the study of epidemiology, compartmental models are used to predict how infectious diseases spread throughout a population.

# The Compartmental Models
To simplify such a model, the members of a population are compartmentalized into various diﬀerent groups–in the case of SIR, the groups are susceptible, infected and removed/recovered.

# Variations
Although the SIR model is the most studied, there are other models which are variations of the SIR, including but not limited to the SIS, MSIR and SEIR models. There are beneﬁts of the SIR model for many; pharmaceutical companies are impacted by SIR and other related models for they approximate the amount of people who will become infected, allowing the companies to make a proﬁt when selling the antibiotics and also down the road producing and proﬁting oﬀ of a vaccination, along with insurance companies.

# Practicalities
The models allow the companies to see how much they would have to pay out to families, from medical bills to life insurance policies. Giving the insurance companies a good idea of what they should make their premiums and who they should insure. In summation, using compartmental models to simulate epidemics is just as useful for saving lives as it is for making a proﬁt.

# The SIR Model
* Because we are modeling the change of three variables over time, which are each derived from both their own values and the values of the other two variables, we are left with three diﬀerentiable equations that will be analyzed through a numerical approach.
* In these equations we denote the number of susceptible individuals by “S(t)”, infected, which is denoted with an “I(t)”, and removed/recovered, which are denoted with an “R(t)” and are immune from further infection.
* Importantly, in order to understand the relationship between these variables, we must understand that a susceptible individual may only move from the susceptible group to the infected group. From here, the infected group may only move to the removed group. This means that the change in susceptible individuals over time must be based entirely on the negative change in the number of infected individuals. This is phenomenon is displayed in the equations below.
* The number of infected individuals, on the other hand, would grow with the number of susceptible individuals, which would then lose members to the removed category. Lastly, the removed category will grow in some relationship with the number of infected individuals. These relationships are shown below:
<p align="center">
<img src="https://tex.cheminfo.org/?tex=%5Cbegin%7Baligned%7D%0A%5Cfrac%7BdS%7D%7Bdt%7D%20%26%3D%20-%5Calpha%20SI%5C%5C%0A%5Cfrac%7BdI%7D%7Bdt%7D%20%26%3D%20%5Calpha%20SI%20-%20%5Cbeta%20I%5C%5C%0A%5Cfrac%7BdR%7D%7Bdt%7D%20%26%3D%5Cbeta%20I%5C%5C%0A%5Cend%7Baligned%7D%0A"/>
</p>

Logically, it also makes sense that the combined change must equal 0, as the population does not change throughout the model (excluding deceased members of the population, which are labeled as removed and categorized under the "$R(t)$" variable). This overarching relationship is shown below:

<img src="https://tex.cheminfo.org/?tex=%5Cbegin%7Baligned%7D%0A%26%5Cdfrac%7BdS%7D%7Bdt%7D%2B%5Cdfrac%7BdI%7D%7Bdt%7D%2B%5Cdfrac%7BdR%7D%7Bdt%7D%3D0%0A%5Cend%7Baligned%7D%0A"/>
