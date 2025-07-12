from crewai import Crew  # Crew orchestrates the agents and tasks
from textwrap import dedent  # Useful for clean multi-line input prompts
from agents import TravelAgents  # Custom class that defines your agents
from tasks import TravelTasks  # Custom class that defines your tasks

from dotenv import load_dotenv  # Load environment variables from .env file
load_dotenv()  # Useful if you're using secrets like API keys or LLM settings

# Main class to encapsulate the crew workflow
class TripCrew:
    def __init__(self, origin, cities, date_range, interests):
        # These values are collected from the user and passed to tasks
        self.origin = origin
        self.cities = cities
        self.date_range = date_range
        self.interests = interests

    def run(self):
        # Instantiate your defined agents and tasks
        agents = TravelAgents()
        tasks = TravelTasks()

        # Create the actual agent instances
        expert_travel_agent = agents.expert_travel_agent()
        city_selection_expert = agents.city_selection_expert()
        local_tour_guide = agents.local_tour_guide()

        # Create specific tasks and assign them to the respective agents
        plan_itinerary = tasks.plan_itinerary(
            expert_travel_agent,
            self.cities,
            self.date_range,
            self.interests
        )

        identify_city = tasks.identify_city(
            city_selection_expert,
            self.origin,
            self.cities,
            self.interests,
            self.date_range
        )

        gather_city_info = tasks.gather_city_info(
            local_tour_guide,
            self.cities,
            self.date_range,
            self.interests
        )

        # Create a crew: Assign agents and tasks together
        crew = Crew(
            agents=[
                expert_travel_agent,
                city_selection_expert,
                local_tour_guide
            ],
            tasks=[
                plan_itinerary,
                identify_city,
                gather_city_info
            ],
            verbose=True,  # Print detailed output of each step
        )

        # This is the method that kicks off the task execution
        result = crew.kickoff()
        return result


# The entry point of the script when run directly
if __name__ == "__main__":
    print("## Welcome to Trip Planner Crew")
    print('-------------------------------')

    # Collect user input
    origin = input(dedent("""\nFrom where will you be traveling from?\n"""))
    cities = input(dedent("""\nWhat are the cities options you are interested in visiting?\n"""))
    date_range = input(dedent("""\nWhat is the date range you are interested in traveling?\n"""))
    interests = input(dedent("""\nWhat are some of your high level interests and hobbies?\n"""))

    # Create an instance of TripCrew with user input
    trip_crew = TripCrew(origin, cities, date_range, interests)

    # Run the crew to execute tasks using the defined agents
    result = trip_crew.run()

    # Print the final output returned by the Crew
    print("\n\n########################")
    print("## Here is your Trip Plan")
    print("########################\n")
    print(result)
