class Player:
    def __init__(self, name, balance):
        
        self.name = name
        self.balance = balance
        self.hand = [] #mano del jugador 2 cartas
        
    def make_bet(self, amount):
        # Realiza una apuesta el jugador 
        if amount > self.balance:
            raise ValueError("No tienes suficiente saldo para apostar esa cantidad.")
        self.balance -= amount
        return amount
        
    def show_hand(self):
        # Muestra la mano del jugador
        return self.hand
    
    