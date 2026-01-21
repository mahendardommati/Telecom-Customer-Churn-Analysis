import numpy as np

class Transformer:

    def log_transform(self, df, columns):
        try:
            for col in columns:
                df[col] = np.log1p(df[col])
            return df
        except Exception as e:
            raise Exception(f"Transformation error: {e}")
