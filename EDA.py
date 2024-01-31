import pandas as pd
from ydata_profiling import ProfileReport

# Load your dataset
df = pd.read_csv('/Users/daras/PycharmProjects/CSI6900_winlogroberta/project_parsed/Windows.log_structured.csv')

report = ProfileReport(df, minimal=True)
#report.to_notebook_iframe()
report.to_file("windows_event_log_data.html")