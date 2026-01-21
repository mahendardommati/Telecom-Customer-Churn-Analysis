from sklearn.preprocessing import LabelEncoder

class Encoder:

    def encode_categorical(self, df):
        try:
            le = LabelEncoder()
            for col in df.select_dtypes(include='object').columns:
                df[col] = le.fit_transform(df[col])
            return df

        except Exception as e:
            raise Exception(f"Encoding error: {e}")
