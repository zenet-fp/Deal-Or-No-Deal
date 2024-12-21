import random

class DealOrNoDeal:
   def __init__(self):
       self._available_boxes = [0.01, 0.1, 1, 5, 25, 50, 100, 250, 500, 1000, 2500, 5000, 7500, 12500, 25000, 50000, 75000, 100000, 125000, 150000, 175000, 200000]
       random.shuffle(self._available_boxes)
       self._boxes_removed = []
       self._rounds_played = 0
       self._cut = False
       self.user_choice = None
       self.user_start_choice = []
       self.user_start_value = []

   def allocate_boxes(self):
       for x, value in enumerate(self._available_boxes, start=1):
           display_value = "X" if value == "GONE" else f"Box{x}"
           print(f"{display_value}", end=" | ")


   def user_choose(self):
       while len(self.user_start_value) == 0 and len(self.user_start_choice) == 0:
           self.allocate_boxes()
           user_choice = int(input("\nEnter the number box you want, you shall keep this one to yourself: "))
           if user_choice <= 0:
               print("Error, please enter a valid box")
           else:
               if user_choice == 22:

                   self.user_start_choice.append(user_choice)
                   self.user_start_value.append(self._available_boxes[user_choice - 1])
                   self.user_choice = user_choice
               else:
                   self.user_start_choice.append(user_choice)
                   self.user_start_value.append(self._available_boxes[user_choice])
                   self.user_choice = user_choice

               print(f"\nYou have chosen the box: {user_choice}, the value of this box is hidden until you accept a deal or 2 boxes remain.")
               print("---------------------------------------------------------------------------------------------------------------------------")
               self._available_boxes[user_choice - 1] = "GONE"
               self._boxes_removed.append(f"Box{user_choice}")
               self._rounds_played += 1
               print(f"Rounds played: {self._rounds_played}")


   def main(self):
       self.user_choose()
       while len(self._available_boxes) > 2 and not self._cut:
           while self._rounds_played != 21:
               self.allocate_boxes()
               user_choice_ = int(input("\nEnter another box, this time try to eliminate the boxes with the least value: ")) - 1
               player_chosen_card_ = self._available_boxes[user_choice_]


               if user_choice_ <= 0:
                   print("Error, please enter a valid box")
               elif self._available_boxes[user_choice_] == "GONE":
                   print("Error, this box has been picked")
                   continue
               else:
                   print(f"\nYou have chosen the box: {user_choice_ + 1}, this has a value of: £{self._available_boxes[user_choice_]}")
                   print("---------------------------------------------------------------------------------------------------------------------------")
                   self._available_boxes[user_choice_] = "GONE"
                   self._rounds_played += 1
                   print(f"Rounds played: {self._rounds_played}")

                   if self._rounds_played in [6, 9, 12, 14]:
                       self.dealer_choice()
                       if self._cut:
                           break

           if self._rounds_played == 21:
               self.final_round()
               break


   def dealer_choice(self):
       deal = random.randint(2500, 10000)
       print(f"\nThe dealer wants to buy your box at: £{deal}")
       user_deal_choice = input("Do you want to accept this deal?: yes / no ").lower()
       if user_deal_choice in ["yes", "ye", "ys", "y"]:
           print(f"You have received: £{deal} for your box.")
           print("---------------------------------------------------------------------------------------------------------------------------")
           self._cut = True
       else:
           print("Offer has been declined")
           print()
           

   def final_round(self):
       print("---------------------------------------------------------------------------------------------------------------------------")
       for x, value in enumerate(self._available_boxes, start=1):
           display_value = "X" if value == "GONE" else f"Box{x}"
           print(f"{display_value}", end=" | ")

       print("\nThese are the remaining boxes")
       
       configure_deal = random.randint(1, 100)
       
       if configure_deal <= 40:
           print("You can choose to swap your box with the final box. ")
           user_swap = input("Do you want to sawp?: ").lower()
           
           if user_swap in ["yes", "ye", "ys", "y"]:
               remaining_box_index = next(i for i, value in enumerate(self._available_boxes) if value != "GONE")
               last_box_value = self._available_boxes[remaining_box_index]
               user_original_value = self.user_start_value[0]


               print(f"\nYou swapped your box and now have £{last_box_value}.")
               print(f"Your original box contained £{user_original_value}.")

       else:
           print(f"You kept your starting box, this has a value of: £{self.user_start_value[0]}")


if __name__ == '__main__':
   p = DealOrNoDeal()
   p.main()


