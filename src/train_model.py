import joblib
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, f1_score

from data_preprocessing import load_data, clean_data, encode_data

TRAIN_PATH = '../data/KDDTrain+.txt'
TEST_PATH = '../data/KDDTest+.txt'
MODEL_PATH = '../models/ids_model.pkl'


def main():
    # data load aur clean
    train_df = clean_data(load_data(TRAIN_PATH))
    test_df = clean_data(load_data(TEST_PATH))

    # encoding
    train_df = encode_data(train_df)
    test_df = encode_data(test_df)

    # test mein kuch service/flag values alag ho sakti hain,
    # isliye test ke columns ko train ke columns jaisa bana do
    test_df = test_df.reindex(columns=train_df.columns, fill_value=0)

    # features (X) aur target (y) alag karo
    X_train = train_df.drop('label', axis=1)
    y_train = train_df['label']
    X_test = test_df.drop('label', axis=1)
    y_test = test_df['label']

    models = {
        'Decision Tree': DecisionTreeClassifier(max_depth=15, random_state=42),
        'Random Forest': RandomForestClassifier(n_estimators=100, max_depth=20, random_state=42),
    }

    best_name = None
    best_model = None
    best_f1 = 0

    for name, model in models.items():
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        f1 = f1_score(y_test, pred)

        print('Model:', name)
        print(classification_report(y_test, pred, target_names=['Normal', 'Attack']))
        print(confusion_matrix(y_test, pred))
        print('F1 (Attack):', f1)
        print('-' * 40)

        if f1 > best_f1:
            best_f1 = f1
            best_name = name
            best_model = model

    print('Best model:', best_name)

    joblib.dump(
        {'model': best_model, 'columns': list(X_train.columns)},
        MODEL_PATH,
        compress=3
    )
    print('Model saved at', MODEL_PATH)


if __name__ == '__main__':
    main()