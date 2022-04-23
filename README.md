## University of Michigan SIADS 697 Capstone Project
# Seattle Airbnb Advisory Dashboard 
by Team Breakfast Analytica: Kristina Garber (kgarb), Benjamin Bartek (bbartek), Jono O'Dowd (jodowd)

## Table of Contents
* [Introduction](#introduction)
* [Objective](#objective)
* [Data Sets](#data-sets)
* [Data Science Methodology](#data-science-methodology)
* [Final Product](#final-product)
* [Instructions](#instructions)


## Introduction
Kristina Garber, Benjamin Bartek & Jono O'Dowd formed a team called TEAM BREAKFAST ANALYTICA to create a Seattle Airbnb Advisory Dashboard for our University of Michigan SIADS 697 Capstone class project. We utilized various data science techniques and tools to accomplish our goals. We started with qualitative research to determine all the possibilities related to available data sets and potential questions helpful to those using our dashboard. Our resulting research inspired us to build an advisory dashboard for future Seattle Airbnb hosts and customers. For hosts, it is a tool to determine best location to startup an Airbnb in Seattle. For customers, it is a tool to determine best location to stay at an Airbnb in Seattle. The data sets would be a combination of Airbnb, crime, and nearby recreational data. The analyzed data would provide insight on picking the best area to startup an Airbnb based on good profit margins, lower crime, and proximity to nearby recreational activities. 



## Objective
Our intent was to create a dashboard using data science tools and techniques to help future Seattle Airbnb hosts and customers make informative decisions on the best neighborhoods for an Airbnb startup or Airbnb stay. The structure of raw data sets was by neighborhood, and so we decided to base our visuals on a comparative analysis of the Seattle neighborhoods. We limited our scope to three informative areas: Seattle Airbnb neighborhood housing income vs costs, Seattle crime levels by neighborhood, and Seattle recreational facilities proximity to neighborhoods.

## Data Sets
The data sets would be a combination of Airbnb, crime, recreational, and nearby shopping data. The analyzed data would give guidance on picking the best area to startup an Airbnb based on good profit margins, lower crime, proximity to nearby recreational activities and shopping. All of our gathered data went through rigorous cleansing, wrangling and standardization. The data sets were joined as needed and visual exploration was done to help understand how it should be structured for the model phase. Click on links below to explore:
* [Inside Airbnb: Get the Data(Seattle Airbnb data)](http://insideairbnb.com/get-the-data/)
* [SPD Crime Data: 2008-Present | City of Seattle Open Data portal (Seattle Crime Data)](https://data.seattle.gov/Public-Safety/SPD-Crime-Data-2008-Present/tazs-3rd5/data)
* [Seattle - Google Maps (Seattle Recreational Coordinates data)](https://www.google.com/maps/place/Seattle,+WA/@47.6129428,-122.4824927,11z/data=!3m1!4b1!4m5!3m4!1s0x5490102c93e83355:0x102565466944d59a!8m2!3d47.6062095!4d-122.3320708)

## Data Science Methodology
Both unsupervised and supervised learning models were used. A real insightful unsupervised model, K-Means Clustering was used to discover and segment neighborhoods according to clusters with similar patterns. For example, this clustering model segmented neighborhoods into clusters of lowest crime, medium crime, high crime, and highest crime. The clustering also helped to determine neighborhood clusters with the greatest amount of choices of nearby recreational activities and shopping and those neighborhoods where pricing could be advantageous to those starting up an Airbnb and likewise potential customers looking for the best deal. Supervised models such as linear regression and Meta's Prophet provided insight of continuous variables and forecasting. Natural Language Processing was utilized to discover the top key words that describe the neighborhoods where the Airbnbs reside.  Using data science techniques, a story about the data becomes evident. There are a number of ways to tell this story; however, we decided to present our findings using a visual tool called Tableau. Prior to Tableau, the data had to go through rigorous preparation. The preliminary tools that helped us get there were CoCalc, Heroku, and pgAdmin 4. CoCalc provided a repository and workspace for collaboration. With this tool, we created our Jupyter notebooks to interact with the data by importing all the necessary python libraries and models.  Python code then cleansed and prepared the data for processing by our chosen machine learning models. Next, the python code using python libraries called sqlalchemy and psycogpg2 exported the output to our newly created Heroku PostgreSQL database.  Through the pgAdmin 4 tool, we could access and view the values stored in the tables. Finally, from Tableau, we were able to import this processed data from the PostgreSQL database into our Tableau tables. At this point, we could carefully arrange the data into a story in our final informative dashboard.

## Final Product: 
[Link to Seattle Airbnb Crime Advisory](https://public.tableau.com/views/Seattle_Airbnb_Advisory_Dashboard/Story-All?:language=en-US&:display_count=n&:origin=viz_share_link) 

## Instructions:

1. Install a Jupyter Notebook to run our ipynb files. If you are new to Jupyter notebooks, click on this [Link to Jupyter Notebook Beginner Guide](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/execute.html)
2. There are three main areas of our code (see below). You may choose to work on one, two or all three.
    * Neighborhood Airbnb Profit Margin & Keywords Dashboard Analysis (ipynb files found inside folder 'notebooks' sub-folder 'Profit')
    * Neighborhood Airbnb Crime Dashboard Analysis (ipynb files found inside folder 'notebooks' sub-folder 'Crime')
    * Neighborhood Airbnb with Nearby Recreational, Restaurants & Shopping Analysis (ipynb files inside folder 'notebooks' sub-folder 'POI' for Points of Interest)
    * Optional: You are welcome to access our notebooks and data files from our CoCalc repository public view: [Link to Seattle Airbnb Crime Advisory: Datasets & Jupyter Notebooks](https://cocalc.com/share/public_paths/9f5e4e91cd5e0842e82c32209ca40da9b7e1b24f)   
3. After choosing which notebook files to run, you will also need the following tools:
    * Heroku - to build a PostgreSQL database and connect Jupyter notebooks via python libraries called sqlalchemy and psycogpg2.
    * pgAdmin 4 tool - to access your new PostgreSQL database to ensure the data exported properly from the Jupyter notebook files.
    * Tableau - to connect to the PostgreSQL database and begin building your visual story using Tableau's worksheet & dashboard features.
4. Summary of steps:
    * You must do the preliminary step of setting up Heroku PostgreSQL database first. Then include PostgreSQL credentials in designated Jupyter Notebook cell with sqlalchemy and psycogpg2 python libraries that act as connectors to the PostgreSQL database.
    * Ensure the respective csv file data sets are in local folder where the Jupyter notebooks exist.
    * Run the Jupyter Notebooks against the respective csv file data sets.
    * Use pgAdmin 4 tool to check on the post-model results to ensure it made it to the PostgreSQL database.
    * Using Tableau, set up connectors to the PostgreSQL database using your PostgreSQL credentials from your Heroku account.
    * Within Tableau, create any necessary database joins and set up either an ‘Extract’ or ‘Live’ connector to the PostgreSQL database depending on your strategy. We just used ‘Extract’ to update manually as necessary but if you are in a production-like environment, ‘Live’ may be the way to go.
    * Now begin your Tableau construction of telling the data story. Start with ‘Worksheet’ to manipulate and configure the data to particular visuals. Next move to ‘Dashboard’ where you can pull in one or more ‘Worksheets’ depending on your visual approach. Finally pull in all ‘Dashboards’ into what Tableau calls a ‘Story’ screen. This is where you can display all your dashboards into one screen where each dashboard can be accessed one at a time via a navigational tab menu structure. That is all there is to it. Well, we found this quite a challenge to get the final dashboard you now see at the link further above in this ReadMe. We are thankful to our guide, Michelle LeBlanc, who coached us along the way to go above and beyond anything we thought possible. Thank you, Michelle and our other instructors and co-students who gave helpful advice along the way. Go Blue!
