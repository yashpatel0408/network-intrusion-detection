import joblib

from data_preprocessing import load_data, clean_data, encode_data

TEST_PATH = '../data/KDDTest+.txt'
MODEL_PATH = '../models/ids_model.pkl'


def predict_connections(df):
    saved = joblib.load(MODEL_PATH)
    model = saved['model']
    columns = saved['columns']

    X = encode_data(df)
    X = X.reindex(columns=columns, fill_value=0)
    return model.predict(X)


if __name__ == '__main__':
    df = clean_data(load_data(TEST_PATH))
    sample = df.sample(10, random_state=1)

    actual = sample['label'].values
    predicted = predict_connections(sample.drop('label', axis=1))

    for i in range(len(sample)):
        actual_text = 'ATTACK' if actual[i] == 1 else 'NORMAL'
        predicted_text = 'ATTACK' if predicted[i] == 1 else 'NORMAL'
        print('Actual:', actual_text, '| Predicted:', predicted_text)