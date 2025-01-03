import numpy as np
import pandas as pd
  
def get_data():
    print("Loading custom dataset from the data directory.")
    ds = pd.read_csv("data/dataset.tsv", sep='\t', index_col="ID").reset_index(drop=True)
    print(ds.describe)
    label_name = "LumP"
    categorical_attribute_names = ["gender", "history_of_neoadjuvant_treatment", "primary_lymph_node_presentation_assessment", "lymphovascular_invasion_present", "neoplasm_histologic_grade", "history_non_muscle_invasive_blca"]
    y = ds.loc[:, label_name]
    X = ds.loc[:, ds.columns != label_name]
    
    categorical_mask = np.array([c in categorical_attribute_names for c in X.columns], dtype=bool)
    
    return X, y, categorical_mask, X.columns.to_list()

if __name__ == "__main__":
    df, y, mask, attribute_names = get_data()
    
    print(df)
    print(mask)
    print(attribute_names)
