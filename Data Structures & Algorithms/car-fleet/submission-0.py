class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = deque()
        cars = []

        for position_i, speed_j in zip(position, speed):
            cars.append([position_i, speed_j])
        
        cars.sort(key=lambda x: x[0])

        stack = []
        for i in range(len(cars)-1, -1, -1):
            position, speed = cars[i]
            time = (target-position)/speed

            if len(stack) > 0:
                if time > stack[-1]:
                    stack.append(time)
            else:
                stack.append(time)
        
        return len(stack)
