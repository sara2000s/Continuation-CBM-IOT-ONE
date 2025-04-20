import pandas as pd  
import os  

diabetes_file_path = r'D:\سارا\ترم 3 دانشگاه قم\فصل سوم و چهارم پایان نامه 1\diabetes.csv'  
mitbih_file_path = r'D:\سارا\ترم 3 دانشگاه قم\فصل سوم و چهارم پایان نامه 1\mitbih_test.csv'  

def test_scalability(devices_count, transactions_per_device=10, time_per_transaction=0.001):  
    total_transactions = devices_count * transactions_per_device  
    total_time = total_transactions * time_per_transaction  
    return total_time  

def process_file(file_path, devices_counts=None, transactions_per_device=2, time_per_transaction=0.0005):  
    if not os.path.exists(file_path):  
        print(f"Error: File not found at {file_path}")  
        return  
    
    try:  
        df = pd.read_csv(file_path)  
        total_devices = len(df)  
        if total_devices == 0:  
            print(f"The file {file_path} is empty.")  
            return  

        # اگر لیست تعداد دستگاه ارائه نشده، استفاده از تعداد واقعی رکوردها و کمی اعداد پایین‌تر برای تست مقیاس پذیری  
        if devices_counts is None:  
            # مثلا مقادیر نماینده = بخش‌هایی از تعداد کل دستگاه‌ها (10%, 25%, 50%, 100%)  
            devices_counts = sorted(set([  
                max(1, int(total_devices * 0.1)),  
                max(1, int(total_devices * 0.25)),  
                max(1, int(total_devices * 0.5)),  
                total_devices  
            ]))  

        print(f"Processing file: {file_path}")  
        print(f"Total devices (rows): {total_devices}")  
        print(f"Transactions per device: {transactions_per_device}")  
        print(f"Time per transaction: {time_per_transaction} seconds\n")  

        print(f"{'Devices Count':>15} | {'Estimated Validation Time (s)':>30}")  
        print("-" * 50)  
        for devices_count in devices_counts:  
            # محدود کردن حد بالایی به تعداد کل دستگاه‌ها  
            devices_count_capped = min(devices_count, total_devices)  
            time_taken = test_scalability(devices_count_capped, transactions_per_device, time_per_transaction)  
            print(f"{devices_count_capped:>15} | {time_taken:>30.6f}")  

        print("\n" + "="*50 + "\n")  

    except Exception as e:  
        print(f"Error processing file {file_path}: {e}")  

# نمونه مقادیر تعداد دستگاه برای تست مقیاس پذیری (شما می‌توانید این لیست را بر حسب نیاز تغییر دهید)  
devices_test_list = [10, 50, 100, 500, 1000]  

# اجرای کد روی هر دو فایل با مقیاس پذیری:  
process_file(diabetes_file_path, devices_counts=devices_test_list)  
process_file(mitbih_file_path, devices_counts=devices_test_list)  