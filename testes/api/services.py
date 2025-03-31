from fastapi import HTTPException, status
import pandas as pd

from models import Operadora

def filter_dataframe(df: pd.DataFrame, conditions: list[pd.Series], filtered_df, limit: int) -> list[Operadora]:
    if not conditions:
        return []
    cleaned_results = [clean_data(record) for record in filtered_df.head(limit).to_dict(orient='records')]
    return [Operadora(**row) for row in cleaned_results]

def validate_filters(df: pd.DataFrame, filters: dict):
    '''Validates whether all the keys of the filters exist in the columns of the DataFrame.'''
    invalid_columns = [column for column in filters if column not in df.columns]
    if invalid_columns:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Invalid filters: {', '.join(invalid_columns)}'
        )

def search_operadoras_by_filters(df: pd.DataFrame, filters: dict, limit: int = 10) -> list[Operadora] | None:
    validate_filters(df, filters)
    conditions = [
        df[column].astype(str).str.lower().str.contains(value.lower(), na=False)
        for column, value in filters.items()
        if column in df.columns
    ]
    filtered_df = df[pd.concat(conditions, axis=1).all(axis=1)]
    return filter_dataframe(df, conditions, filtered_df, limit)

def search_operadoras(df: pd.DataFrame, query: str, limit: int = 10) -> list[Operadora] | None:
    query = query.lower()
    search_fields = ['Nome_Fantasia', 'Razao_Social', 'CNPJ', 'Modalidade', 'Cidade', 'UF']
    conditions = [
        df[field].astype(str).str.lower().str.contains(query, na=False)
        for field in search_fields
    ]
    filtered_df = df[pd.concat(conditions, axis=1).any(axis=1)]
    return filter_dataframe(df, conditions, filtered_df, limit)
def clean_data(record: dict) -> dict:
    '''Cleans the data, converting NaN and None to empty string and ensuring that all values are strings.'''
    return {key: '' if pd.isna(value) else str(value) for key, value in record.items()}