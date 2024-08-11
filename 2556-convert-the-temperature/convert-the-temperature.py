class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin = round(celsius + 273.15,5)
        fahrenheit = round(celsius * 1.80 + 32.00,5)
        # time complexity O(1)
        # space complexity O(1)
        return [kelvin, fahrenheit]