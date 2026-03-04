📊 End-to-End Sales Data ETL Pipeline & Analytics Dashboard <br><br>


🔷 Project Overview 

This project demonstrates an end-to-end sales data analysis workflow using Python, SQL, and Power BI.

Multiple Excel files stored across different folders were:

Programmatically scanned

Column names standardized using mapping logic

Cleaned and type-aligned

Loaded into SQL using automated loop-based processing

Merged into structured tables

Aggregated using SQL views

Connected to Power BI for KPI reporting and business analysis.<br><br>

This repository contains a demo-safe version of the automation pipeline.
Advanced business transformation logic has been modularized.<br><br>

🏗 Architecture Flow

Excel Files
→ Python ETL Automation
→ SQL Database
→ SQL Views
→ Power BI
→ Analytics Dashboard

📂 Project Structure

📸 (Screenshot 1 — Folder Structure)

![Folder Structure](screenshots/folder_structure.png)

Explanation below image:

The project is structured into data preparation, SQL analysis, and Power BI reporting layers to ensure separation of concerns and modular design.<br><br>

🔹 Column Mapping Logic

📸 (Screenshot 2 — Column Mapping)

![Column Mapping](screenshots/column_mapping.png)

Column names from multiple inconsistent Excel files were standardized using a mapping dictionary to ensure schema consistency before database loading.<br><br>


🔹 Data Cleaning & Type Alignment

📸 (Screenshot 3 — Data Cleaning)

![Data Cleaning](screenshots/data_cleaning.png)

Data cleaning steps included:

Handling missing values

Converting mixed data types

Removing invalid characters

Standardizing numeric fields

Ensuring date consistency <br><br>


🔹 Loop-Based SQL Loading

📸 (Screenshot 4 — Loop Based SQL Load)

![SQL Load Loop](screenshots/Loop-based_SQL_loading.png)

All Excel files were processed dynamically using a loop, enabling automated ingestion of multiple files without manual intervention.<br><br>


🔹 Console Execution Output

📸 (Screenshot 5 — Console Output)

![Console Output](screenshots/console_output.png)

The console output confirms successful processing and loading of multiple files into SQL. <br><br>


🗄 SQL Database Layer
🔹 Final Merged Table

📸 (Screenshot 6 — Final Table)

![Merged Table](screenshots/final_merged_table.png)

All cleaned datasets were merged into a centralized SQL table for analytical processing.<br><br>


🔹 SQL View (Business Aggregation)

📸 (Screenshot 7 — SQL View)

![SQL View](screenshots/sql_view.png)

A SQL view was created to:

Aggregate yearly sales

Compute profit metrics

Prepare structured data for BI consumption<br><br>


📊 Power BI Data Modeling
🔹 Data Model Relationship View

📸 (Screenshot 8 — Model View)

![Data Model](screenshots/Data_model_relationship_view.png)

A proper star schema approach was implemented using a continuous Date Table to handle missing months and enable time intelligence.<br><br>


🔹 DAX Measure Example

📸 (Screenshot 9 — DAX Measure)

![DAX Measure](screenshots/DAX_measure_example.png)

Key measures implemented:

Total Sales

Profit Margin

Year-over-Year Growth

Top N Analysis <br><br>


📈 Business Intelligence Dashboard
🔹 Full Dashboard

📸 (Screenshot 10 — Dashboard)

![Dashboard](screenshots/dashboard.png)

The dashboard provides an executive-level overview of business performance from 2012–2020.<br><br>


🔹 Combo Chart (Trend + Margin)

📸 (Screenshot 11 — Combo Chart)

![Combo Chart](screenshots/combo_chart.png)

A combo chart was used to visualize:

Monthly Sales (Column)

Profit Margin Trend (Line)<br><br>


🔹 KPI Section

📸 (Screenshot 12 — KPI Section)

![KPI Section](screenshots/KPI_section.png)

KPIs displayed:

Total Sales

Total Profit

Profit Margin

Year-over-Year Growth <br><br>


📌 Key Business Insights

Sales peaked during the later years of the dataset.

Profit margin averaged approximately 68%.

Certain months showed zero recorded transactions.

Top 5 customers contributed significantly to total revenue. <br><br>


🛠 Tools & Technologies

Python (Pandas)

MySQL

Power BI

DAX

SQL Views

Data Modeling (Star Schema) <br><br>


🔎 Data Handling Note

Months with no recorded transactions were treated as zero sales using a continuous Date Table approach to ensure accurate trend visualization.<br><br>


🚀 Skills Demonstrated

Data Cleaning & Standardization

Schema Mapping

SQL Aggregation

Time Intelligence Modeling

KPI Development

Business Dashboard Design

End-to-End Data Workflow
