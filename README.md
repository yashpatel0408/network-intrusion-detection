# Network Intrusion Detection using Machine Learning

Machine learning project to classify network connections as Normal or Attack using the NSL-KDD dataset.

## Dataset
NSL-KDD (KDDTrain+ and KDDTest+), 41 features per connection.
The test set contains attack types that are not present in the training set.

## Approach
1. EDA: attack types, protocol type and connection flag vs attack
2. Binary label: normal = 0, any attack = 1
3. One-hot encoding for protocol_type, service and flag
4. Models: Decision Tree and Random Forest
5. Evaluation on the separate KDDTest+ set: precision, recall, F1, confusion matrix

## Results
- Best model: <naam daalo>
- Accuracy: <value daalo>
- Attack F1: <value daalo>

## Key Insights
- <Cell 6, 7, 12 ke graphs dekh ke 2-3 lines likh>

## How to run
pip install -r requirements.txt
cd src
python train_model.py
python predict.py