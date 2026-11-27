# Product Data Science — Master Roadmap

>
Goal: Become an excellent Product Data Scientist who can take an ambiguous real-world/product question, investigate it with data, build appropriate statistical/ML models, establish causality where possible, and communicate a clear recommendation.

>
Target roles: Product Data Scientist · Experimentation Scientist · Applied Data Scientist · Decision Scientist · Causal Inference / Experimentation · Research Data Scientist · Sports Data Scientist

>
Learning principle: Don't just learn how to implement something. Learn when to use it, why it works, what assumptions it makes, and how to interpret the result.

>
Coding principle: Write the code yourself. Use ChatGPT/docs when stuck, but don't copy implementations you don't understand.

---

#
0. CS & Programming Foundations

## 0.1 Python Fundamentals
- [ ] Variables and types
- [ ] Integers / floats / strings / booleans
- [ ] Lists
- [ ] Tuples
- [ ] Dictionaries
- [ ] Sets
- [ ] Indexing and slicing
- [ ] if / elif / else
- [ ] for loops
- [ ] while loops
- [ ] Functions
- [ ] Parameters and return values
- [ ] Scope
- [ ] List/dict/set comprehensions
- [ ] enumerate
- [ ] zip
- [ ] range
- [ ] Sorting with sorted()
- [ ] Lambda functions
- [ ] \*args / \*\*kwargs
- [ ] Exceptions / try / except
- [ ] Reading and writing files
- [ ] Modules and imports
- [ ] Virtual environments
- [ ] Packages / pip
- [ ] Basic debugging

## 0.2 Python Software Practices
- [ ] Write clean functions
- [ ] Meaningful variable names
- [ ] Type hints
- [ ] Docstrings
- [ ] Assertions
- [ ] Unit tests
- [ ] pytest
- [ ] Debugging with breakpoints
- [ ] Basic logging
- [ ] Understand Python project structure
- [ ] requirements.txt
- [ ] .gitignore
- [ ] Git basics
- [ ] Branches
- [ ] Commits
- [ ] Pull requests / code review concepts

---

#
1. Algorithms & Data Structures

>
Technical literacy, not becoming a competitive programmer.

## 1.1 Complexity
- [ ] Big-O notation
- [ ] O(1)
- [ ] O(log n)
- [ ] O(n)
- [ ] O(n log n)
- [ ] O(n²)
- [ ] Understand time vs space complexity
- [ ] Identify complexity of simple Python code

## 1.2 Searching
- [x] Linear search
- [x] Binary search
- [ ] Binary search with duplicates
- [ ] First occurrence
- [ ] Last occurrence
- [ ] Understand why binary search is O(log n)

## 1.3 Core Data Structures
- [ ] Arrays / Python lists
- [ ] Stacks
- [ ] Queues
- [ ] Hash tables / dictionaries
- [ ] Sets
- [ ] Linked lists
- [ ] Trees
- [ ] Binary search trees
- [ ] Heaps / priority queues
- [ ] Graphs

## 1.4 Core Algorithms
- [x] Linear search
- [x] Binary search
- [ ] Bubble sort
- [ ] Selection sort
- [ ] Insertion sort
- [ ] Merge sort
- [ ] Quick sort
- [ ] Understand recursion
- [ ] BFS
- [ ] DFS
- [ ] Basic greedy algorithms
- [ ] Basic dynamic programming intuition

## 1.5 Algorithmic Thinking
- [ ] Break a problem into smaller problems
- [ ] Identify brute-force solution
- [ ] Identify bottleneck
- [ ] Improve complexity
- [ ] Think about edge cases
- [ ] Test assumptions
- [ ] Explain an algorithm verbally

---

#
2. NumPy

## 2.1 Arrays
- [ ] Create arrays
- [ ] Array shape
- [ ] Dimensions
- [ ] Indexing
- [ ] Slicing
- [ ] Boolean indexing
- [ ] Reshaping
- [ ] Transposing
- [ ] Concatenation
- [ ] Broadcasting

## 2.2 Numerical Operations
- [ ] Vectorised operations
- [ ] Sum
- [ ] Mean
- [ ] Median
- [ ] Standard deviation
- [ ] Min / max
- [ ] Quantiles
- [ ] Random number generation
- [ ] Sampling
- [ ] Simulations

## 2.3 Numerical Thinking
- [ ] Understand why vectorisation matters
- [ ] Understand arrays vs Python lists
- [ ] Simulate probability experiments
- [ ] Use simulation to check analytical results

---

#
3. pandas

## 3.1 DataFrames
- [ ] Create a DataFrame
- [ ] Read CSV
- [ ] Read Excel
- [ ] Inspect data
- [ ] head()
- [ ] info()
- [ ] describe()
- [ ] Select columns
- [ ] Filter rows
- [ ] Boolean conditions
- [ ] Create new columns
- [ ] Rename columns
- [ ] Drop columns/rows

## 3.2 Cleaning
- [ ] Missing values
- [ ] Detect missingness
- [ ] Imputation
- [ ] Duplicates
- [ ] Incorrect data types
- [ ] Outliers
- [ ] String cleaning
- [ ] Date/time columns
- [ ] Categorical variables

## 3.3 Aggregation
- [ ] groupby
- [ ] agg
- [ ] transform
- [ ] Counts
- [ ] Means
- [ ] Medians
- [ ] Multiple aggregations
- [ ] Grouped proportions
- [ ] Cohort calculations

## 3.4 Combining Data
- [ ] Merge
- [ ] Join
- [ ] Concatenate
- [ ] Understand one-to-one joins
- [ ] Understand one-to-many joins
- [ ] Understand many-to-many joins
- [ ] Detect accidental row multiplication

## 3.5 Time-Series Data
- [ ] Datetime conversion
- [ ] Extract date components
- [ ] Resampling
- [ ] Rolling averages
- [ ] Lagged variables
- [ ] Time-based grouping

---

#
4. Data Visualisation

## 4.1 matplotlib
- [ ] Line plots
- [ ] Scatter plots
- [ ] Histograms
- [ ] Bar charts
- [ ] Box plots
- [ ] Subplots
- [ ] Labels
- [ ] Titles
- [ ] Legends
- [ ] Annotations

## 4.2 Statistical Visualisation
- [ ] Distribution plots
- [ ] Relationships between variables
- [ ] Correlation plots
- [ ] Group comparisons
- [ ] Confidence intervals
- [ ] Error bars
- [ ] Time trends
- [ ] Heterogeneity across groups

## 4.3 Data Storytelling
- [ ] Choose an appropriate plot
- [ ] Remove unnecessary visual noise
- [ ] Highlight the important result
- [ ] Avoid misleading axes
- [ ] Explain uncertainty
- [ ] Turn a chart into a clear conclusion

---

#
5. Probability

> Rebuild from scratch. Don't assume MSc knowledge is still fresh.

## 5.1 Foundations
- [ ] Sample spaces
- [ ] Events
- [ ] Conditional probability
- [ ] Independence
- [ ] Bayes' theorem
- [ ] Law of total probability

## 5.2 Random Variables
- [ ] Discrete random variables
- [ ] Continuous random variables
- [ ] PMF
- [ ] PDF
- [ ] CDF
- [ ] Expectation
- [ ] Variance
- [ ] Covariance
- [ ] Correlation
- [ ] Conditional expectation

## 5.3 Distributions
- [ ] Bernoulli
- [ ] Binomial
- [ ] Geometric
- [ ] Poisson
- [ ] Uniform
- [ ] Normal
- [ ] Exponential
- [ ] Gamma
- [ ] Beta
- [ ] Student's t
- [ ] Chi-squared
- [ ] F distribution

## 5.4 Core Results
- [ ] Law of Large Numbers
- [ ] Central Limit Theorem
- [ ] Law of Total Expectation
- [ ] Law of Total Variance
- [ ] Covariance identities
- [ ] Transformations of random variables

## 5.5 Simulation
- [ ] Monte Carlo simulation
- [ ] Simulate distributions
- [ ] Estimate probabilities
- [ ] Estimate expectations
- [ ] Verify theoretical results computationally

---

#
6. Statistical Inference

## 6.1 Estimation
- [ ] Estimators
- [ ] Bias
- [ ] Variance
- [ ] MSE
- [ ] Consistency
- [ ] Efficiency
- [ ] Method of moments
- [ ] Maximum likelihood
- [ ] Likelihood functions
- [ ] Log-likelihood

## 6.2 Sampling Distributions
- [ ] Sampling distributions
- [ ] Standard errors
- [ ] CLT-based approximations
- [ ] Bootstrap
- [ ] Parametric bootstrap
- [ ] Non-parametric bootstrap

## 6.3 Confidence Intervals
- [ ] Confidence interval intuition
- [ ] Confidence intervals for means
- [ ] Confidence intervals for proportions
- [ ] Confidence intervals for regression coefficients
- [ ] Bootstrap confidence intervals

## 6.4 Hypothesis Testing
- [ ] Null hypothesis
- [ ] Alternative hypothesis
- [ ] Test statistic
- [ ] p-value
- [ ] Type I error
- [ ] Type II error
- [ ] Statistical power
- [ ] One-sided vs two-sided tests
- [ ] Multiple testing

## 6.5 Statistical Thinking
- [ ] Statistical significance vs practical significance
- [ ] Correlation vs causation
- [ ] Selection bias
- [ ] Sampling bias
- [ ] Measurement error
- [ ] Confounding
- [ ] Simpson's paradox
- [ ] Regression to the mean
- [ ] Multiple comparisons
- [ ] p-hacking
- [ ] HARKing

---

#
7. Regression & Statistical Modelling

## 7.1 Linear Regression
- [ ] Simple linear regression
- [ ] Multiple linear regression
- [ ] OLS intuition
- [ ] Matrix formulation
- [ ] Coefficient interpretation
- [ ] Residuals
- [ ] R²
- [ ] Adjusted R²
- [ ] Confidence intervals
- [ ] Prediction intervals

## 7.2 Regression Assumptions
- [ ] Linearity
- [ ] Independence
- [ ] Homoscedasticity
- [ ] Normality of errors
- [ ] Multicollinearity
- [ ] Influential observations
- [ ] Understand what happens when assumptions fail

## 7.3 Logistic Regression
- [ ] Binary outcomes
- [ ] Log-odds
- [ ] Odds ratios
- [ ] Coefficient interpretation
- [ ] Predicted probabilities
- [ ] Classification threshold

## 7.4 GLMs
- [ ] Exponential family intuition
- [ ] Link functions
- [ ] Log link
- [ ] Logit link
- [ ] Poisson regression
- [ ] Gamma regression
- [ ] Interpretation of coefficients

## 7.5 Model Selection
- [ ] Train/test split
- [ ] Cross-validation
- [ ] Bias/variance trade-off
- [ ] Overfitting
- [ ] Underfitting
- [ ] Regularisation
- [ ] Ridge
- [ ] Lasso
- [ ] Elastic Net
- [ ] Feature selection

---

#
8. SQL

>
Become genuinely strong at SQL.

## 8.1 Basics
- [ ] SELECT
- [ ] FROM
- [ ] WHERE
- [ ] ORDER BY
- [ ] LIMIT
- [ ] DISTINCT
- [ ] NULL handling
- [ ] CASE WHEN

## 8.2 Aggregation
- [ ] COUNT
- [ ] SUM
- [ ] AVG
- [ ] MIN / MAX
- [ ] GROUP BY
- [ ] HAVING
- [ ] Conditional aggregation

## 8.3 Joins
- [ ] INNER JOIN
- [ ] LEFT JOIN
- [ ] RIGHT JOIN
- [ ] FULL JOIN
- [ ] Self joins
- [ ] Understand join cardinality
- [ ] Detect duplicate rows after joins

## 8.4 Advanced SQL
- [ ] Subqueries
- [ ] CTEs
- [ ] Window functions
- [ ] ROW_NUMBER
- [ ] RANK
- [ ] DENSE_RANK
- [ ] LAG
- [ ] LEAD
- [ ] Running totals
- [ ] Rolling averages
- [ ] PARTITION BY

## 8.5 Product SQL
- [ ] Funnels
- [ ] Cohort analysis
- [ ] Retention
- [ ] Churn
- [ ] Conversion rates
- [ ] DAU / WAU / MAU
- [ ] User segmentation
- [ ] Session analysis
- [ ] Experiment analysis
- [ ] Time-to-event calculations

---

#
9. A/B Testing & Experimentation

>
One of the most important sections for Product DS.

## 9.1 Experiment Fundamentals
- [ ] What an A/B test actually measures
- [ ] Randomisation
- [ ] Treatment group
- [ ] Control group
- [ ] Unit of randomisation
- [ ] Unit of analysis
- [ ] Treatment effect
- [ ] Average treatment effect

## 9.2 Metrics
- [ ] Define primary metric
- [ ] Define secondary metrics
- [ ] Define guardrail metrics
- [ ] Understand numerator/denominator
- [ ] Avoid metric manipulation
- [ ] Choose metrics aligned with product goals

## 9.3 Experiment Design
- [ ] Sample size
- [ ] Statistical power
- [ ] Minimum detectable effect
- [ ] Effect size
- [ ] Significance level
- [ ] Experiment duration
- [ ] Randomisation checks
- [ ] Sample-ratio mismatch

## 9.4 Experiment Analysis
- [ ] Difference in means
- [ ] Difference in proportions
- [ ] Confidence intervals
- [ ] Hypothesis tests
- [ ] Practical significance
- [ ] Heterogeneous treatment effects
- [ ] Segment analysis

## 9.5 Experiment Pitfalls
- [ ] Peeking
- [ ] Multiple testing
- [ ] Novelty effects
- [ ] Seasonality
- [ ] Interference
- [ ] Spillover effects
- [ ] Selection bias
- [ ] Attrition
- [ ] Non-compliance
- [ ] Simpson's paradox

## 9.6 Experiment Decision-Making
- [ ] Decide whether an experiment is appropriate
- [ ] Decide what should be randomised
- [ ] Decide when an experiment can stop
- [ ] Interpret ambiguous results
- [ ] Decide whether to ship
- [ ] Balance primary and guardrail metrics
- [ ] Communicate uncertainty

---

#
10. Causal Inference

>
Potential specialisation / "weapon" for Product DS.

## 10.1 Foundations
- [ ] Correlation vs causation
- [ ] Potential outcomes
- [ ] Treatment
- [ ] Control
- [ ] Individual treatment effect
- [ ] Average treatment effect
- [ ] Average treatment effect on treated

## 10.2 Causal Assumptions
- [ ] Exchangeability / no unmeasured confounding
- [ ] Positivity
- [ ] Consistency
- [ ] Understand why assumptions matter

## 10.3 DAGs
- [ ] Directed acyclic graphs
- [ ] Confounders
- [ ] Mediators
- [ ] Colliders
- [ ] Backdoor paths
- [ ] Conditioning on variables
- [ ] Identify adjustment sets

## 10.4 Observational Methods
- [ ] Regression adjustment
- [ ] Propensity scores
- [ ] Propensity score matching
- [ ] Inverse probability weighting
- [ ] AIPW
- [ ] Doubly robust estimation

## 10.5 Quasi-Experimental Methods
- [ ] Difference-in-differences
- [ ] Parallel trends
- [ ] Instrumental variables
- [ ] Regression discontinuity
- [ ] Synthetic controls

## 10.6 Heterogeneous Effects
- [ ] Treatment effect heterogeneity
- [ ] Subgroup effects
- [ ] Interaction effects
- [ ] Conditional average treatment effects
- [ ] Uplift modelling
- [ ] Causal forests

## 10.7 Causal Reasoning
- [ ] Identify causal question
- [ ] Identify treatment
- [ ] Identify outcome
- [ ] Identify confounders
- [ ] Draw a DAG
- [ ] State assumptions
- [ ] Choose identification strategy
- [ ] Estimate effect
- [ ] Test robustness
- [ ] Explain limitations

---

#
11. Machine Learning

## 11.1 ML Fundamentals
- [ ] Supervised vs unsupervised learning
- [ ] Features
- [ ] Labels
- [ ] Training data
- [ ] Validation data
- [ ] Test data
- [ ] Overfitting
- [ ] Underfitting
- [ ] Bias/variance trade-off
- [ ] Cross-validation
- [ ] Data leakage

## 11.2 Regression
- [ ] Linear regression
- [ ] Ridge
- [ ] Lasso
- [ ] Elastic Net
- [ ] Decision tree regression
- [ ] Random forest regression
- [ ] Gradient boosting

## 11.3 Classification
- [ ] Logistic regression
- [ ] Decision trees
- [ ] Random forests
- [ ] Gradient boosting
- [ ] XGBoost / LightGBM

## 11.4 Evaluation
- [ ] MSE
- [ ] RMSE
- [ ] MAE
- [ ] R²
- [ ] Accuracy
- [ ] Precision
- [ ] Recall
- [ ] F1
- [ ] ROC-AUC
- [ ] PR-AUC
- [ ] Log loss
- [ ] Calibration
- [ ] Confusion matrices

## 11.5 Feature Engineering
- [ ] Categorical encoding
- [ ] Scaling
- [ ] Transformations
- [ ] Interaction features
- [ ] Missing-value features
- [ ] Time-based features
- [ ] Feature selection

## 11.6 Model Interpretation
- [ ] Feature importance
- [ ] Partial dependence
- [ ] SHAP intuition
- [ ] Model calibration
- [ ] Error analysis

## 11.7 ML + Product
- [ ] Evaluate model performance
- [ ] Evaluate business/customer impact
- [ ] Define model success metrics
- [ ] Compare offline vs online performance
- [ ] Model monitoring
- [ ] Model drift
- [ ] Model reliability
- [ ] A/B test model changes

---

#
12. Product Analytics

## 12.1 Product Metrics
- [ ] North-star metrics
- [ ] KPIs
- [ ] Engagement
- [ ] Retention
- [ ] Churn
- [ ] Conversion
- [ ] Activation
- [ ] Revenue
- [ ] Customer lifetime value
- [ ] Frequency
- [ ] Session length

## 12.2 Funnels
- [ ] Define funnel stages
- [ ] Conversion between stages
- [ ] Identify drop-off
- [ ] Segment funnels
- [ ] Diagnose funnel changes

## 12.3 Cohorts
- [ ] User cohorts
- [ ] Time cohorts
- [ ] Retention curves
- [ ] Cohort comparisons
- [ ] Cohort-based experiments

## 12.4 Product Sense
- [ ] Understand the product
- [ ] Identify user goals
- [ ] Identify business goals
- [ ] Identify relevant metrics
- [ ] Identify trade-offs
- [ ] Identify possible unintended consequences
- [ ] Translate vague questions into measurable hypotheses

## 12.5 Product Case Studies
- [ ] "Engagement dropped 10%. What would you investigate?"
- [ ] "How would you measure whether a new feature works?"
- [ ] "What metric would you use for a recommendation system?"
- [ ] "Conversion increased but revenue fell. Why?"
- [ ] "How would you design an experiment for this feature?"
- [ ] "A/B test says the feature had no effect. What could have gone wrong?"
- [ ] "Users are spending more time in the app. Is that necessarily good?"

---

#
13. Data Engineering / Technical Literacy

>
Enough to work effectively with engineers. Don't turn this into a second degree.

## 13.1 Databases
- [ ] Relational databases
- [ ] Tables
- [ ] Primary keys
- [ ] Foreign keys
- [ ] Indexes
- [ ] Normalisation
- [ ] Basic database design

## 13.2 Data Warehouses
- [ ] What a data warehouse is
- [ ] OLTP vs OLAP
- [ ] BigQuery
- [ ] Snowflake
- [ ] Redshift
- [ ] Partitioning
- [ ] Query costs

## 13.3 dbt
- [ ] What dbt does
- [ ] Models
- [ ] Sources
- [ ] Tests
- [ ] Documentation
- [ ] Basic transformations

## 13.4 APIs
- [ ] What an API is
- [ ] HTTP basics
- [ ] GET / POST
- [ ] JSON
- [ ] API authentication
- [ ] Make API requests from Python

## 13.5 Reproducibility
- [ ] Git
- [ ] Environments
- [ ] Dependency management
- [ ] Requirements
- [ ] Project structure
- [ ] Reproducible analysis
- [ ] Basic Docker understanding

---

#
14. Data Storytelling & Communication

## 14.1 Analysis
- [ ] Define the question
- [ ] Define the metric
- [ ] Understand the data
- [ ] Identify limitations
- [ ] Explore
- [ ] Model
- [ ] Validate
- [ ] Interpret
- [ ] Recommend

## 14.2 Communication
- [ ] Explain statistics to non-statisticians
- [ ] Explain uncertainty clearly
- [ ] Explain model limitations
- [ ] Explain causal assumptions
- [ ] Present a recommendation
- [ ] Defend an analysis under questioning
- [ ] Write concise analytical summaries
- [ ] Build clear presentations

## 14.3 Executive-Level SummaryBe able to reduce a complicated analysis to:\*\*Question → Finding → Evidence → Recommendation → Caveat\*\*

---

#
15. Portfolio Projects

>
No generic Titanic projects.

>
Projects should involve questions where you genuinely don't know the answer beforehand.

##

## Project 1 — Exploratory Data Science
- [ ] Find interesting dataset
- [ ] Define question
- [ ] Clean data
- [ ] EDA
- [ ] Visualisations
- [ ] Statistical analysis
- [ ] Findings
- [ ] Limitations
- [ ] README

##

## Project 2 — Product ExperimentBuild a simulated or real product experiment.
- [ ] Define product problem
- [ ] Define hypothesis
- [ ] Define treatment
- [ ] Define control
- [ ] Define primary metric
- [ ] Define guardrails
- [ ] Calculate sample size
- [ ] Simulate experiment
- [ ] Analyse results
- [ ] Investigate heterogeneity
- [ ] Make product recommendation

##

## Project 3 — Causal Inference
- [ ] Find observational dataset
- [ ] Define causal question
- [ ] Identify treatment
- [ ] Identify outcome
- [ ] Draw DAG
- [ ] Identify confounders
- [ ] Estimate naive association
- [ ] Estimate adjusted effect
- [ ] Use IPW/AIPW or another appropriate method
- [ ] Sensitivity/robustness analysis
- [ ] Interpret assumptions
- [ ] Explain limitations

##

## Project 4 — ML + Product Decision
- [ ] Define business/product problem
- [ ] Build baseline
- [ ] Build ML model
- [ ] Cross-validation
- [ ] Evaluate model
- [ ] Error analysis
- [ ] Interpretability
- [ ] Translate model performance into product impact
- [ ] Recommend whether to deploy

##

## Project 5 — Sports Data SciencePossible question:

> What actually predicts winning in wrestling?Potential variables:
- [ ] Weight
- [ ] Age
- [ ] Experience
- [ ] First score
- [ ] Takedown rate
- [ ] Scoring frequency
- [ ] Match duration
- [ ] Tournament experience
- [ ] Style
- [ ] Opponent qualityAnalysis:
- [ ] EDA
- [ ] Visualisation
- [ ] Statistical modelling
- [ ] Prediction
- [ ] Confounding
- [ ] Causal questions
- [ ] Heterogeneous effects
- [ ] Unexpected findings
- [ ] Limitations

---

#
16. Interview Preparation

## Technical
- [ ] Python coding
- [ ] pandas
- [ ] SQL
- [ ] Statistics
- [ ] Probability
- [ ] A/B testing
- [ ] Regression
- [ ] ML
- [ ] Causal inference

## Product
- [ ] Product metrics
- [ ] Experiment design
- [ ] Product sense
- [ ] Metric diagnosis
- [ ] Feature evaluation
- [ ] Trade-offs

## Case Studies
- [ ] Investigate metric decline
- [ ] Design an experiment
- [ ] Evaluate a recommendation system
- [ ] Diagnose an unexpected result
- [ ] Choose KPIs
- [ ] Analyse a product launch
- [ ] Explain an experiment to a PM

## Communication
- [ ] Explain an MSc project
- [ ] Explain a statistical model
- [ ] Explain causal inference
- [ ] Explain an A/B test
- [ ] Explain an ML model
- [ ] Explain a surprising result
- [ ] Defend analytical decisions

---

#
17. The "Beast Mode" StandardDon't mark a topic complete just because you have watched a lecture.For each major topic, aim to be able to:
- [ ] Explain it without notes
- [ ] Explain why it works
- [ ] Implement it from scratch at least once
- [ ] Use the relevant Python/SQL tools
- [ ] Interpret the output
- [ ] Identify common mistakes
- [ ] Know when NOT to use it
- [ ] Apply it to a real dataset
- [ ] Explain the result to a non-technical person

---

#
18. Final Product DS CapabilityEventually I want to be able to give you a completely unfamiliar problem such as:

> "Spotify introduced a new recommendation algorithm and listening time increased by 5%. Should they roll it out?"And you should naturally think:
> 1. [ ] What exactly changed?
> 2. [ ] What outcome are we trying to improve?
> 3. [ ] What is the unit of analysis?
> 4. [ ] What is the appropriate metric?
> 5. [ ] What are the guardrail metrics?
> 6. [ ] Is this causal or merely correlational?
> 7. [ ] Can we randomise?
> 8. [ ] How should we design the experiment?
> 9. [ ] How much data do we need?
> 10. [ ] What assumptions are we making?
> 11. [ ] What does the result actually tell us?
> 12. [ ] Is the effect practically meaningful?
> 13. [ ] Does the effect differ across users?
> 14. [ ] Could there be unintended consequences?
> 15. [ ] Should we ship?
> 16. [ ] What should we investigate next?
> 17. [ ] Can I communicate the answer clearly?

---

# Current Status

## Today
- [x] Binary search- [] Binary search with duplicates / first occurrence
- [ ] Refresh core Python
- [ ] Begin pandas
- [ ] Work through first real dataset

## Current Priority Order
1. [ ] Python
2. [ ] pandas / NumPy / visualisation
3. [ ] Probability & statistics refresh
4. [ ] SQL
5. [ ] Regression
6. [ ] A/B testing
7. [ ] Causal inference
8. [ ] Machine learning
9. [ ] Product analytics
10. [ ] Data engineering literacy
11. [ ] Portfolio projects
12. [ ] Interviews

---

# Philosophy

> Don't optimise for knowing the most techniques. Optimise for being able to answer interesting questions.The ultimate skill is:\*\*Question → Data → Model → Evidence → Causal reasoning → Decision → Communication\*\*And the goal isn't to become someone who knows every Python library.The goal is to become the person in the room who can say:

> \*\*"Interesting. But what is actually going on here?"\*\*and then figure it out.** &#x20;
