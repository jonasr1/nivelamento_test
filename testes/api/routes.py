import os

from fastapi import APIRouter, Body, HTTPException, status

from .data_loader import load_data
from .models import Operadora
from .services import search_operadoras, search_operadoras_by_filters

router = APIRouter()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, '../bancos_dados/operadoras_de_plano_de_saude_ativas/Relatorio_cadop.csv')

if not os.path.exists(FILE_PATH):
    raise FileNotFoundError(f"Arquivo CSV não encontrado: {FILE_PATH}")

df = load_data(FILE_PATH)

@router.get('/search', response_model=list[Operadora] | None)
def search(query: str, limit: int = 10):
    ''''Search across all relevant columns using a generic term.'''
    raise_if_empty(query, 'Query string is required')
    results = search_operadoras(df, query, limit)
    return raise_if_empty(results, 'No operators found matching the query', status.HTTP_404_NOT_FOUND)

def raise_if_empty(data, detail: str, status_code=status.HTTP_400_BAD_REQUEST):
    if not data:
        raise HTTPException(status_code=status_code, detail=detail)
    return data

@router.post('/filter', response_model=list[Operadora] | None)
def filter_operadoras(filters: dict[str, str] = Body(..., example={'Nome_Fantasia': 'saude', 'UF': 'SP'}), limit: int = 10):
    '''Filters operators based on specific columns passed via JSON.'''
    search_operadoras_by_filters(df, filters, limit)
    raise_if_empty(filters, detail='Query string is required')
    results = search_operadoras_by_filters(df, filters, limit)
    return raise_if_empty(results, 'No operators found matching the query', status_code=status.HTTP_404_NOT_FOUND)
