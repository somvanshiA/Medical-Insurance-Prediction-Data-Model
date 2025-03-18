# Medical-Insurance-Prediction-Data-Model


## Overview
This dataset contains medical insurance data that can be used for predictive modeling and exploratory data analysis. It includes key features of individuals along with their respective insurance charges. The primary goal is to develop models that predict insurance costs based on these features.

## Dataset Description
The dataset includes records with the following attributes:

- **Age:** Age of the policyholder.
- **Sex:** Gender of the policyholder.
- **BMI:** Body Mass Index (a measure of body fat based on height and weight).
- **Children:** Number of children covered under the policy.
- **Smoker:** Whether the policyholder is a smoker (values: `yes` or `no`).
- **Region:** Geographical region of the policyholder (e.g., `northwest`, `northeast`, `southwest`, `southeast`).
- **Charges:** Medical insurance charges billed to the policyholder (target variable).

## File Structure
- **insurance.csv:** CSV file containing the dataset.
- **medical_insurance.csv
- 
- **README.md:** This file.

## How to Use the Dataset

### Loading the Data
You can load the dataset using Python with Pandas:

```python
import pandas as pd

# Load the dataset
df = pd.read_csv('insurance.csv')
print(df.head())
