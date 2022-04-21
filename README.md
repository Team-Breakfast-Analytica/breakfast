## University of Michigan SIADS 697 Capstone Project
# Seattle Airbnb Advisory Dashboard 
by Team Breakfast Analytica: Kristina Garber (kgarb), Benjamin Bartek (bbartek), Jono O'Dowd (jodowd)

## Introduction:
Kristina Garber, Benjamin Bartek & Jono O'Dowd formed a team called TEAM BREAKFAST ANALYTICA to create a Seattle Airbnb Advisory Dashboard for our University of Michigan SIADS 697 Capstone class project. We utilized various data science techniques and tools to accomplish our goals. We started with qualitative research to determine all the possibilities related to available data sets and potential questions that might be helpful to those using our dashboard. Our resulting research inspired us to build an advisory dashboard for future Seattle Airbnb hosts and customers. For hosts, it is a tool to determine best location to startup an Airbnb in Seattle. For customers, it is a tool to determine best location to stay at an Airbnb in Seattle. The data sets would be a combination of Airbnb, crime, recreational, and nearby shopping data. The analyzed data would give guidance on picking the best area to startup an Airbnb based on good profit margins, lower crime, proximity to nearby recreational activities and shopping. All of our gathered data went through rigorous cleansing, wrangling and standardization. The data sets were joined as needed and visual exploration was done to help understand how it should be structured for the model phase. Both unsupervised and supervised learning models were used. A real insightful unsupervised model, K-Means Clustering was used to discover and segment neighborhoods according to clusters with similar patterns. For example, this clustering model segmented neighborhoods into clusters of lowest crime, medium crime, high crime, and highest crime. The clustering also helped to determine neighborhood clusters with the greatest amount of choices of nearby recreational activities and shopping and those neighborhoods where pricing could be advantageous to those starting up an Airbnb and likewise potential customers looking for the best deal. Supervised models such as linear regression and Meta's Prophet provided insight of continuous variables and forecasting. Natural Language Processing was utilized to discover the top key words that describe the neighborhoods where the Airbnbs reside.  Using data science techniques, a story about the data becomes evident. There are a number of ways to tell this story; however, we decided to present our findings using a visual tool called Tableau. Prior to Tableau, the data had to go through rigorous preparation. The preliminary tools that helped us get there were CoCalc, Heroku, and pgAdmin 4. CoCalc provided a repository and workspace for collaboration. With this tool, we created our Jupyter notebooks to interact with the data by importing all the necessary python libraries and models.  Python code then cleansed and prepared the data for processing by our chosen machine learning models. Next, the python code using python libraries called sqlalchemy and psycogpg2 exported the output to our newly created Heroku PostgreSQL database.  Through the pgAdmin 4 tool, we could access and view the values stored in the tables. Finally, from Tableau, we were able to import this processed data from the PostgreSQL database into our Tableau tables. At this point, we could carefully arrange the data into a story in our final informative dashboard.

## A look at the final product: 
[Link to Seattle Airbnb Crime Advisory](https://breakfastanalytica.wixsite.com/breakfast/html) 


## Step by step instructions:

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
 4. 

