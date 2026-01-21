import pandas as pd
import numpy as np

class MissingValueHandler:

    def handle_missing(self, df: pd.DataFrame) -> pd.DataFrame:
        try:
            for col in df.columns:
                if df[col].dtype == 'object':
                    df[col] = df[col].fillna(df[col].mode()[0])

                else:
                    df[col] = df[col].fillna(df[col].median())
            return df

        except Exception as e:
            raise Exception(f"Error in missing value handling: {e}")
