import pandas as pd
import time

# Path to your CSV file
file_path = r'D:\سارا\ترم 3 دانشگاه قم\فصل سوم و چهارم پایان نامه 1\patientMonitoring.csv'

#  blockchain function for storing/validating data
def blockchain_transaction(data_row):
    #  processing time for blockchain transaction
    time.sleep(0.5)  # Placeholder for actual blockchain processing time
    print(f"Data committed to blockchain: {data_row.to_dict()}")

try:
    # Load IoMT data from CSV
    print("Loading IoMT data...")
    data = pd.read_csv(file_path)

    # Check if the CSV contains data
    if data.empty:
        print("Error: The CSV file is empty.")
    else:
        print("IoMT data loaded successfully.")
        print(f"Columns: {data.columns.tolist()}")

        # Process each row of data
        for index, row in data.iterrows():
            print(f"\nProcessing row {index + 1}...")
            start_time = time.time()  # Start time before transaction

            # Send data to blockchain (simulated)
            blockchain_transaction(row)

            end_time = time.time()  # End time after transaction
            latency = end_time - start_time  # Calculate latency

            print(f"Transaction latency for row {index + 1}: {latency:.4f} seconds")

except FileNotFoundError:
    print(f"Error: File not found at path {file_path}")
except pd.errors.EmptyDataError:
    print("Error: The CSV file is either empty or corrupted.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
