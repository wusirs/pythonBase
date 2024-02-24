import pandas as pd


def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    result_df = employee[employee['salary'] > employee['managerId'].map(employee.set_index('id')['salary'])]
    result_df = result_df[['name']].rename(columns={'name': 'Employee'})
    return result_df


json_string: list[dict[str, str]] = [{'id': '1', 'name': 'joe', 'salary': '7200', 'managerId': '3'},
                                     {'id': '3', 'name': 'joe', 'salary': '7000', 'managerId': None}]
# print(find_employees(pd.DataFrame(json_string)))
frame = pd.DataFrame(json_string)
# print(frame['managerId'].map(frame.set_index('id')['salary']))
