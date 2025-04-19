import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
import os # برای بررسی وجود فایل

# تعریف مسیر فایل‌ها
diabetes_file_path = 'D:\سارا\ترم 3 دانشگاه قم\فصل سوم و چهارم پایان نامه 1\diabetes.csv'
mitbih_file_path = 'D:\سارا\ترم 3 دانشگاه قم\فصل سوم و چهارم پایان نامه 1\mitbih_test.csv'

# --- پردازش فایل diabetes.csv ---
print(f"Processing file: {diabetes_file_path}")
if not os.path.exists(diabetes_file_path):
    print(f"Error: File not found at {diabetes_file_path}")
else:
    try:
        # بارگذاری داده‌ها از فایل diabetes.csv
        df_diabetes = pd.read_csv(diabetes_file_path)

        # فرض می‌کنیم ستون آخر متغیر هدف (y) و بقیه ویژگی‌ها (X) هستند.
        # لطفاً اگر ساختار فایل شما متفاوت است، این قسمت را تنظیم کنید.
        X_diabetes = df_diabetes.iloc[:, :-1]
        y_diabetes = df_diabetes.iloc[:, -1]

        # اطمینان از اینکه تعداد نمونه‌ها برای cross-validation کافی است
        if len(y_diabetes) < 10:
            print(f"Not enough samples ({len(y_diabetes)}) in {diabetes_file_path} for 10-fold cross-validation.")
        else:
            # تعریف مدل Random Forest
            # افزودن random_state برای تکرارپذیری نتایج
            model_diabetes = RandomForestClassifier(random_state=42)

            # اجرای 10-fold cross-validation
            print("Performing 10-fold cross-validation for diabetes dataset...")
            cv_scores_diabetes = cross_val_score(model_diabetes, X_diabetes, y_diabetes, cv=10, scoring='accuracy')

            # نمایش نتایج
            print(f"Cross-Validation Scores (diabetes): {cv_scores_diabetes}")
            print(f"Mean Accuracy (diabetes): {cv_scores_diabetes.mean():.4f}")
            print("-" * 30) # خط جداکننده برای خوانایی بیشتر

    except pd.errors.EmptyDataError:
        print(f"Error: The file {diabetes_file_path} is empty.")
    except pd.errors.ParserError:
        print(f"Error: Could not parse the file {diabetes_file_path}. Check the file format.")
    except Exception as e:
        print(f"An error occurred while processing {diabetes_file_path}: {e}")


# --- پردازش فایل mitbih_test.csv ---
print(f"Processing file: {mitbih_file_path}")
if not os.path.exists(mitbih_file_path):
    print(f"Error: File not found at {mitbih_file_path}")
else:
    try:
        # بارگذاری داده‌ها از فایل mitbih_test.csv
        df_mitbih = pd.read_csv(mitbih_file_path)

        # فرض می‌کنیم ستون آخر متغیر هدف (y) و بقیه ویژگی‌ها (X) هستند.
        # لطفاً اگر ساختار فایل شما متفاوت است، این قسمت را تنظیم کنید.
        X_mitbih = df_mitbih.iloc[:, :-1]
        y_mitbih = df_mitbih.iloc[:, -1]

        # اطمینان از اینکه تعداد نمونه‌ها برای cross-validation کافی است
        if len(y_mitbih) < 10:
             print(f"Not enough samples ({len(y_mitbih)}) in {mitbih_file_path} for 10-fold cross-validation.")
        else:
            # تعریف مدل Random Forest
            # افزودن random_state برای تکرارپذیری نتایج
            model_mitbih = RandomForestClassifier(random_state=42)

            # اجرای 10-fold cross-validation
            print("Performing 10-fold cross-validation for MITBIH test dataset...")
            # توجه: داده‌های MITBIH ممکن است بزرگ باشند، cross-validation ممکن است زمان ببرد.
            cv_scores_mitbih = cross_val_score(model_mitbih, X_mitbih, y_mitbih, cv=10, scoring='accuracy')

            # نمایش نتایج
            print(f"Cross-Validation Scores (MITBIH test): {cv_scores_mitbih}")
            print(f"Mean Accuracy (MITBIH test): {cv_scores_mitbih.mean():.4f}")
            print("-" * 30) # خط جداکننده برای خوانایی بیشتر

    except pd.errors.EmptyDataError:
        print(f"Error: The file {mitbih_file_path} is empty.")
    except pd.errors.ParserError:
         print(f"Error: Could not parse the file {mitbih_file_path}. Check the file format.")
    except Exception as e:
        print(f"An error occurred while processing {mitbih_file_path}: {e}")

print("Finished processing both files.")