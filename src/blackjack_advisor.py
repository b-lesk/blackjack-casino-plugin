import customtkinter as ctk
from screen_reader import ScreenReader
from bb_utils import format_advice
from yolo_screen_reader import YoloScreenReader

def blackjack_strategy(player_cards, dealer_card):
    """
    player_cards: list of ints, e.g. [8, 8] or [10, 6]
    dealer_card: int, e.g. 2-11 (where 11 is Ace)
    """
    # Helper functions
    def is_pair(cards):
        return len(cards) == 2 and cards[0] == cards[1]
    def is_soft(cards):
        return 11 in cards and sum(cards) <= 21

    # Convert face cards to 10, Ace to 11
    def card_value(card):
        if card in ['J', 'Q', 'K']:
            return 10
        if card == 'A':
            return 11
        return int(card)

    # Strategy tables (abbreviated for clarity; expand as needed)
    pairs = {
        (2, 2):  {2: 'Split', 3: 'Split', 4: 'Split', 5: 'Split', 6: 'Split', 7: 'Split', 8: 'Hit', 9: 'Hit', 10: 'Hit', 11: 'Hit'},
        (8, 8):  {2: 'Split', 3: 'Split', 4: 'Split', 5: 'Split', 6: 'Split', 7: 'Split', 8: 'Split', 9: 'Split', 10: 'Split', 11: 'Split'},
        (11, 11):  {2: 'Split', 3: 'Split', 4: 'Split', 5: 'Split', 6: 'Split', 7: 'Split', 8: 'Split', 9: 'Split', 10: 'Split', 11: 'Split'},
        # ...add all pairs...
    }
    soft_totals = {
        13: {2: 'Hit', 3: 'Hit', 4: 'Hit', 5: 'Double', 6: 'Double', 7: 'Hit', 8: 'Hit', 9: 'Hit', 10: 'Hit', 11: 'Hit'},
        18: {2: 'Stand', 3: 'Double', 4: 'Double', 5: 'Double', 6: 'Double', 7: 'Stand', 8: 'Stand', 9: 'Hit', 10: 'Hit', 11: 'Hit'},
        # ...add all soft totals...
    }
    hard_totals = {
        8:  {2: 'Hit', 3: 'Hit', 4: 'Hit', 5: 'Hit', 6: 'Hit', 7: 'Hit', 8: 'Hit', 9: 'Hit', 10: 'Hit', 11: 'Hit'},
        12: {2: 'Hit', 3: 'Hit', 4: 'Stand', 5: 'Stand', 6: 'Stand', 7: 'Hit', 8: 'Hit', 9: 'Hit', 10: 'Hit', 11: 'Hit'},
        17: {2: 'Stand', 3: 'Stand', 4: 'Stand', 5: 'Stand', 6: 'Stand', 7: 'Stand', 8: 'Stand', 9: 'Stand', 10: 'Stand', 11: 'Stand'},
        # ...add all hard totals...
    }

    # Convert input
    cards = [card_value(c) for c in player_cards]
    dealer = card_value(dealer_card)
    total = sum(cards)

    # Pairs
    if is_pair(cards):
        pair_key = (cards[0], cards[1])
        if pair_key in pairs and dealer in pairs[pair_key]:
            return pairs[pair_key][dealer]
        # fallback to hard total if pair not in table

    # Soft totals
    if is_soft(cards):
        if total in soft_totals and dealer in soft_totals[total]:
            return soft_totals[total][dealer]

    # Hard totals
    if total in hard_totals and dealer in hard_totals[total]:
        return hard_totals[total][dealer]

    # Default fallback
    if total >= 17:
        return "Stand"
    return "Hit"

def run_gui():
    ctk.set_appearance_mode("system")  # or "dark" / "light"
    ctk.set_default_color_theme("blue")  # Try "green", "dark-blue", etc.

    root = ctk.CTk()
    root.title("Blackjack Buddy")
    root.geometry("480x340")

    reader = YoloScreenReader(weights_path="yolov5/runs/train/exp/weights/best.pt")
    result_var = ctk.StringVar()

    title = ctk.CTkLabel(root, text="🃏 Blackjack Buddy", font=("Arial Rounded MT Bold", 28))
    title.pack(pady=(24, 10))

    advice_label = ctk.CTkLabel(root, textvariable=result_var, font=("Arial", 16), wraplength=420, justify="center")
    advice_label.pack(pady=16)

    def analyze():
        cards = reader.detect_cards()
        # Parse cards into player_cards and dealer_card as needed
        # Call blackjack_strategy and update result_var
        player_cards, dealer_card = reader.recognize_cards_on_screen()
        if player_cards and dealer_card:
            advice = blackjack_strategy(player_cards, dealer_card)
            result_var.set(f"🃏 Player: {player_cards}\n🂠 Dealer: {dealer_card}\n\n{format_advice(advice)}")
        else:
            result_var.set("❌ Could not detect at least two player cards and one dealer card.")

    analyze_btn = ctk.CTkButton(root, text="Analyze Screen", command=analyze, width=220, height=44, font=("Arial", 16))
    analyze_btn.pack(pady=8)

    quit_btn = ctk.CTkButton(root, text="Quit", command=root.quit, width=220, height=44, font=("Arial", 16))
    quit_btn.pack(pady=8)

    root.mainloop()

if __name__ == "__main__":
    run_gui()
