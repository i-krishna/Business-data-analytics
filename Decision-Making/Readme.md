# Tableau Storyboard

[View the interactive storyboard](https://public.tableau.com/views/TableauStoryboard_Final_V1/Storyboard?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link ) - explore the full storyboard on Tableau Public (in full-screen mode).

[Read the walkthrough](https://github.com/i-krishna/Business-Analytics/blob/main/Decision-Making/Tableau%20Project.pdf) — narrative documentation of the dashboards, design choices, and underlying analysis of above storyboard.

# Best Practices and Frameworks for Data Visualization
by Krishna Damarla - Wednesday, November 12, 2025, 7:11 PM

**Takeaways**

Choosing the right chart requires matching data characteristics to visual encoding methods, as charts should focus on fetching information from data and not on creating art. Charts should be chosen as per the data at hand to visualize and should emit only the information the audience needs to view. Although there are many charts, I will discuss the main ones, such as bar charts, which can track one or two variables effectively but fail when showing five or more variables or parts of a whole (Dougherty & Ilyankou, 2025). Line charts track multiple variables simultaneously without clutter and are used mainly for time-series data visualization. For cases where line charts fall short, such as visualizing more than 50 variables or handling datasets up to 1GB in browsers or desktop applications, Parallel Coordinates using WebGL GPU rendering with additive blending can be used.  Scatter plots identify correlations, trends, patterns, and outliers between variables. Area charts, particularly stacked versions, show how parts of a whole change over time. Heatmaps display density information effectively. Pie and doughnut charts excel at showing proportions within a single time period (365 Data Science, 2018).

Colors on top of charts guide the audience to where to focus and bring their immediate attention. Imagine a situation where I need to deliver a year-long research result in a 10-minute pitch to investors to get funding. I must be extremely concise and direct their attention to what really matters. Less text, more charts, essential colors. There are five strategic color usages as per Munzner (2021): sequential (gradients showing progression), diverging (two extremes with neutral midpoint), categorical (maximum four distinct colors), highlight (directing attention), and alert (signaling importance). Further, as per Schaffer's framework, it is advisable to use color sparingly and to avoid red-green combinations for a color-blind audience. Instead, use blue-orange alternatives. As color influences mood and behavior, use blue to convey trust and orange to communicate friendliness (Krause, 2014). Also, test RGB screen colors with CMYK print. 

**Applications**

Before designing my dashboards that track patients' information across U.S. states, I plan to apply Subotin's (n.d.) four questions: Who is this for? Where will the viewers view it (desktop or mobile)? Why am I creating this? What data matters to viewers?

For any chart I build where applicable, I make sure it comprises 10 essential elements discussed in Storytelling with Data (2021), such as axis lines, axis labels, axis titles, graph titles, data lines, data markers, data labels, reference lines, legends, and annotations. Further, I would make my charts interactive and user-friendly while answering the five questions I stated as my business problem. I will use my cleaned dataset from Week 3, which already eliminated cluttered variables not essential for answering my questions or creating appropriate charts. In this project, I am planning to use line charts for predicting future events from historical time-series data, horizontal bar charts for data with comparisons, stacked bar charts for revealing peaks within data, scatter plots for identifying correlations between variables and maps for geographical density information.

Although Tableau Public and certain enterprise BI tools do not offer advanced interactive visualization features such as linking and brushing or zoom and pan on high-volume data for selecting and exporting specific data points, charts created using custom WebGL JavaScript scripts can be integrated into these tools to enable such techniques. For example, I implemented these advanced interactive visualization features across all the aforementioned chart types in my thesis [SRDH17]. In the future, charts may not require manual brushing and linking. Instead, graph areas where the human eye focuses for longer durations could automatically export data for further analysis, adding a new layer to interactive visual analytics and Human-Computer Interaction (HCI).

For my charts' color choices, I will use sequential light-to-dark blue for ordered data with no rainbows, as they lack perceptual uniformity. For trends, I will apply diverging blue-gray-red colors. I plan to use three to four categorical colors that showcase high contrast and remain colorblind-safe. Saturated red will be used for highlighting important data points, while other, less important data will appear as pale gray, following Schaffer's framework (Wexler et al., 2018). I will also test all color palettes using ColorBrewer to ensure perceptual uniformity.

References

365 Data Science. (2018). Which is the best chart: Selecting among 14 types of charts Part I. YouTube.

Dougherty, J., & Ilyankou, I. (2025). Chapter 6: Chart Your Data. In hands-on data visualization. https://handsondataviz.org/chart.html

Krause, J. (2014). Color for designers: Ninety-five things you need to know when choosing and using colors for layouts and illustrations. New Riders.

Munzner, T. (2021). Color (Ch 10), Visualization Analysis & Design. YouTube.

[SRDH17]  C. Schulz, N. Rodrigues, K. Damarla, A. Henicke, D. Weiskopf. 
          Visual Exploration of Mainframe Workloads. SIGGRAPH Asia 2017 
          Symp. Vis. Art. no. 4, pp. 1-7. Association for Computing 
          Machinery, Incorporated, 2017. (cit. on pp. 3, 5).
 
Storytelling with Data. (2021). Ten considerations when designing a graph. YouTube.

Subotin, S. (n.d.). Dashboard design best practices. Toptal. https://www.toptal.com/designers/data-visualization/dashboard-design-best-practices

Wexler, S., Shaffer, J., & Cotgreave, A. (2018). The big book of dashboards: Visualizing your data using real-world business scenarios (1st ed.). Wiley.

<img width="962" height="224" alt="image" src="https://github.com/user-attachments/assets/133798f2-7186-4131-ad4d-68ea1bdcde0b" />


# How Analytics Shapes Decision Making: From Descriptive to Cognitive by Krishna Damarla 

Descriptive analytics (what happened) summarizes historical data to answer the question "what happened," giving numerical statistical insights into past business performance. It can be based on a sample (part of the population), or a census (the entire population). For example, in examining the average age of 100 randomly selected Trine University students (AbdulHussein, 2022), the average age is a statistic for the sample, and the mean age of all Trine University students is a parameter of the entire population.

Exploratory analytics (understand data) focuses on "understanding the data" rather than summarization. Finding correlations and identifying relationships are part of it (Devopedia, 2022). For instance, it can be noticed from email marketing data (Ponnambalam, 2024) that a 30% discount on items, such as USB drives and headphones, worked better than a 40% off. An income-based study showed that people who earn more than $150,000 expressed less interest in the ads. Another example is discovering that sales are higher in certain geographic regions or during certain months. These insights help us in re-evaluating our pricing strategies in terms of sales and revenue.

Diagnostic Analytics (why it happened, root cause analysis) is used to examine trends in past data to identify possible root causes or relationships between variables (Stathopoulos, 2024).  It’s typically used after an event occurs to understand the reasons behind it. For example, investigating a drop in sales by analyzing data on customer behavior, marketing campaigns, and other factors to determine the root cause of the decline. Exploratory Analytics is about looking for patterns and insights without a specific hypothesis, whereas Diagnostic Analytics is about understanding the cause of a known issue or event.

Explanatory analytics (Main cause / core reason) determines the "underlying reasons for the problem" and presents narratives with future vision. For example, a recent CrowdStrike software update caused a global IT outage (Sato, 2024). According to an investigation by CrowdStrike, a bug in the update's test program stopped it from validating the configuration content before deployment. The main reason is an inconsistency between the input fields provided in the update and what was intended. Because of inadequate testing procedures, this was overlooked. To prevent similar issues in the future, it is crucial to test different test scenarios and validate software modifications thoroughly.

Predictive analytics (How future looks) applies statistical methodologies and machine learning to identify patterns in large datasets and forecast future possibilities (Ponnambalam, 2024). Statistical learning techniques can be supervised, such as regression to predict numerical results and classification to classify non-numerical outcomes, or unsupervised, like clustering (AbdulHussein, 2022a). Machine learning techniques, such as transformers, neural networks, and decision trees, play a vital role as well. GPT-4 models, for example, can anticipate the next word in a sentence or generate relevant text based on prior information. In real life, investment firms use predictive analytics to analyze global market trends and economic indicators of a business (Halton, 2024). 

Prescriptive analytics (What should we do ? (after we have seen the future in predictive analytics)) goes beyond predicting future outcomes by recommending specific actions to achieve the best results using simulation, optimization, and risk assessment (AbdulHussein, 2022b). For example, distributing funds to different financial products to maximize return. It provides an overview by evaluating various aspects, including estimating resources (budget, time, usage effort), cost-benefits, business competition, product changes, and other social, environmental, and economic changes.  For instance, an investment advisory firm may use prescriptive analytics to suggest strategies for multinational companies, which may include recommendations such as investing in high-growth markets, emerging technology adoption, or mergers and acquisitions (Halton, 2024) and helping them create investment strategies that align with their goals and maximize results.

Experimental analytics (EXA) tests the solution’s performance in real-world conditions. This contrasts with simulation-based prescriptive analysis. It involves the implementation of a business plan on a subset. Testing various options, and identifying unknowns (Ponnambalam, 2024). The main steps include selecting a validated hypothesis, design and execution, result analysis, and choosing the best option. These tests can be repeated or modified to optimize the results. For example, in the use case of an email campaign (Ponnambalam, 2024), the experiment aimed to evaluate whether there was a difference in conversion rates (customers purchasing the product out of total customer visits) between discounts of 30% and 40% for customers who earn between $100,000 and $150,000. Data suggests that a 30% discount can lead to higher conversions. To verify this, an A/B test is run with two subgroups of customers: Subgroup A would receive a 30% discount, while Subgroup B would receive a 40% discount. These subgroups are evenly distributed on variables such as age and gender, and the campaigns were held on the same day to control the effect of the day of the week. Results were compared to determine if the discount rate significantly affects the conversion rates. 

A new era of analytics powered by AI is emerging. With solutions like SAP Predictive Analytics, we can forecast results more accurately. AI is used in prescriptive analytics to model scenarios and suggest the optimal action. Experimental analytics is conducting virtual experiments and AI-driven testing (Ponnambalam, 2024). Automated analytics uses solutions like Google’s AutoML to automate business processes without human intervention. Cognitive Analytics (Ulster University, n.d) is improving the quality of analytics by imitating human intelligence and providing deep insights into complex data with products like IBM Watson and Microsoft Cortona. Soon, integrating analytics with other fields like quantum computing, cybersecurity, multimodal AI, and AI-embedded hardware will transform all industries by increasing efficiency and innovation. This integration will enable real-time decision-making, faster threat detection, and operational efficiency, enabling smarter communication with more connected systems in areas such as automotive and space tourism (Apptunix, 2023).

**References**

AbdulHussein, A. (2022). Data Analytics and Decision Making. University of Windsor. https://ecampusontario.pressbooks.pub/dataanalyticsvls1/chapter/2-1-descriptive-analytics/

AbdulHussein, A. (2022a). Data Analytics and Decision Making. University of Windsor. https://ecampusontario.pressbooks.pub/dataanalyticsvls1/chapter/3-1-predictive-analytics/

AbdulHussein, A. (2022b). Data Analytics and Decision Making. University of Windsor. https://ecampusontario.pressbooks.pub/dataanalyticsvls1/chapter/4-1-prescriptive-analytics/ 

Apptunix. (2023). How AI is helping to make space travel more affordable. Apptunix. https://www.apptunix.com/blog/how-ai-is-helping-to-make-space-travel-more-affordable/

Devopedia. (2022). Exploratory Data Analysis. https://devopedia.org/exploratory-data-analysis

Halton, C. (2024). Predictive analytics: Definition, model types, and uses. Investopedia. https://www.investopedia.com/terms/p/predictive-analytics.asp

International Institute of Business Analysis. (2015). A guide to the business analysis body of knowledge (BABOK guide) (Version 3.0). Toronto, ON: International Institute of Business Analysis.

Ponnambalam, K. (2024). Business analytics: Descriptive, exploratory, and explanatory techniques. LinkedIn Learning. https://www.linkedin.com/learning/business-analytics-foundations-descriptive-exploratory-and-explanatory-analytics

Sato, M. (2024). CrowdStrike and Microsoft: All the latest news on the global IT outage. The Verge. https://www.theverge.com/24201803/crowdstrike-microsoft-it-global-outage-airlines-banking

Stathopoulos, C. (2024). Becoming a Business Analyst: Learning to Translate Data into Actionable Insights. O'Reilly Media, Inc. https://learning.oreilly.com/course/becoming-a-business/0642572047689/ 

Ulster University. (n.d.). Cognitive Analytics Research. https://www.ulster.ac.uk/cognitive-analytics-research/cognitive-analytics

<img width="896" alt="image" src="https://github.com/user-attachments/assets/45e5bbaf-d075-41b7-9f9b-38d569a2d98d">

<img width="897" alt="image" src="https://github.com/user-attachments/assets/913839f3-37c7-4946-bfc0-fb1fb9636498">

<img width="812" alt="image" src="https://github.com/user-attachments/assets/d2194ecb-71cf-4d32-a10d-880a1bfd2b22">

# From Data to Decisions: Harnessing Tableau for Strategic Business Insights by Krishna Damarla

## Tableau's Decision Support

Business decision-making benefits greatly from Tableau to visualize complex data because of some of the following unique points the tool offers:

1. Data Visualization and Interactivity: Tableau has advanced visualization techniques that allow users to interact with data through dashboard actions such as filtering and selection. For example, clicking on a region in a sales map can dynamically update related visualizations to display trends unique to a product, enabling seamless exploration. Tableau’s storyboards craft a clear narrative & key insight from multiple dashboard explorations, making it easier for executives to understand the data for faster business decisions (Francis, 2019).

2. Data Preparation Simplification: Tableau Data Interpreter automatically cleans unstructured data from Excel or CSV files, while Tableau Prep Builder streamlines data preparation. Tableau Prep Conductor automates these processes, allowing users to focus on analysis rather than data preparation (Baldwin, 2016).

3. Customization and Integration: Tableau supports the creation of custom charts through the Extensions API. It also seamlessly integrates with programming languages such as R and Python via TabPy Server for advanced analytics and machine learning. While, SQL, and JavaScript for enhanced data querying and web application functionalities. Tableau Public Cloud enables community collaboration by allowing users to share insights.

4. Data Blending Capabilities: Tableau can blend data from multiple sources (e.g., Salesforce & Google Analytics) without complex joins for seamless cross-platform integration.

5. Mobile and Real-Time Access: Users can access dashboards on mobile devices for real-time updates, critical for making timely decisions based on current information. Tableau’s dashboards tailored to specific audiences integrate live data sources in real-time, essential for industries where accuracy and timing are crucial (Stikeleather, 2013).

However, Tableau does have a high learning curve and cost, which can be challenging for smaller organizations, and its AI capabilities are limited compared to other tools in the market.

Scenario Where Tableau Best Supports Decision-Making

In a modern manufacturing environment (Tableau, 2024a), Tableau optimizes supply chain operations and improves efficiency. A manufacturing company can leverage Tableau for:

1. Comprehensive View Creation: Blending data from ERP, CRM and logistics systems offers clients a holistic perspective of the supply chain for effective resource allocation.

2. Predictive Analytics: Production scheduling and efficient inventory management can be made easier with product demand forecasting based on past sales and market trends.

3. Supply Chain Analysis: To make strategic sourcing decisions, tableau’s tools can be utilized to assess supplier performance, delivery times, and inventory turnover (Tableau, 2024b).

4. Interactive Dashboard Visualizations: To identify bottlenecks and boost operational effectiveness, production metrics like throughput, defect rate and outages can be visualized with user interactive features. Highlighting Key Performance Indicators (KPIs) related to production, quality and supply chain efficiency enables business executives for strategic planning and decision-making (The Creators Project, 2015).

References

Baldwin, D. (2016). Mastering Tableau: Smart business intelligence techniques to get maximum insights from your data. Packt Publishing. https://www.packtpub.com/en-us/product/mastering-tableau-9781784397692

Francis, M. (2019). Creating Interactive Tableau dashboards. LinkedIn Learning. https://www.linkedin.com/learning/creating-interactive-tableau-dashboards/  

Stikeleather, J. (2013). How to tell a story with data. Harvard Business Review. https://hbr.org/2013/04/how-to-tell-a-story-with-data

Tableau. (2024a). Manufacturing analytics: Build a modern supply chain, reduce your risk, and save cost with data. Salesforce. https://www.tableau.com/solutions/industries/manufacturing 

Tableau. (2024b). Supply chain analytics: Efficiently deliver more with less across your supply chain. Salesforce. https://www.tableau.com/solution/supply-chain-analytics

The Creators Project. (2015). ReForm - Data becomes art in immersive visualizations. YouTube.

<img width="973" alt="image" src="https://github.com/user-attachments/assets/544d0ff7-e8b4-4ed0-bcc7-6e632e30bd19">

# Interactive Actions in Dashboard Visualizations: Naive to Advanced by Krishna Damarla

In Tableau, you can add six types of actions to a dashboard to explore data dynamically, increasing user engagement for visual insights. They are Filter, Highlight, Go to URL, Go to Sheet, Change Parameter, and Change Set Values (used for brushing or drill-down). Let’s look at the two most common actions: Highlight and Filter within a dashboard that shows regional sales and employee ratings (Francis, 2019).

1. Highlight Action

The Highlight action filters data in other sheets based on selections made in one sheet. In the left dashboard example below, selecting the SE region in the timeline (line chart) will highlight all relevant data across associated sheets, to show only results for that SE region. The action runs when you select an item, and de-selecting the same item will return you to the original dashboard view (right dashboard below).

![image](https://github.com/user-attachments/assets/1e3c8ed6-fd18-42d2-b071-474131d83185)   ![image](https://github.com/user-attachments/assets/1c87d380-c957-4188-adc4-a89d8f0acd0e)


 2. Filter Action

The Filter action dynamically updates data in other sheets based on selections. For example, clicking on a specific time point in the SW region of the timeline will filter the dashboard to display only products sold during that specific week and employees responsible for sales in that week. You can customize this action to run either on selection or on hover.

![image](https://github.com/user-attachments/assets/9a6bf141-9bdd-48ef-bdaf-b561ca123af5)


While these actions are widely used, they are limited in scope. For more complex research goals, such as exploring geospatial data, additional interactions may be required. Visual Information-Seeking Mantra proposed by Shneiderman (Aigner, 2007) is highly relevant in this context. This mantra, "overview first, zoom and filter, then details-on-demand," is useful for effectively navigating large datasets. 

3. Overview First, Zoom and Filter, Then Details-On-Demand Action

One example that follows this advanced action is Interactive Catchment Explorer (ICE), a web-based interactive data visualization framework (Walker et al., 2020). 

# ICE Usecase

ICE (Interactive Catchment Explorer) is designed to help decision-makers explore complex geospatial environmental datasets and model predictions. The framework is built on Shneiderman's Mantra, allowing users to first gain a broad overview, zoom in for filtering, and then drill down into specific details. 

Key Components of ICE:

Map: Displays spatial features and allows users to pan and zoom at different scales.
Selection Menu: Enables the selection of variables (e.g., mean summer temperature) that determine the color coding of features.
Crossfilters: Histograms for crucial variables (e.g., elevation, forest cover) help users visualize data distributions and filter specific values. 
For example, filtering data by Forest Cover (%) in the histogram will highlight corresponding regions on the map, as demonstrated in the ICE dashboard below. 

![image](https://github.com/user-attachments/assets/d47d8c3b-b945-4e34-a34c-85e99d6537f6)

In another application, the ICE framework is used to assess the vulnerability of trout species towards climate change within the Crown of the Continent Ecosystems. It displays the overall risk level for various trout conservation population and uses cross-filters to analyze different risk levels, including overall risk, climate risk, and demographic risk as depicted in the dashboard below. This visual analysis helps stakeholders understand potential impacts of climate change on trout populations and recommend conservation strategies to reduce associated risks (Walker et al., 2020).

![image](https://github.com/user-attachments/assets/8f8de852-8e7c-4918-9f92-264b22c07883)

References 

Aigner, W. (2007). Visual information-seeking mantra by Shneiderman. InfoVis Wiki. https://infovis-wiki.net/wiki/Visual_Information-Seeking_Mantra / https://www.infovis.org/resources.php 

Francis, M. (2019). Creating interactive Tableau dashboards. LinkedIn Learning. https://www.linkedin.com/learning/creating-interactive-tableau-dashboards/

Keim, D., Kohlhammer, J., Ellis, G., & Mansmann, F. (2010). Mastering the information age: Solving problems with visual analytics. Eurographics Association.

Walker, J. D., Letcher, B. H., Rodgers, K. D., Muhlfeld, C. C., & D’Angelo, V. S. (2020). An interactive data visualization framework for exploring geospatial environmental datasets and model predictions. U.S. Geological Survey. https://www.usgs.gov/apps/ecosheds/#/   

https://github.com/EcoSHEDS/fpe-model & https://www.usgs.gov/apps/ecosheds/fpe/#/ 

https://ecosheds.github.io/northeast-temp-model/ 

https://db.ecosheds.org/ 

https://aktemp.uaa.alaska.edu/viz/ 

https://www.usgs.gov/apps/ecosheds/ice-nps-ner/

https://ecology.wa.gov/water-shorelines/water-quality 

https://www.hydrotech-group.com/blog/wastewater-treatment-across-the-world-which-countries-recycle-the-most-and-where-is-the-best-water-quality 

<img width="881" alt="image" src="https://github.com/user-attachments/assets/510a30f4-64ab-47e5-9421-ec7a47e9e2be">

<img width="894" alt="image" src="https://github.com/user-attachments/assets/7adebaf0-d355-4678-a432-f8f4069f4b63">

# Four Critical Questions for Designing Effective Dashboards

Creating an effective dashboard that displays useful information at a glance requires asking four critical questions to ensure it serves its purpose and meets user needs (Subotin, n.d.).

First, who is the dashboard suitable for? Understanding the target audience helps designers determine the visualization type, complexity, and detail level. While experienced viewers may need more complex insights, general viewers benefit from its simplicity (Francis, 2019).

Second, where should I view the dashboard? The display device impacts layout and interactivity, whether on desktop, tablet, or mobile. For example, mobile screens need more compact and touch-friendly interfaces (Francis, 2019).

Third, why is the dashboard being created? Understanding the purpose (whether for exploration, explanation, or tracking KPIs) leads to the selection of data and visualization. Dashboards often combine data from multiple departments in one place (Hayward, 2024). To increase organizational value, design choices should focus on creating dashboards that serve a purpose (Subotin, n.d.).


Finally, what data and elements need to be shown? Choosing relevant data avoids clutter and confusion. Additionally, deciding whether the dashboard displays real-time or historical data (Francis, 2019) can guide the use of interactive elements such as drill-down, drop-down, and zooming, thus improving user experience and engagement.

Failure to ask these questions can lead to poor design, low usability, and the risk of dashboards that are too complex or simplistic, misaligned for user needs, or cluttered with irrelevant and inconsistent information. Misaligned dashboards may overwhelm or distract the audience, while cluttered displays may dilute the intended insights.

In summary, asking these questions is crucial to creating a purposeful and user-friendly dashboard suited to its context. These questions ensure the dashboard is designed with clarity, focus, and relevance, enhancing its impact and usability to deliver meaningful insights (Francis, 2019).

References

Francis, M. (2019). Creating interactive Tableau dashboards. LinkedIn Learning. https://www.linkedin.com/learning/creating-interactive-tableau-dashboards/

Hayward, E. (2024). Starter guide to dashboards. Klipfolio. https://www.klipfolio.com/blog/starter-guide-to-dashboards#WhatDashboard

Subotin, S. (n.d.). Dashboard design best practices. Toptal. https://www.toptal.com/designers/data-visualization/dashboard-design-best-practices

<img width="981" alt="image" src="https://github.com/user-attachments/assets/f8027b82-bf22-4e30-b12d-11b9809a1e40">

<img width="980" alt="image" src="https://github.com/user-attachments/assets/70eebb16-ae0d-4f79-a6b5-02095815739c">

# Reporting Transformation at Landon Hotels with Tableau by Krishna Damarla

## Issue

Landon Hotels utilize Excel spreadsheets for reporting. Due to potential expansion of company, this model of reporting does not scale to meet the dynamic, complex requirements of the firm. To date, 360 employees use reports for analysis. Of these, 30 managers and 10 Business Intelligence (BI) team members create static Excel reports, creating confusion and lack of standardization across the organization. Without a centralized framework at place, employees led by these leaders are also vulnerable to such inefficiencies (Ngwena, 2022).

## Solution 

To address these issues, Landon Hotels plan to use Tableau to transition from static reporting to dynamic reporting. This change will enable real time data visualization and deliver accurate insights from a single source of truth across the organization. Further, they are focusing on deploying automated data pipelines to ensure timely data delivery for reporting. A Tableau deployment plan will be created with KPIs to track progress and measure success. In addition, the firms existing IT infrastructure management will be outsourced to third party provider (Red30) to integrate the new solutions into its cloud-based platform. Finally, the company is looking for turnkey training programs to equip its employees with the skills needed to use the newly implemented solution (Ngwena, 2022). 

## Key Lessons Learned and Reevaluations

**1. Strategic Planning**

I learned to create a clear plan for successful delivery. Using Tableau Blueprint (Baldwin, 2016) can further help align projects with company goals and create KPIs to track progress. This study also taught me that planning is as important as implementation. And, to consider the impact of external influences throughout all the phases of project from deployment to maintenance.

**2. User Groups and Licensing**

I learned that to determine the appropriate Tableau licenses, I needed to understand different roles of users, and their level of involvement in the organization. For example, the BI team needs access to Tableau Desktop and Prep Builder (Baldwin, 2016) as Creators, while managers and employees need Explorer and Viewer licenses, respectively. 

Previously, I focused more on creating technical solutions, than clustering user groups. This business case taught me that users should be assigned different types of licenses to avoid unnecessary costs and to ensure that all users have access to the right tools.

**3. Data pipeline Automation**

I learned that automation is key for timely and accurate data extraction. Tableau Prep Conductor can be used to schedule data workflows (or) Hyper API to extract with ETL script (Ngwena, 2022).

**4. IT Infrastructure Management**

I learned the value of focusing on the business’s priorities and re-using existing IT infrastructure rather than building it from scratch. For Landon Hotels, choosing Tableau Cloud and to outsource IT infrastructure management to Red30 (Ngwena, 2022) can reduce the need for in-house expertise and save time.

**5. Adaptability to growth and Integration**

I learned to develop solutions with future growth in mind. Continuous learning and the ability to integrate with other platforms like R and Salesforce (including CRM Analytics, formerly Tableau CRM and the Einstein One for AI model deployment), allow BI tools like Tableau to expand its capabilities and adapt to evolving customer needs (Salesforce, n.d.)

**References**

Baldwin, D. (2016). Mastering Tableau: Smart business intelligence techniques to get maximum insights from your data. Packt Publishing. https://www.packtpub.com/en-us/product/mastering-tableau-9781784397692

Ngwena, T. (2022). Everybody's introduction to Tableau. LinkedIn Learning. https://www.linkedin.com/learning/everybody-s-introduction-to-tableau-2022/solution-business-use-case-landon-hotels?u=130423532

Salesforce. (n.d.). Tableau analytics: Make better, faster decisions with enterprise analytics tailored to your CRM. Salesforce.com. https://www.salesforce.com/eu/products/einstein-analytics/overview/ 

Tableau. (n.d.). Pass Expressions with Analytics Extensions. Tableau.com. https://help.tableau.com/current/pro/desktop/en-us/r_connection_manage.htm

<img width="949" alt="image" src="https://github.com/user-attachments/assets/4e04d179-bb60-42ef-bd21-cf04c339dd8a">

<img width="984" alt="image" src="https://github.com/user-attachments/assets/8b547574-f632-4d47-a58e-b757a611cfb2">

# Healthcare Analytics Experience by Krishna Damarla

<img width="957" alt="image" src="https://github.com/user-attachments/assets/c293fe49-0909-4ae2-a260-37a3738894b3">

Code to Implement above Suggestion: [face-recognition.py](../Data-Science/Python/face-recognition.py)

Note: The above code snippet is intended for scenarios where a person's face has already been trained using a predefined set of images in a training model. In real-world applications, recognizing the face of an unknown individual requires using a government-approved ID and photograph to train the model, enabling it to match the person in live video for recognition purposes. Implementing such an architecture must align with healthcare security practices and regulations of local body, such as HIPAA in the U.S, PIPEDA in Canada, GDPR in Europe, DISHA in India, and PIPL in China.


# Health Insurance Analytics Experience by Krishna Damarla

Project Experience

In a project with an insurance client, I extracted data into a central data warehouse table for advanced analytics. At first, I worked with senior business analysts to understand the key business challenges and identified key performance indicators (KPIs) that directly affect enterprise operations. Later, I focused on cleansing, data modelling, and leveraging statistical, machine-learning models for descriptive and predictive analysis (Ariansen & Madecraft, 2022). This project culminated in recommending data-driven solutions to client to enhance their decision-making in business operations and marketplace positioning.

Tools Usage

In this project, I compared various business intelligence (BI) tools from major cloud vendors. I identified the pros and cons of these tools with a focus on client-specific reporting needs. This includes depth of analysis, chart selection, colour combinations, and data masking (security) for specific users. Although some BI tools offer customization, many fail, even with enterprise licenses. I decided upon Cognos due to its ease of on-premises integration, superior customization capabilities, data modelling options, and connectors for external data sources (Hiter, 2023).

Future Outlook

I am interested in learning about various techniques in integrating generative artificial intelligence (GenAI) into reporting and dashboard creation (Raghupathi & Raghupathi, 2021). For instance, enabling users to create reports with natural language commands like, "Create an interactive bar chart from recent sales data," which would then be converted into an SQL/NoSQL query. Such a query verified by developers would then pull information from the database, generate a creative report, and present it to the user for visual analysis. This type of innovation is cost-effective for non-technical clients, allowing them to save valuable time while enhancing their decision-making capabilities.

References

Ariansen, J. D., & Madecraft. (2022). Introduction to Business Analytics. LinkedIn Learning. https://www.linkedin.com/learning/introduction-to-business-analytics-14621877

Hiter, S. (2023). Cognos vs. Power BI: 2024 data platform comparison. eWeek.com.  https://www.eweek.com/cloud/cognos-vs-power-bi/

Raghupathi, W., & Raghupathi, V. (2021). Contemporary business analytics: An overview. MDPI Journal. https://doi.org/10.3390/data6080086

<img width="958" alt="image" src="https://github.com/user-attachments/assets/34f59064-a8af-4b01-9a50-0c7bc27b100d">

# Best Practices for Using Color in Data Visualization by Krishna Damarla

If a colleague or stakeholder suggests that the dashboard could be made more impactful by adding more or bolder colors, my response would be: I understand the desire to make the dashboard stand out more. But adding more or darker colors can reduce the effectiveness. Instead, we should focus on using color strategically, as Jeffrey suggests in his "The Big Book of Dashboards” (Wexler et al., 2018) and as Krause suggests in his book “Color for Designers” (Krause, 2014). 

The main points regarding the use of color in data visualization are:

1. Five Uses of Color (Wexler, 2021): The following graphic by Jeffrey Schaefer outlines the ways color can be used in data visualization.

   o   Sequential Colors: Using gradient colors to show value progression (low to high).
   
   o   Diverging: Showing the contrast between two extremes with a neutral mid-point.
   
   o   Categorical: Using distinct colors to separate different categories. It’s best to use no more than 4 distinct colors. Group similar categories and then use sequential coloring for differentiation. Example applications are heat-maps, and density maps.
   
   o   Highlight: Drawing attention to specific data points.
   
   o   Alert Colors: Colors like red can highlight important data or signal alerts, but cultural contexts are important as color meanings can differ from region to region.

2. Use Color Sparingly (Wexler et al., 2018): Too much color can overwhelm and obscure insights. Minimal, well-placed color helps make data clearer and more understandable. Adding more or bolder colors to dashboards won’t always make dashboard more impactful.

3. Avoid Traffic Light Colors: Red-green color blindness affects many people, so using the typical traffic light colors can be problematic. Adjusting colors to be less dense or using alternatives like blue and orange can make visuals more accessible.

4. Maintain Color Harmony: Make visuals appealing without overwhelming them by trying different color harmony palettes (complementary, analogous, triadic).

5. Color in Branding (Krause, 2014): Understanding that color plays a major role in brand identity, and recognition, and can influence consumer behavior.

6. Emotional Impact of Colors: Color can evoke emotions and influence a viewer’s thought process and behaviors. Use color choices to set the mood or tone of a design, whether professional or elegant.

7. Testing Color Combinations: Test different colors in the real world to see how they perform and resonate with your audience. Experiment with color to discover unique palettes and combinations to enhance your designs.

8. Color in Digital and Print: Understand the difference between digital screen (RGB) and print (CMYK) colors to ensure accurate color reproduction.

9. Feedback and Revision (Krause, 2014): Get feedback from peers or audiences on color choices and be willing to make changes based on their feedback. Find color inspiration in nature, art, and everyday surroundings to develop original color palettes. Use tools like color wheel (primary, secondary, tertiary colors), swatches, and software in selecting and managing colors.

References

Krause, J. (2014). Color for designers: Ninety-five things you need to know when choosing and using colors for layouts and illustrations. New Riders.

Wexler, S. (2021). How to use data visualization to make better decisions—Faster. LinkedIn Learning. https://www.linkedin.com/learning/how-to-use-data-visualization-to-make-better-decisions-faster/

Wexler, S., Shaffer, J., & Cotgreave, A. (2018). The big book of dashboards: Visualizing your data using real-world business scenarios (1st ed.). Wiley. https://www.tableau.com/big-book-dashboards



