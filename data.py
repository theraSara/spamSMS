import kagglehub


# Kaggle Link: https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset?resource=download

# Download latest version
path = kagglehub.dataset_download("uciml/sms-spam-collection-dataset")

print("Path to dataset files:", path)

# Directory Output: /Users/vanilla/.cache/kagglehub/datasets/uciml/sms-spam-collection-dataset/versions/1