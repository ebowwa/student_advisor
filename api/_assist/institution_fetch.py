# institution_fetch.py
import asyncio
from api._assist.async_scraper import AsyncScraper

class InstitutionFetcher(AsyncScraper):
    """
    Fetches and parses institution-related data using the AsyncScraper.
    """

    async def fetch_institutions(self):
        """
        Fetches a list of institutions from the assist.org API or another API.
        """
        institutions_data = await self.scrape_endpoint("https://assist.org/api/institutions")
        if institutions_data:
            return self.parse_institutions(institutions_data)
        else:
            print("Error: Unable to fetch institutions data.")
            return []

    @staticmethod
    def parse_institutions(data):
        """
        Parses institutions data and returns a list of dictionaries.
        """
        institutions = []
        for institution in data:
            institutions.append({
                "ID": institution['id'],
                "Name": institution['names'][0]['name']
            })
        return institutions

    async def fetch_institution_agreements(self, institution_id):
        """
        Fetches institution agreements data for a specific institution.
        """
        endpoint = f"institution-agreements/{institution_id}"
        institution_agreements_data = await self.scrape_endpoint(f"https://assist.org/api/{endpoint}")
        if institution_agreements_data:
            return self.parse_institution_agreements(institution_agreements_data)
        else:
            print(f"Error: Unable to fetch institution agreements data for institution ID {institution_id}.")
            return None

    @staticmethod
    def parse_institution_agreements(data):
        """
        Parses institution agreements data.
        """
        print("\nInstitution Agreements:")
        for agreement in data:
            print(f"Institution Parent ID: {agreement['institutionParentId']}, "
                  f"Institution Name: {agreement['institutionName']}, "
                  f"Code: {agreement['code']}, "
                  f"Is Community College: {agreement['isCommunityCollege']}")
