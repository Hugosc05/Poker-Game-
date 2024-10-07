import random
from IA import PokerAI
from collections import Counter

class PokerGame:
    def __init__(self, players):
        # Inicializa el juego con una lista de jugadores
        self.deck = self.create_deck()  # Crea una baraja de 52 cartas
        self.players = players  # Lista de jugadores
        self.community_cards = []  # Cartas comunitarias (se reparten en el flop, turn, river)
        self.pot = 0  # Pozo acumulado de apuestas
        self.current_bet = 0  # Apuesta actual de la ronda
    
    def create_deck(self):
        # Genera una baraja de 52 cartas
        suits = ['Corazones', 'Diamantes', 'Picas', 'Tréboles']  # Palos de las cartas en español
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']  # Valores de las cartas
        return [(value, suit) for value in values for suit in suits]  # Genera una baraja como lista de tuplas (valor, palo)
    
    def shuffle_deck(self):
        # Mezcla las cartas del mazo
        random.shuffle(self.deck)
    
    def deal_cards(self):
        # Reparte dos cartas a cada jugador
        for player in self.players:
            # A cada jugador se le reparten dos cartas del mazo
            player.hand = [self.deck.pop(), self.deck.pop()]
    
    def deal_community_cards(self, num):
        # Reparte cartas comunitarias (flop, turn, river)
        for _ in range(num):
            # Añade cartas comunitarias desde el mazo
            self.community_cards.append(self.deck.pop())
        for _ in range(num):
            # Añade cartas comunitarias desde el mazo
            self.community_cards.append(self.deck.pop())
    
    def start_betting_round(self):
        # Inicia una nueva ronda de apuestas
        self.current_bet = 0  # Reinicia la apuesta actual a 0
        for player in self.players:
            player.bet = 0  # Reinicia la apuesta de cada jugador
    
    def betting_round(self):
        """Lógica básica de una ronda de apuestas."""
        for player in self.players:
            if isinstance(player, PokerAI):  # Si el jugador es una IA
                player_action = player.make_decision(self.current_bet, self.community_cards)
            else:
                player_action = player.make_decision(self.current_bet)  # Para jugadores humanos

            if player_action == 'call':
                self.pot += self.current_bet - player.bet  # Igualar la apuesta
                player.bet = self.current_bet
            elif player_action == 'raise':
                raise_amount = player.raise_amount(self.current_bet)  # Subir la apuesta
                self.current_bet += raise_amount
                self.pot += raise_amount
                player.bet = self.current_bet
            elif player_action == 'fold':
                player.active = False  # El jugador se retira de la mano
    
    def evaluate_hand(self, player_hand):
        # Evalua la mano de un jugador
        # Combina las cartas del jugador con las comunitarias
        all_cards = player_hand + self.community_cards
        all_cards = sorted(all_cards, key=lambda x: self.card_value(x[0]), reverse=True)  # Ordena por valor
        ranks = [card[0] for card in all_cards]  # Extrae los valores de las cartas
        suits = [card[1] for card in all_cards]  # Extrae los palos de las cartas
        
        # Verifica si hay Flush (mismo palo) o Straight (secuencia de valores)
        is_flush = self.is_flush(suits)
        is_straight = self.is_straight(ranks)
        counts = Counter(ranks)  # Cuenta las ocurrencias de cada valor
        
        # Verifica las mejores combinaciones de manos de póker
        if is_flush and is_straight:
            return "Escalera de Color", all_cards[:5]
        elif 4 in counts.values():
            return "Póker", self.get_best_hand(counts, 4)
        elif 3 in counts.values() and 2 in counts.values():
            return "Full House", self.get_best_hand(counts, 3, 2)
        elif is_flush:
            return "Color", all_cards[:5]
        elif is_straight:
            return "Escalera", all_cards[:5]
        elif 3 in counts.values():
            return "Trío", self.get_best_hand(counts, 3)
        elif list(counts.values()).count(2) == 2:
            return "Doble Pareja", self.get_best_hand(counts, 2, 2)
        elif 2 in counts.values():
            return "Pareja", self.get_best_hand(counts, 2)
        else:
            return "Carta Alta", all_cards[:5]
    
    def card_value(self, rank):
        # Convierte el valor de la carta a un número para facilitar la evaluación
        if rank == 'A':
            return 14
        elif rank == 'K':
            return 13
        elif rank == 'Q':
            return 12
        elif rank == 'J':
            return 11
        else:
            return int(rank)
    
    def is_flush(self, suits):
        # Verifica si hay Flush (mismo palo)
        return max(Counter(suits).values()) >= 5
    
    def is_straight(self, ranks):
       #  Verifica si hay una escalera (cinco cartas en secuencia)
        rank_values = sorted(set(self.card_value(rank) for rank in ranks), reverse=True)
        for i in range(len(rank_values) - 4):
            if rank_values[i] - rank_values[i + 4] == 4:
                return True
        return False
    
    def get_best_hand(self, counts, *criteria):
        # Devuelve las mejores cartas según los criterios dados (ej. pares, trío)
        hand = []
        for c in criteria:
            for rank, count in counts.items():
                if count == c:
                    hand.extend([(rank, suit) for rank_, suit in self.community_cards if rank_ == rank])
                    if len(hand) == 5:
                        return hand
        return hand[:5]

    def play_game(self):
        # Lógica completa de una partida
        self.shuffle_deck()  # Mezcla la baraja
        self.deal_cards()  # Reparte las cartas a los jugadores
        
        # Primera ronda de apuestas
        self.start_betting_round()
        self.betting_round()

        # Flop (3 cartas comunitarias)
        self.deal_community_cards(3)
        self.betting_round()

        # Turn (1 carta comunitaria)
        self.deal_community_cards(1)
        self.betting_round()

        # River (1 carta comunitaria)
        self.deal_community_cards(1)
        self.betting_round()

        # Evaluar las manos de los jugadores activos
        remaining_players = [p for p in self.players if p.active]
        best_hand = None
        best_player = None
        
        for player in remaining_players:
            hand_type, hand = self.evaluate_hand(player.hand)
            print(f"{player.name} tiene {hand_type} con {hand}")
            if best_hand is None or self.compare_hands(hand, best_hand):
                best_hand = hand
                best_player = player
        
        print(f"El ganador es {best_player.name} con {best_hand}")
    
    def compare_hands(self, hand1, hand2):
        # Compara dos manos y determina cuál es mejor
        hand1_values = sorted([self.card_value(card[0]) for card in hand1], reverse=True)
        hand2_values = sorted([self.card_value(card[0]) for card in hand2], reverse=True)
        return hand1_values > hand2_values
