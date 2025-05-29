# import sys
# import os
# import asyncio
# from typing import TypedDict
# from dotenv import load_dotenv  # type: ignore
# from langgraph.graph import StateGraph, END  # type: ignore

# from tools.api_ninja import get_location_from_full_address, get_location_from_zip, get_city_demographics
# from tools.naics_classifier import classify_business
# from tools.form_filler import fill_form
# from models import BusinessData, SessionLocal

# load_dotenv()


# if sys.platform.startswith("win"):
#     # This switches the event loop policy to a compatible one for subprocess on Windows. - Form FillingError
#     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


# class AgentState(TypedDict):
#     data: dict
#     validated: bool
#     submitted: bool


# def extract_data(state: AgentState) -> AgentState:
#     street = state.get("street", "")
#     city = state.get("city", "")
#     state_abbr = state.get("state", "")
#     business_description = state.get("business_description", "")

#     print(f"📦 Geocoding full address: {street}, {city}, {state_abbr}")
#     location = get_location_from_full_address(street, city, state_abbr)

#     if location:
#         loc = location[0]
#         lat = float(loc["latitude"])
#         lon = float(loc["longitude"])
#         zip_code = loc.get("postal_code", "")
#         census_tract = loc.get("census_tract", "N/A")
#         print(f"✅ Geocoded: {lat}, {lon}")

#         print("📊 Getting city demographics...")
#         demographics = get_city_demographics(city, state_abbr)
#         population = demographics[0].get("population", 0)
#         country = demographics[0].get("country", "")
#         is_capital = demographics[0].get("is_capital", False)

#         print("🏢 Inferring business category using Ollama...")
#         naics = classify_business(business_description)
#         print("✅ NAICS Result:", naics)

#         db = SessionLocal()
#         entry = BusinessData(
#             zip_code=zip_code,
#             city=city,
#             state=state_abbr,
#             latitude=lat,
#             longitude=lon,
#             census_tract=census_tract,
#             population=population,
#             country=country,
#             is_capital=is_capital,
#             business_description=business_description,
#             naics=naics
#         )
#         db.add(entry)
#         db.commit()
#         db.refresh(entry)

#         return {
#             "data": {
#                 "zip_code": zip_code,
#                 "latitude": lat,
#                 "longitude": lon,
#                 "city": city,
#                 "state": state_abbr,
#                 "census_tract": census_tract,
#                 "population": population,
#                 "country": country,
#                 "is_capital": is_capital,
#                 "business_description": business_description,
#                 "naics": naics
#             },
#             "validated": False,
#             "submitted": False
#         }

#     print("❌ Full address geocoding failed.")
#     return {"data": {}, "validated": False, "submitted": False}


# def validate_data(state: AgentState) -> AgentState:
#     print("✅ Validating data...")
#     state["validated"] = True
#     return state


# async def submit_form(state: AgentState) -> AgentState:
#     print("🚀 Submitting form...")
#     try:
#         result = fill_form(state["data"])  # ⛔️ Don't await a sync function
#         print(f"✅ Form submitted: {result}")
#     except Exception as e:
#         print(f"❌ Form error: {e}")
#     state["submitted"] = True
#     return state

# graph = StateGraph(AgentState)
# graph.add_node("extract_data", extract_data)
# graph.add_node("validate_data", validate_data)
# graph.add_node("submit_form", submit_form)

# graph.set_entry_point("extract_data")
# graph.add_edge("extract_data", "validate_data")
# graph.add_edge("validate_data", "submit_form")
# graph.add_edge("submit_form", END)

# workflow = graph.compile()


# async def run_workflow():
#     result = await workflow.ainvoke({})
#     print("📜 Workflow result:", result)

# if __name__ == "__main__":
#     asyncio.run(run_workflow())


import sys
import os
import asyncio
from typing import TypedDict
from dotenv import load_dotenv  # type: ignore
from langgraph.graph import StateGraph, END  # type: ignore

from tools.api_ninja import get_zip_info, get_city_demographics
from tools.naics_classifier import classify_business
from tools.form_filler import fill_form
from models import BusinessData, SessionLocal

load_dotenv()

if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


class AgentState(TypedDict):
    street: str
    city: str
    state: str
    business_description: str
    data: dict
    validated: bool
    submitted: bool


def extract_data(state: AgentState) -> AgentState:
    city = state.get("city", "")
    state_abbr = state.get("state", "")
    business_description = state.get("business_description", "")
    street = state.get("street", "")

    print(f"📦 Looking up ZIP code for city/state: {city}, {state_abbr}")
    # Might be deprecated but kept for compatibility
    zip_info = get_zip_info(city, state_abbr)

    print("📊 Getting city demographics...")
    demographics = get_city_demographics(city, state_abbr)
    demo = demographics[0] if demographics else {}

    lat = demo.get("latitude", 0.0)
    lon = demo.get("longitude", 0.0)
    population = demo.get("population", 0)
    country = demo.get("country", "")
    is_capital = demo.get("is_capital", False)
    zip_code = demo.get("zip", "N/A")

    print("🏢 Inferring business category using Ollama...")
    naics = classify_business(business_description)
    print("✅ NAICS Result:", naics)

    db = SessionLocal()
    entry = BusinessData(
        zip_code=zip_code,
        city=city,
        state=state_abbr,
        latitude=lat,
        longitude=lon,
        census_tract="N/A",
        population=population,
        country=country,
        is_capital=is_capital,
        business_description=business_description,
        naics=naics
    )
    db.add(entry)
    db.commit()
    db.refresh(entry)

    return {
        "street": street,
        "city": city,
        "state": state_abbr,
        "business_description": business_description,
        "data": {
            "zip_code": zip_code,
            "latitude": lat,
            "longitude": lon,
            "city": city,
            "state": state_abbr,
            "census_tract": "N/A",
            "population": population,
            "country": country,
            "is_capital": is_capital,
            "business_description": business_description,
            "naics": naics
        },
        "validated": False,
        "submitted": False
    }


def validate_data(state: AgentState) -> AgentState:
    print("✅ Validating data...")
    state["validated"] = True
    return state


async def submit_form(state: AgentState) -> AgentState:
    print("🚀 Submitting form...")
    try:
        result = fill_form(state["data"])
        print(f"✅ Form submitted: {result}")
    except Exception as e:
        print(f"❌ Form error: {e}")
    state["submitted"] = True
    return state

graph = StateGraph(AgentState)
graph.add_node("extract_data", extract_data)
graph.add_node("validate_data", validate_data)
graph.add_node("submit_form", submit_form)

graph.set_entry_point("extract_data")
graph.add_edge("extract_data", "validate_data")
graph.add_edge("validate_data", "submit_form")
graph.add_edge("submit_form", END)

workflow = graph.compile()


async def run_workflow():
    result = await workflow.ainvoke({})
    print("📜 Workflow result:", result)

if __name__ == "__main__":
    asyncio.run(run_workflow())
