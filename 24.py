import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression # مدل برای دسته‌بندی دوگانه (مثل دیابت)
from sklearn.tree import DecisionTreeClassifier # مدل برای دسته‌بندی چندگانه (مثل mitbih)
from sklearn.metrics import confusion_matrix

# مسیر فایل‌ها
diabetes_file_path = 'D:/سارا/ترم 3 دانشگاه قم/فصل سوم و چهارم پایان نامه 1/diabetes.csv'
mitbih_file_path = 'D:/سارا/ترم 3 دانشگاه قم/فصل سوم و چهارم پایان نامه 1/mitbih_test.csv'

# --- پردازش فایل diabetes.csv ---
print("Processing diabetes.csv...")
try:
    # بارگذاری داده‌ها
    df_diabetes = pd.read_csv(diabetes_file_path)

    # جداسازی ویژگی‌ها (X) و برچسب (y)
    # فرض بر این است که ستون 'Outcome' ستون هدف است. اگر نام ستون فرق می‌کند، آن را جایگزین کنید.
    if 'Outcome' in df_diabetes.columns:
         X_diabetes = df_diabetes.drop('Outcome', axis=1)
         y_diabetes = df_diabetes['Outcome']
    else:
         # در صورت عدم وجود ستون Outcome، فرض می‌کنیم ستون آخر هدف است
         print("Warning: 'Outcome' column not found in diabetes.csv. Assuming the last column is the target.")
         X_diabetes = df_diabetes.iloc[:, :-1]
         y_diabetes = df_diabetes.iloc[:, -1]


    # تقسیم داده‌ها به مجموعه آموزشی و آزمایشی
    X_train_diabetes, X_test_diabetes, y_train_diabetes, y_test_diabetes = train_test_split(
        X_diabetes, y_diabetes, test_size=0.2, random_state=42, stratify=y_diabetes # stratify برای حفظ نسبت کلاس‌ها
    )

    # آموزش یک مدل دسته‌بندی (رگرسیون لجستیک برای دسته‌بندی دوگانه)
    model_diabetes = LogisticRegression(max_iter=200) # max_iter را برای همگرایی بیشتر کردیم
    model_diabetes.fit(X_train_diabetes, y_train_diabetes)

    # پیش‌بینی روی داده‌های آزمایشی
    y_pred_diabetes = model_diabetes.predict(X_test_diabetes)

    # محاسبه ماتریس درهم‌ریختگی
    cm_diabetes = confusion_matrix(y_test_diabetes, y_pred_diabetes)

    # پلات ماتریس درهم‌ریختگی با استفاده از کد اصلی شما
    plt.figure(figsize=(6, 5)) # اندازه شکل را تنظیم کنید
    sns.heatmap(cm_diabetes, annot=True, fmt='d', cmap='Blues',
                xticklabels=['Predicted Negative', 'Predicted Positive'],
                yticklabels=['Actual Negative', 'Actual Positive'])
    plt.ylabel('Actual Label')
    plt.xlabel('Predicted Label')
    plt.title('Confusion Matrix - Diabetes Prediction')
    plt.show()

except FileNotFoundError:
    print(f"Error: The file {diabetes_file_path} was not found.")
except Exception as e:
    print(f"An error occurred while processing {diabetes_file_path}: {e}")

print("-" * 30) # جداکننده خروجی‌ها

# --- پردازش فایل mitbih_test.csv ---
print("Processing mitbih_test.csv...")
try:
    # بارگذاری داده‌ها (اغلب این فایل هدر ندارد)
    df_mitbih = pd.read_csv(mitbih_file_path, header=None)

    # جداسازی ویژگی‌ها (X) و برچسب (y)
    # فرض بر این است که ستون آخر (بدون هدر، ستون با ایندکس N-1) ستون هدف است.
    X_mitbih = df_mitbih.iloc[:, :-1]
    y_mitbih = df_mitbih.iloc[:, -1]

    # نکته مهم: mitbih_test.csv معمولاً مجموعه آزمایشی است.
    # استاندارد این است که مدل را روی mitbih_train.csv آموزش داد.
    # برای نمایش ماتریس درهم‌ریختگی با فایل موجود شما،
    # همین مجموعه آزمایشی را دوباره به دو قسمت آموزشی و آزمایشی تقسیم می‌کنیم.
    # این روش برای ارزیابی نهایی عملکرد مدل مناسب نیست!
    print("Note: For demonstration, splitting the provided mitbih_test.csv into train/test.")

    # تقسیم داده‌ها به مجموعه آموزشی و آزمایشی
    X_train_mitbih, X_test_mitbih, y_train_mitbih, y_test_mitbih = train_test_split(
        X_mitbih, y_mitbih, test_size=0.3, random_state=42, stratify=y_mitbih # stratify برای حفظ نسبت کلاس‌ها
    )

    # آموزش یک مدل دسته‌بندی (درخت تصمیم برای دسته‌بندی چندگانه)
    model_mitbih = DecisionTreeClassifier(random_state=42)
    model_mitbih.fit(X_train_mitbih, y_train_mitbih)

    # پیش‌بینی روی داده‌های آزمایشی
    y_pred_mitbih = model_mitbih.predict(X_test_mitbih)

    # محاسبه ماتریس درهم‌ریختگی
    cm_mitbih = confusion_matrix(y_test_mitbih, y_pred_mitbih)
# گرفتن برچسب‌های کلاس‌های منحصر به فرد برای نمایش در محورها
    # این دیتاست چند کلاسه است، بنابراین برچسب‌ها عددی هستند (معمولاً 0, 1, 2, 3, 4)
    class_labels_mitbih = sorted(y_test_mitbih.unique())
    # تبدیل برچسب‌ها به رشته برای نمایش در پلات
    class_labels_str = [str(int(label)) for label in class_labels_mitbih]

    # پلات ماتریس درهم‌ریختگی با استفاده از کد اصلی شما
    plt.figure(figsize=(8, 7)) # اندازه شکل را برای تعداد کلاس‌های بیشتر تنظیم کنید
    sns.heatmap(cm_mitbih, annot=True, fmt='d', cmap='Blues',
                xticklabels=class_labels_str,
                yticklabels=class_labels_str)
    plt.ylabel('Actual Label')
    plt.xlabel('Predicted Label')
    plt.title('Confusion Matrix - MITBIH Arrhythmia Prediction')
    plt.show()

except FileNotFoundError:
    print(f"Error: The file {mitbih_file_path} was not found.")
except Exception as e:
    print(f"An error occurred while processing {mitbih_file_path}: {e}")
