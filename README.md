# 🐦 Bird-Species-Observation-Analysis

**Domain**: 🌿 *Environmental Studies, Biodiversity Conservation, and Ecology*

This project focuses on analyzing bird observation data across various administrative units and habitat types. It includes data cleaning, exploratory analysis, and visual insights to support ecological understanding and conservation planning.

---

## ❓ Problem Statement

The project aims to analyze the distribution and diversity of bird species in two distinct ecosystems: **forests** and **grasslands**. By examining bird species observations across these habitats, the goal is to understand how environmental factors—such as vegetation type, climate, and terrain—influence bird populations and behavior.

This study leverages observational data to:
- Identify patterns of **habitat preference**
- Assess the **impact of ecosystems** on bird diversity
- Provide insights into **avian ecology and behavior**

The findings aim to support **habitat conservation**, **biodiversity management**, and address the effects of **environmental changes** on bird communities.

---

## 💼 Business Use Cases

1. 🦉 **Wildlife Conservation**  
   Inform decisions on protecting critical bird habitats and enhancing biodiversity conservation efforts.

2. 🌱 **Land Management**  
   Optimize land use and habitat restoration strategies by understanding bird species' habitat preferences.

3. 🧭 **Eco-Tourism**  
   Identify bird-rich areas for developing bird-watching tourism, attracting eco-tourists and boosting local economies.

4. 🌾 **Sustainable Agriculture**  
   Guide the development of farming practices that minimize negative impacts on bird populations in grasslands and forests.

5. 🏛️ **Policy Support**  
   Provide data-driven insights to help environmental agencies craft effective conservation policies for vulnerable bird species.

6. 📈 **Biodiversity Monitoring**  
   Track the health and diversity of bird populations to monitor overall ecosystem stability and detect early signs of ecological imbalance.

---

## 🔍 1️⃣ Data Cleaning and Preprocessing

- 🧹 Handle missing data and standardize observational metrics.
- 📊 Filter relevant columns for analysis (e.g., species, environmental factors, temporal data).
- 🔄 Consolidate data from forest and grassland units into comparable formats.

---

## 📈 2️⃣ Exploratory Data Analysis (EDA)

- 🗺️ Analyze species distribution across administrative units and habitat types.
- 📅 Study observation frequency by year, month, and season.
- 🌡️ Investigate relationships between environmental conditions (e.g., temperature, humidity) and bird activity.

---

## 📊 3️⃣ Types of Analysis – Examples

### 🕒 3.1 Temporal Analysis

- 📆 **Seasonal Trends**: Analyze the `Date` and `Year` columns for seasonal or annual patterns in sightings.
- ⏰ **Observation Time**: Review `Start_Time` and `End_Time` for peak bird activity periods.

### 📍 3.2 Spatial Analysis

- 🗺️ **Location Insights**: Group by `Location_Type` (e.g., Grassland) to locate biodiversity hotspots.
- 📌 **Plot-Level Analysis**: Compare `Plot_Name` data to identify high-activity plots.

### 🐤 3.3 Species Analysis

- 🌿 **Diversity Metrics**: Count unique species (`Scientific_Name`) by location type.
- 🎶 **Activity Patterns**: Use `Interval_Length` and `ID_Method` to analyze behavior types (e.g., Singing).
- ⚖️ **Sex Ratio**: Examine the `Sex` column for gender distribution by species.

### 🌦️ 3.4 Environmental Conditions

- 🌡️ **Weather Correlation**: Analyze how `Temperature`, `Humidity`, `Sky`, and `Wind` affect sightings.
- 🚨 **Disturbance Effect**: Evaluate how various `Disturbance` levels influence bird observations.

### 📏 3.5 Distance and Behavior

- 📐 **Distance Analysis**: Use the `Distance` column to assess proximity trends by species.
- ✈️ **Flyover Frequency**: Track `Flyover_Observed` to detect behavioral patterns.

### 👤 3.6 Observer Trends

- 👀 **Observer Bias**: Review observation patterns by `Observer` to check for individual reporting trends.
- 🔁 **Visit Patterns**: Use the `Visit` column to study effects of repeat visits on species count/diversity.

### 🛡️ 3.7 Conservation Insights

- 📋 **Watchlist Trends**: Track species with `PIF_Watchlist_Status` or `Regional_Stewardship_Status`.
- 🔢 **AOU Code Patterns**: Study `AOU_Code` distributions to align with conservation priorities.

---

## 📊 4️⃣ Visualization
- 📍 Create interactive visuals using **Plotly**, **Streamlit**, or **Power BI**.
- 📉 Dynamic scatter plots and bar charts for species distribution.
- 🔥 Temporal heatmaps by year and month.
- 🌍 Geographic maps (if location data available) for activity zones.
- 🔎 Species/environment-specific filters for deep-dive insights.

---

## 💡 5️⃣ Additional Insights

- 🗺️ Identify high-activity regions and peak seasons for specific species.
- 🧠 Understand environmental influence on bird behavior.
- 🚨 Highlight at-risk species for targeted conservation efforts.

---

## 🧰 Skills & Technologies

### 🖥️ Programming & Tools
- **Languages:** Python  
- **Libraries:** `pandas`, `matplotlib`, `plotly` ,  
- **Databases:** PostgreSQL, MySQL  
- **BI Tools:** Power BI

### 🔧 Data Science Skills
- 🧹 **Data Cleaning**
- 🔄 **Data Preprocessing**
- 📊 **Exploratory Data Analysis (EDA)**
- 📈 **Data Visualization** (Matplotlib, Plotly, Power BI)

---

## ✨ Demo & Usage
      1. Fetched the Uncleaned DataSet (in the xlsx format) and performing the data cleaning.
		2. Execute Forest_Data_Cleaning.ipynb,Grassland_Data_Cleaning.ipynb [UnCleaned_Forest_DataSet.csv,UnCleaned_Grassland_DataSet.csv] and after data cleaning saved the csv files as Cleaned_Forest_DataSet.csv , Cleaned_Grassland_DataSet.csv
      3. Execute EDA files Forest_EDA.ipynb, Grassland_EDA.ipynb
		4. Combined the Forest + Land [Execute this file Forest_Grassland_EDA.ipynb]. Cleaning the excel files [Combined_UnCleanDataSet.csv -> Cleaned_Combined_DataSet.csv -> EDA_Combined_DataSet.csv]
		5. Execute the above files in any IDE(VisualStudioCode) and for database for local use postgresql or for cloud use cloud streamlit
      6. If using cloud, change the environment to cloud in config.json. IF using local database, then change the environment to local
      7. Added the passwords in the password.toml folder (for local DB)
                     Inside secrets.toml/password.toml:
                         host = "localhost"
                         user = "youruser"
                         password = "yourpassword"
                         database = "yourdbname"
                         port = "5432"
	   8. In db_utils.py: It has a Function to connect to the database
		9. In SQL\config_secrets.py: Loading the environment details and Load secrets from your custom toml file
		10.In SQL\db_setup.py: Setting up the birdspecies database
		11. Execute the files in the order of:
		           Forest_Data_Cleaning.ipynb,Grassland_Data_Cleaning.ipynb
				   Forest_EDA.ipynb, Grassland_EDA.ipynb,Forest_Grassland_EDA.ipynb
				   Forest_Sql.ipynb,Grassland_Sql.ipynb,Forest_Grassland_combined_Sql.ipynb
		12. I have zipped [Forest_Sql.ipynb,Grassland_Sql.ipynb,Forest_Grassland_combined_Sql.ipynb] these 3 files in sql.7z

##  PowerBi Report
https://app.powerbi.com/view?r=eyJrIjoiNzE4MDUwYzMtNTc5NS00NjA2LWFkYzYtNWE3NmEwYTFhNTk5IiwidCI6IjczY2UwZTg5LWRjMzUtNGExMC04NTMxLTFjYzJmMTgxNTUyZCJ9&embedImagePlaceholder=true
