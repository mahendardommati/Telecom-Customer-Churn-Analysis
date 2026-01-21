class OutlierHandler:

    def cap_outliers(self, df, column):
        try:
            q1 = df[column].quantile(0.25)
            q3 = df[column].quantile(0.75)
            iqr = q3 - q1
            lower = q1 - 1.5 * iqr
            upper = q3 + 1.5 * iqr

            df[column] = df[column].clip(lower, upper)
            return df

        except Exception as e:
            raise Exception(f"Outlier handling error: {e}")
