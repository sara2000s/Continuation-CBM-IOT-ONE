import time
import pandas as pd
import os # برای کار با مسیرهای فایل

# تابع شبیه سازی تراکنش در بلاکچین (بدون تغییر)
def validate_transaction(transaction_data):
    """
    این تابع فرآیند اعتبارسنجی تراکنش در بلاکچین انجام می کند.
    transaction_data می تواند هر داده ای باشد که نماینده یک تراکنش است.
    """
    #   زمان لازم برای اعتبارسنجی تراکنش
   
    time.sleep(0.5)
    # در یک سناریوی واقعی، این تابع با یک نود بلاکچین تعامل می کند،
    # تراکنش را ارسال می کند و منتظر تایید می ماند.
    # print(f"داده تراکنش شبیه سازی شده: {transaction_data}") # می توانید این خط را برای مشاهده داده ها فعال کنید

# مسیر فایل های CSV
file_path_diabetes = r"D:\سارا\ترم 3 دانشگاه قم\فصل سوم و چهارم پایان نامه 1\diabetes.csv"
file_path_mitbih = r"D:\سارا\ترم 3 دانشگاه قم\فصل سوم و چهارم پایان نامه 1\mitbih_test.csv"

# لیست مسیر فایل ها برای پردازش
file_paths = [file_path_diabetes, file_path_mitbih]

# پردازش هر فایل
for file_path in file_paths:
    print(f"--- شروع پردازش فایل: {os.path.basename(file_path)} ---") # نمایش نام فایل

    # بررسی وجود فایل
    if not os.path.exists(file_path):
        print(f"خطا: فایل در مسیر مشخص شده یافت نشد: {file_path}")
        continue # رفتن به فایل بعدی

    try:
        # خواندن داده ها از فایل CSV با استفاده از pandas
        # فقط ردیف اول را برای شبیه سازی یک تراکنش می خوانیم
        # اگر می خواهید تمام ردیف ها را پردازش کنید، باید حلقه دیگری اضافه کنید
        # و محاسبات latency را به ازای هر ردیف یا به صورت میانگین انجام دهید.
        df = pd.read_csv(file_path, nrows=1) # خواندن فقط ردیف اول

        if df.empty:
            print(f"فایل {os.path.basename(file_path)} خالی است یا فقط هدر دارد.")
            continue

        # تبدیل ردیف اول به دیکشنری به عنوان داده تراکنش
        # (یا می توانید از فرمت دیگری استفاده کنید)
        transaction_data = df.iloc[0].to_dict()


        # زمان شروع قبل از تراکنش
        start_time = time.time()

        # شبیه سازی ارسال و اعتبارسنجی تراکنش
        validate_transaction(transaction_data)

        # زمان پایان پس از اعتبارسنجی تراکنش
        end_time = time.time()

        # محاسبه تاخیر (latency)
        latency = end_time - start_time
        print(f"تاخیر تراکنش (با استفاده از ردیف اول): {latency:.4f} ثانیه") # نمایش تاخیر با 4 رقم اعشار

    except pd.errors.EmptyDataError:
        print(f"خطا: فایل {os.path.basename(file_path)} خالی است.")
    except FileNotFoundError:
        # این حالت توسط os.path.exists پوشش داده شده است، اما برای اطمینان بیشتر
        print(f"خطا: فایل در مسیر مشخص شده یافت نشد: {file_path}")
    except Exception as e:
        print(f"خطای غیرمنتظره در هنگام پردازش فایل {os.path.basename(file_path)}: {e}")

    print(f"--- پایان پردازش فایل: {os.path.basename(file_path)} ---\n")