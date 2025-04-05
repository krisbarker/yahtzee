from dataclasses import dataclass, field
from typing import Dict

@dataclass
class Scorecard:
    upper_section: Dict[str, int] = field(default_factory=lambda: {
        "ones": 0, "twos": 0, "threes": 0,
        "fours": 0, "fives": 0, "sixes": 0,
    })
    bonus: int = 0
    lower_section: Dict[str, int] = field(default_factory=lambda: {
        "three_of_a_kind": 0, "four_of_a_kind": 0,
        "full_house": 0, "small_straight": 0,
        "large_straight": 0, "yahtzee": 0,
        "chance": 0
    })
    yahtzees: int = 0

    def calculate_total_score(self) -> int:
        upper_total = sum(self.upper_section.values())
        lower_total = sum(self.lower_section.values()) + self.yahtzees * 100

        if upper_total >= 63:
            self.bonus = 35
        else:
            self.bonus = 0

        return upper_total + lower_total + self.bonus

    def display_scorecard(self):
        print("Scorecard:")
        print("="*20)

        # Print Upper Section
        print("\nUpper Section")
        for category, score in self.upper_section.items():
            print(f"{category.title()}: {score}")
        print(f"Bonus: {self.bonus}")

        # Print Lower Section
        print("\nLower Section")
        for category, score in self.lower_section.items():
            print(f"{category.replace('_', ' ').title()}: {score}")

        # Print Yahtzees and Total Score
        print(f"\nYahtzees: x{self.yahtzees} (Bonus: {self.yahtzees * 100})")
        total_score = self.calculate_total_score()
        print(f"Total Score: {total_score}")


def main():
    # Example Usage
    scorecard = Scorecard(
        upper_section={"ones": 42, "twos": 14, "threes": 0, "fours": 7, "fives": 35, "sixes": 21},
        lower_section={"three_of_a_kind": 30, "four_of_a_kind": 40,
                       "full_house": 25, "small_straight": 15,
                       "large_straight": 20, "yahtzee": 50, "chance": 18}
    )
    scorecard.yahtzees = 1
    scorecard.upper_section['threes'] = 9
    scorecard.display_scorecard()


if __name__ == "__main__":
    main()
