class ModelBasedAgent:
    def __init__(self, desired_temperature):
        self.desired_temperature = desired_temperature
        self.internal_state = {}
    def perceive(self, room, current_temperature):
        if room not in self.internal_state:
            self.internal_state[room] = {"temperature": current_temperature, "heater": "off"}
        else:
            self.internal_state[room]["temperature"] = current_temperature

    def act(self, room):
        current_temperature = self.internal_state[room]["temperature"]
        heater_status = self.internal_state[room]["heater"]
        
        if current_temperature < self.desired_temperature:
            if heater_status == "off":
                action = "Turn on heater"
                self.internal_state[room]["heater"] = "on"
            else:
                action = "Heater remains on"
        else:
            if heater_status == "on":
                action = "Turn off heater"
                self.internal_state[room]["heater"] = "off" 
            else:
                action = "Heater remains off"

        return action

    def run(self, rooms):
        for room, temperature in rooms.items():
            self.perceive(room, temperature)
            action = self.act(room)
            print(f"{room}: Current temperature = {temperature}°C. {action}.")

rooms = {
    "Living Room": 18,
    "Bedroom": 22,
    "Kitchen": 20,
    "Bathroom": 24
}
desired_temperature = 22
agent = ModelBasedAgent(desired_temperature)
agent.run(rooms)
