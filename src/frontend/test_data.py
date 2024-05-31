import pandas as pd
import numpy as np

columns = ['Arrival date', 'Patient ID', 'Doctor', 'Tasks', 'Classification', 'Status']
data = pd.DataFrame(columns=columns)
dates = [
    pd.Timestamp("2024-06-01"),
    pd.Timestamp("2024-06-02"),
    pd.Timestamp("2024-06-02"),
    pd.Timestamp("2024-06-02"),
    pd.Timestamp("2024-06-02"),
    pd.Timestamp("2024-06-02"),
    pd.Timestamp("2024-06-02"),
    pd.Timestamp("2024-06-02"),
    pd.Timestamp("2024-06-03"),
    pd.Timestamp("2024-06-03"),
    pd.Timestamp("2024-06-03"),
    pd.Timestamp("2024-06-03"),
    pd.Timestamp("2024-06-03"),
    pd.Timestamp("2024-06-03"),
    pd.Timestamp("2024-06-03"),
    pd.Timestamp("2024-06-03"),
]
data['Arrival date'] = dates
data['Patient ID'] = np.random.randint(100000, 999999, size=len(data))
data['Doctor'] = np.random.choice(['Dr. Smith', 'Dr. Johnson', 'Dr. Brown', 'Dr. Wilson'], size=len(data))
data['Tasks'] = np.random.choice(['Blood test', 'Scans'], size=len(data))
data['Classification'] = np.random.choice(['Normal', 'Abnormal'], size=len(data))
data['Status'] = np.random.choice(['Pending'], size=len(data))