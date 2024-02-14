from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel
import uvicorn
from api._assist.scrapers import AsyncScraper, InstitutionFetcher, AssistOrgAPI
from api._assist.models import AgreementQuery 
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/api/institutions", response_model=list)
async def get_institutions():
    try:
        fetcher = InstitutionFetcher()
        institutions = await fetcher.fetch_institutions()
        return institutions
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/institution-agreements/{institution_id}", response_model=list)
async def get_institution_agreements(institution_id: int):
    try:
        api = AssistOrgAPI(school_id=institution_id, major="", major_code="")
        agreements = await api.fetch_institution_agreements(institution_id)
        return agreements
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/agreements-categories/")
async def get_agreements_categories(receiving_institution_id: int, sending_institution_id: int, academic_year_id: int):
    try:
        api = AssistOrgAPI(school_id=receiving_institution_id, major="", major_code="")
        categories = await api.fetch_agreements_categories(receiving_institution_id, sending_institution_id, academic_year_id)
        return categories
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/agreements/")
async def get_agreements(receiving_institution_id: int, sending_institution_id: int, academic_year_id: int, category_code: str):
    try:
        api = AssistOrgAPI(school_id=receiving_institution_id, major="", major_code="")
        agreements = await api.fetch_agreements(receiving_institution_id, sending_institution_id, academic_year_id, category_code)
        return agreements
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/articulation-agreements/{key}", response_model=dict)
async def get_articulation_agreements(key: str):
    try:
        scraper = AsyncScraper()
        agreement = await scraper.scrape_endpoint(f"https://assist.org/api/articulation/Agreements?Key={key}")
        return agreement
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/query-agreements/")
async def query_agreements(query: AgreementQuery):
    try:
        api = AssistOrgAPI(school_id=query.receiving_institution_id, major="", major_code="")
        if query.category_code:
            agreements = await api.fetch_agreements(query.receiving_institution_id, query.sending_institution_id, query.academic_year_id, query.category_code)
        else:
            agreements = await api.fetch_agreements_categories(query.receiving_institution_id, query.sending_institution_id, query.academic_year_id)
        return agreements
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))



@app.get("/api/openapi", include_in_schema=True)
async def custom_openapi(request: Request):
    openapi_schema = app.openapi()
    server_url = str(request.base_url)[:-1]  # Remove trailing slash for consistency
    openapi_schema["servers"] = [{"url": server_url}]
    return JSONResponse(content=openapi_schema)


# To run the server, use the following command in your terminal:
# uvicorn app:app --reload
