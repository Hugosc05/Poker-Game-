import random
from core.game import PokerGame  # Importamos la lógica del juego

class PokerAI:
    def __init__(self, name, chips):
        # Inicializamos la IA con su nombre y la cantidad de fichas que tiene
        self.name = name  # Nombre del jugador IA
        self.chips = chips  # Cantidad de fichas que tiene la IA
        self.hand = []  # Cartas del jugador IA (se reparten al inicio del juego)
        self.active = True  # Si el jugador IA sigue en juego o se retiró
        self.bet = 0  # Apuesta actual de la IA en la ronda
    
    def evaluate_hand_strength(self, community_cards):
        
        #Evalúa la fuerza de la mano de la IA en función de las cartas comunitarias.
        
        all_cards = self.hand + community_cards  # Combina cartas propias y comunitarias
        game = PokerGame([])  # Creamos una instancia del juego para evaluar la mano
        hand_type, _ = game.evaluate_hand(self.hand)  # Evaluamos la mano
        # Asignamos un valor numérico según el tipo de mano (por simplicidad, valores inventados)
        hand_strengths = {
            "Escalera de Color": 1.0,
            "Póker": 0.9,
            "Full House": 0.8,
            "Color": 0.7,
            "Escalera": 0.6,
            "Trío": 0.5,
            "Doble Pareja": 0.4,
            "Pareja": 0.3,
            "Carta Alta": 0.1
        }
        return hand_strengths.get(hand_type, 0.1)  # Devuelve la fuerza de la mano (o 0.1 si es desconocida)
    
    def make_decision(self, current_bet, community_cards):
        
        #Toma una decisión (igualar, subir, retirarse) en función de la fuerza de la mano y la apuesta actual.
        
        hand_strength = self.evaluate_hand_strength(community_cards)  # Evalúa la fuerza de la mano

        if hand_strength > 0.8:  # Mano muy fuerte
            if self.chips >= current_bet * 2:
                return 'raise'  # Subir la apuesta si tiene suficientes fichas
            else:
                return 'call'  # Igualar la apuesta si no puede subir más
        elif hand_strength > 0.4:  # Mano decente
            return 'call'  # Igualar la apuesta
        else:
            return 'fold'  # Retirarse si la mano es débil
    
    def raise_amount(self, current_bet):
        
        #Determina cuánto subir en caso de hacer raise.
        
        raise_amount = current_bet + (self.chips * 0.1)  # Sube un 10% de sus fichas
        return min(raise_amount, self.chips)  # Asegura no apostar más de lo que tiene
