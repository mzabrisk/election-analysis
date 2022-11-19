# Election Analysis

## Overview of Election Audit

The Colorado Board of Elections has reached out for help conducting an election audit. They have provided us with a .csv file containing several pieces of information: a Ballot ID, County in which the vote was cast, and the Candidate selected on the ballot. Using Python, and the provided .csv file, they have asked us to analyze the data and provide the following information:

 - Total votes cast.
 - A complete list of counties with votes cast, including the number of votes cast in each county and the percent of the total vote cast in the county.
 - A complete list of candidates receiving votes in the election, including the number of votes they received and the percent of the total vote.
- The identity of the winner.

## Election-Audit Results

- There were a total of 369,711 votes cast in the election
- County vote breakdown:
    -  **Jefferson:** **38,855 votes** were cast in Jefferson County, for **10.5%** of the total vote.
    - **Denver:** **306,055 votes** were cast in Denver County, for **82.8%** of the total vote.
    - **Arapahoe:** **24,801 votes** were cast in Arapahoe County, for **6.7%** of the total vote.
- The most votes were cast in **Denver County**. with 306,055 votes
- Candidate vote breakdown:
    - **Stockham:** **85,213 votes** were case for Charles Casper Stockham, for **23.0%** of the total vote.
    - **DeGette:** **272,892 votes** were case for Diana DeGette, for **73.8%** of the total votes.
    - **Doane:** **11,606 votes** were case for Raymon Anthony Doane, for **3.1%** of the total vote.
- The winning candidate was Diana DeGette, who recived **272,892 votes** for **73.8%** of the total vote.

## Election-Audit Summary

This code works well for analyzing the results of a popular-vote election at the state level. However, in order for it to perform well for elections with an additional layer, such as a national election, an additional layer needs to be accounted for. In this analyis, we account for county votes and total votes. In order to move up to the national level, we would need to keep track of electoral district (analagous to county), state (analagous to total), and national votes. Additionally, our analysis only kept track of the total voting results, but results at all levels need to be tracked. To accomplish this, a couple of changes need to be made to the code.

- The following changes to the main *for* loop enable detailed vote tracking at the county level, while still maintaining the ability to easily output the overal outcome:

![](https://github.com/mzabrisk/election-analysis/blob/2cbdaea5bd233a05aa0b2c103220ab2144b7352c/Resources/revised_code.png)

As currently written, provides the following output:
![](https://github.com/mzabrisk/election-analysis/blob/2cbdaea5bd233a05aa0b2c103220ab2144b7352c/Resources/revised_output.png)


- In order to organize the code to work at the national level, an extra layer needs to be added, which would result in a nested dictionary similarly organized to this:



Of course, to work in US elections as they are currently designed 

