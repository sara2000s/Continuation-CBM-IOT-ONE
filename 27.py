import pandas as pd
import os
import math # برای گرد کردن زمان به سمت بالا

# ---پارامترها ---
simulated_gas_price_per_transaction = 0.01  # هزینه  برای هر تراکنش (ردیف)
simulated_transactions_per_second = 20.0    # تعداد تراکنش (ردیف)  که در هر ثانیه پردازش می شود

# محاسبه هزینه در هر ثانیه
# این مقدار برای همه فایل ها یکسان است چون پارامترها ثابت هستند
cost_per_second = simulated_gas_price_per_transaction * simulated_transactions_per_second
print(f"نرخ هزینه : {cost_per_second:.4f} واحد در هر ثانیه")
print("-" * 40) # خط جدا کننده

# --- مسیر فایل های CSV ---
file_path_diabetes = r"D:\سارا\ترم 3 دانشگاه قم\فصل سوم و چهارم پایان نامه 1\diabetes.csv"
file_path_mitbih = r"D:\سارا\ترم 3 دانشگاه قم\فصل سوم و چهارم پایان نامه 1\mitbih_test.csv"

# لیست مسیر فایل ها برای پردازش
file_paths = [file_path_diabetes, file_path_mitbih]

# --- پردازش هر فایل ---
for file_path in file_paths:
    file_name = os.path.basename(file_path)
    print(f"--- شروع پردازش فایل: {file_name} ---")

    # بررسی وجود فایل
    if not os.path.exists(file_path):
        print(f"خطا: فایل در مسیر مشخص شده یافت نشد: {file_path}")
        print(f"--- پایان پردازش فایل: {file_name} ---\n")
        continue # رفتن به فایل بعدی

    try:
        # خواندن کل فایل CSV برای شمارش تعداد ردیف ها
        df = pd.read_csv(file_path)

        # دریافت تعداد کل ردیف ها (تراکنش ها)
        total_transactions = len(df)

        if total_transactions == 0:
            print(f"فایل {file_name} خالی است یا هیچ ردیف داده ای ندارد.")
        else:
            # محاسبه زمان تخمینی پردازش فایل (به ثانیه)
            # اگر transactions_per_second صفر باشد از تقسیم بر صفر جلوگیری می کنیم
            if simulated_transactions_per_second > 0:
                estimated_processing_time_seconds = total_transactions / simulated_transactions_per_second
            else:
                estimated_processing_time_seconds = float('inf') # زمان بی نهایت اگر سرعت پردازش صفر باشد

            # روش اول: (تعداد تراکنش * هزینه هر تراکنش)
            total_simulated_cost_method1 = total_transactions * simulated_gas_price_per_transaction
            # روش دوم: (زمان پردازش * هزینه در ثانیه) - باید نتیجه یکسانی بدهد
            total_simulated_cost_method2 = estimated_processing_time_seconds * cost_per_second

            print(f"تعداد کل ردیف  (تراکنش ): {total_transactions}")
            print(f"سرعت پردازش: {simulated_transactions_per_second} تراکنش در ثانیه")
            print(f"زمان تخمینی پردازش فایل: {estimated_processing_time_seconds:.2f} ثانیه")
            # نمایش هزینه کل (هر دو روش باید یکسان باشند، یکی را نمایش می دهیم)
            print(f"هزینه کل  برای پردازش فایل: {total_simulated_cost_method1:.6f} واحد")
            # می توانید تایید کنید که هر دو روش یکسان هستند (با خطای گرد کردن جزئی ممکن است متفاوت باشند)
            # print(f"Total Cost (Method 2): {total_simulated_cost_method2:.6f}")


    except pd.errors.EmptyDataError:
        print(f"خطا: فایل {file_name} خالی است.")
    except FileNotFoundError:
        print(f"خطا: فایل در مسیر مشخص شده یافت نشد: {file_path}")
    except Exception as e:
        print(f"خطای غیرمنتظره در هنگام پردازش فایل {file_name}: {e}")

    print(f"--- پایان پردازش فایل: {file_name} ---\n")