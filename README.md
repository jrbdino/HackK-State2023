# Tai Your Life Together
### HackK-State2023
 
## Inspiration
We wanted to make a web application that sorts homework and assignments for classes easily.

## What it does
Our web application uses .csv files to import lists of homework assignments and their due dates, perceived difficulty, and grade weighting.  It then sort ands optimizes the order you should complete the assignments in using a linear regression algorithm.

## How we built it
We made our it web application using Python 3.9, Taipy 3.0.0, pandas, and CSS.

## Challenges we ran into
None of us had ever used Taipy previously, so learning it and using it to implement our project was difficult.  We ran into some issues with our tables not refreshing via Taipy.  We originally wanted to pull homework assignment objects down directly from the Canvas REST API, but we weren't able to get OAuth tokens.

## Accomplishments that we're proud of
We are proud that we learned how to use Taipy and were able to complete our project.

## What we learned
We learned how to use Taipy and became better with pandas dataframes.

## What's next for Tai Your Life Together
Hopefully in the future we will be able to pull the upcoming assignments directly from the API and automatically refresh the queue.