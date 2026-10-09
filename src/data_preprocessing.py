import pandas as pd

COLUMN_NAMES = [
    'duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes',
    'land', 'wrong_fragment', 'urgent', 'hot', 'num_failed_logins', 'logged_in',
    'num_compromised', 'root_shell', 'su_attempted', 'num_root',
    'num_file_creations', 'num_shells', 'num_access_files', 'num_outbound_cmds',
    'is_host_login', 'is_guest_login', 'count', 'srv_count', 'serror_rate',
    'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate',
    'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count',
    'dst_host_srv_count', 'dst_host_same_srv_rate', 'dst_host_diff_srv_rate',
    'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate',
    'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_rerror_rate',
    'dst_host_srv_rerror_rate', 'attack', 'level'
]

CATEGORICAL_COLS = ['protocol_type', 'service', 'flag']


def load_data(path):
    # file mein header nahi hai, isliye names khud de rahe hain
    df = pd.read_csv(path, names=COLUMN_NAMES)
    return df


def clean_data(df):
    df = df.copy()

    # level column sirf attack ki difficulty batata hai, model ke kaam ka nahi
    df = df.drop('level', axis=1)

    # binary label: normal = 0, koi bhi attack = 1
    df['label'] = 0
    df.loc[df['attack'] != 'normal', 'label'] = 1

    # attack ka naam ab label mein convert ho gaya, original column hata do
    df = df.drop('attack', axis=1)
    return df


def encode_data(df):
    # protocol_type, service, flag text columns hain, unko one-hot encode karo
    df = pd.get_dummies(df, columns=CATEGORICAL_COLS, dtype=int)
    return df