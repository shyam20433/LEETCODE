class BusBooking:

    def __init__(self, n: int):
        self.booking={}
        self.total=0
        

    def toggle(self, seat: str) -> None:
        if seat in self.booking:
            self.total-=self.booking.pop(seat)
            return
        middle = {"A": "B", "D": "C"}.get(seat[0], "") + seat[1:]
        self.booking[seat]=3 if middle in self.booking else 1
        self.total+=self.booking[seat]
    def getTotalTime(self) -> int:
        return self.total
    def getMinTime(self) -> int:
        return len(self.booking)
        


# Your BusBooking object will be instantiated and called as such:
# obj = BusBooking(n)
# obj.toggle(seat)
# param_2 = obj.getTotalTime()
# param_3 = obj.getMinTime()