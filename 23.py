import pandas as pd  
from sklearn.model_selection import train_test_split  
from sklearn.ensemble import RandomForestClassifier  
from sklearn.metrics import (  
    accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix, classification_report  
)  

# --- مقادیر زیر را با توجه به فایل‌های خود تنظیم کنید ---  
TARGET_COLUMN_DIABETES = 'Outcome'  
TARGET_COLUMN_MITBIH = 187  # <--- این مقدار را بسته به فایل تغییر دهید  
FILE_PATH_DIABETES = r'D:\سارا\ترم 3 دانشگاه قم\فصل سوم و چهارم پایان نامه 1\diabetes.csv'  
FILE_PATH_MITBIH = r'D:\سارا\ترم 3 دانشگاه قم\فصل سوم و چهارم پایان نامه 1\mitbih_test.csv'  

files_info = [  
    {'path': FILE_PATH_DIABETES, 'target': TARGET_COLUMN_DIABETES, 'has_header': True},  
    {'path': FILE_PATH_MITBIH, 'target': TARGET_COLUMN_MITBIH, 'has_header': False}  
]  

for file_info in files_info:  
    file_path = file_info['path']  
    target_col = file_info['target']  
    has_header = file_info['has_header']  

    print("\n-----------------------------------")  
    print(f"Processing: {file_path.split('\\')[-1]}")  
    
    try:  
        # خواندن فایل CSV با یا بدون هدر  
        df = pd.read_csv(file_path, header=0 if has_header else None)  
        print("Columns:", df.columns.tolist())  

        if target_col not in df.columns:  
            print(f"Error: Target column '{target_col}' not found in {file_path}")  
            print(f"Available columns are: {df.columns.tolist()}")  
            continue  

        X = df.drop(columns=[target_col])  
        y = df[target_col]  

        if not pd.api.types.is_numeric_dtype(y):  
            try:  
                y = pd.to_numeric(y)  
            except ValueError:  
                print(f"Warning: Target column '{target_col}' in {file_path} is not numeric and could not be converted. Skipping this file.")  
                continue  

        X_train, X_test, y_train, y_test = train_test_split(  
            X, y, test_size=0.2, random_state=42, stratify=y  
        )  

        model = RandomForestClassifier(random_state=42)  
        model.fit(X_train, y_train)  
        y_pred = model.predict(X_test)  

        num_classes = len(model.classes_)  
        is_binary = num_classes == 2  

        if is_binary:  
            y_proba = model.predict_proba(X_test)[:, 1]  
        else:  
            y_proba = None  

        acc = accuracy_score(y_test, y_pred)  
        prec = precision_score(y_test, y_pred, average='binary' if is_binary else 'macro', zero_division=0)  
        recall = recall_score(y_test, y_pred, average='binary' if is_binary else 'macro', zero_division=0)  
        f1 = f1_score(y_test, y_pred, average='binary' if is_binary else 'macro', zero_division=0)  

        print(f"Accuracy:  {acc:.4f}")  
        print(f"Precision: {prec:.4f}")  
        print(f"Recall:    {recall:.4f}")  
        print(f"F1 Score:  {f1:.4f}")  

        if y_proba is not None:  
            roc_auc = roc_auc_score(y_test, y_proba)  
            print(f"AUC-ROC:  {roc_auc:.4f}")  
        else:  
            print("AUC-ROC:   Only for binary classification.")  

        print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))  
        print("\nClassification Report:\n", classification_report(y_test, y_pred))  

    except Exception as e:  
        print(f"An error occurred while processing {file_path}: {e}")  