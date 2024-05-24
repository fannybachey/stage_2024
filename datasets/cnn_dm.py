from datasets import load_dataset

# Load the CNN/DailyMail dataset with a specific configuration version
dataset = load_dataset("cnn_dailymail", "3.0.0")

# Print the keys of the dataset to see the available splits
print("Dataset splits:", dataset.keys())

# Get information about the dataset
print("Dataset information:", dataset)


# Access the train split
train_data = dataset['train']

# Get the number of samples in the train split
print(f"Number of training samples: {len(train_data)}")

# Get the column names
print(f"Column names: {train_data.column_names}")

# Example: print the article and its summary
print("Article:", train_data[0]['article'])
print("Summary:", train_data[0]['highlights'])
