class LegalAid():
    id = None
    relationto = None
    relation_other = None
    other_party = None
    relation_start = None
    relation_end = None
    courtship_date = None
    case_number = None
    
    def identify(self):
        id = int(input("Are you 1.the applicant or 2.the respondant?\n"))
        if id == 1:
            relationto = int(input("What is your relationship to the child or children in question?\n 1.Mother \n 2.Father \n 3.Other\n>>"))
            if relationto == 3:
                print("Please specify below\n")
                relation_other = input(">>")
            other_party = input("Is the other party your former partner? (y/n):")
            if other_party == 'y':
                relation_start = input("When did the relationship begin?(dd/mm/yyyy)\n>>")
                courtship_date = input("Date of marriage or civil partnership if applicable(dd/mm/yyyy):\n")
                relation_end = input("When did the relationship end?(dd/mm/yyyy)\n>>")
            case_number = input("What is the case number stated on the court papers that you have?:\n")

def main():
    legal = LegalAid()
    legal.identify()

      
if __name__ == "__main__":
  main()
