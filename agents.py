from crewai import Agent
from textwrap import dedent
from langchain_community.chat_models import ChatOllama  # ✅ new import

class TravelAgents:
    def __init__(self):
        self.llm = ChatOllama(model="mistral", temperature=0.7)  # ✅ Using Ollama

    def expert_travel_agent(self):
        return Agent(
            role="Expert Travel Agent",
            backstory=dedent("""
                Expert in travel planning and logistics. 
                I have decades of experience making travel itineraries.
            """),
            goal=dedent("""
                Create a 7-day travel itinerary with detailed per-day plans,
                include budget, packing suggestions, and safety tips.
            """),
           
            verbose=True,
            llm=self.llm,
        )

    def city_selection_expert(self):
        return Agent(
            role="City Selection Expert",
            backstory=dedent("""
                Expert at analyzing travel data to pick ideal destinations.
            """),
            goal=dedent("""
                Select the best cities based on weather, season, prices, and traveler interests.
            """),
       
            verbose=True,
            llm=self.llm,
        )

    def local_tour_guide(self):
        return Agent(
            role="Local Tour Guide",
            backstory=dedent("""
                Knowledgeable local guide with extensive information
                about the city, its attractions and customs.
            """),
            goal=dedent("""
                Provide the BEST insights about the selected city.
            """),
            
            verbose=True,
            llm=self.llm,
        )
