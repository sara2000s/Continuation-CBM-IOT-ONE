import pandas as pd  
import os  
import time  

# مسیر فایل‌ها  
diabetes_file_path = r'D:\سارا\ترم 3 دانشگاه قم\فصل سوم و چهارم پایان نامه 1\diabetes.csv'  
mitbih_file_path = r'D:\سارا\ترم 3 دانشگاه قم\فصل سوم و چهارم پایان نامه 1\mitbih_test.csv'  

# داده تقلبی برای شبیه‌سازی تراکنش مخرب (می‌تواند هر دیکشنری یا ساختار دلخواه باشد)  
fraudulent_data = {"sender": "attacker", "receiver": "victim", "amount": 0}  

class BlockchainNetwork:  
    def __init__(self):  
        self.processed_transactions = 0  

    def process_transaction(self, transaction):  
        # شبیه‌سازی زمان پردازش یک تراکنش (مثلاً 0.0001ثانیه)  
        time.sleep(0.0001)  
        self.processed_transactions += 1  


def simulate_sybil_attack(blockchain_network, fake_nodes_count):  
    print(f"Simulating Sybil attack with {fake_nodes_count} fake identities...")  
    for i in range(fake_nodes_count):  
        # هر شبیه‌سازی تراکنش از یک هویت جعلی (مثلاً تراکنش تقلبی)  
        blockchain_network.process_transaction({**fraudulent_data, "node_id": f"fake_node_{i}"})  
    print(f"Sybil Attack Simulation Complete: {blockchain_network.processed_transactions} transactions processed.\n")  

def simulate_dos_attack(blockchain_network, attack_frequency):  
    print(f"Simulating DoS attack with {attack_frequency} rapid transactions...")  
    for _ in range(attack_frequency):  
        blockchain_network.process_transaction(fraudulent_data)  
    print(f"DoS Attack Simulation Complete: {blockchain_network.processed_transactions} transactions processed.\n")  


def process_file(file_path):  
    if not os.path.exists(file_path):  
        print(f"Error: File not found at {file_path}")  
        return  

    try:  
        df = pd.read_csv(file_path)  
        devices_count = len(df)  
        if devices_count == 0:  
            print(f"The file {file_path} is empty.")  
            return  

        print(f"Processing file: {file_path} - Devices: {devices_count}")  

        network = BlockchainNetwork()  

        # شبیه‌سازی حمله Sybil به اندازه تعداد دستگاه‌های موجود در فایل  
        simulate_sybil_attack(network, fake_nodes_count=devices_count)  

        # شبیه‌سازی حمله DoS با تعداد مشخص (مثلا 10000 تراکنش تقلبی)  
        simulate_dos_attack(network, attack_frequency=10000)  

    except Exception as e:  
        print(f"Error processing file {file_path}: {e}")  


# اجرای شبیه‌سازی‌ها روی دو فایل  
process_file(diabetes_file_path)  
process_file(mitbih_file_path)  