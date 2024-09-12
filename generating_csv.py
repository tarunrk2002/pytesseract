from PIL import Image
import pytesseract
import re
import random
class abc:
    def creating_random_address(self):
        r_number = random.randint(000,999)
        r_streetnames = random.choice(['Main St', 'Oak St', 'Pine St', 'Maple St', 'Elm St', 'Cedar St'])
        r_citynames = random.choice(['Springfield', 'Boston', 'Los Angeles', 'New York', 'Chicago', 'Dallas'])
        r_states = random.choice(['IL', 'MA', 'CA', 'NY', 'TX'])
        r_zipcodes = random.choice(['62704', '02130', '90001', '10001', '60601', '75201'])
        return(f"{r_number},{r_streetnames},{r_citynames},{r_states}-{r_zipcodes}")












