from glassdoor_scraper import get_jobs
import pandas as pd

path = 'C:/Users/prash/Desktop/data_science_salary_estimator/chromedriver'
df = get_jobs('data scientist', 1000, False, path, 5)

df.to_csv('raw_data.csv', index=False)