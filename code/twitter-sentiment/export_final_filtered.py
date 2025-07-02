# export_final_filtered.py
def export_final_filtered(df):
    df.to_csv('filtered_final_dataset.csv', index=False)
