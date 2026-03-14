import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(
        lambda x: x['salary'] if x['employee_id'] % 2 != 0 and not x['name'].startswith('M') else 0, 
        axis=1
    )
    
    # Return the result sorted by employee_id as per LeetCode requirements
    return employees[['employee_id', 'bonus']].sort_values(by='employee_id')