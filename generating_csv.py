from PIL import Image
import pytesseract
import re
import random
class address:
    def creating_random_address(self):
        r_number = random.randint(000,999)
        r_streetnames = random.choice(['Main St', 'Oak St', 'Pine St', 'Maple St', 'Elm St', 'Cedar St'])
        r_citynames = random.choice(['Springfield', 'Boston', 'Los Angeles', 'New York', 'Chicago', 'Dallas'])
        r_states = random.choice(['IL', 'MA', 'CA', 'NY', 'TX'])
        r_zipcodes = random.choice(['62704', '02130', '90001', '10001', '60601', '75201'])
        return(f"{r_number},{r_streetnames},{r_citynames},{r_states}-{r_zipcodes}")

    def creating_non_adddress(self):
        non_address_texts = random.choice([
            "Bachelor of Science in Computer Science",
            "Software Engineer at XYZ Company",
            "Experience in developing web applications",
            "Master of Business Administration",
            "Certified Data Scientist",
            "Fluent in Python and Java",
            "Bachelor of Arts in Graphic Design",
            "Front-End Developer at ABC Tech",
            "Proficient in React, JavaScript, and CSS",
            "Master of Science in Information Technology",
            "Certified Scrum Master",
            "Experienced in cloud architecture and DevOps practices",
            "Fluent in SQL and C#",
            "Software Architect at DEF Innovations",
            "Bachelor of Engineering in Electronics",
            "Agile project management expert",
            "Proficient in AI and Machine Learning",
            "Database Administrator with 5+ years of experience",
            "Master of Science in Cybersecurity",
            "Certified AWS Solutions Architect",
            "Expertise in mobile app development (iOS/Android)",
            "I am cooking",
            "The sun is shining brightly",
            "She loves reading mystery novels",
            "We're going on a vacation next week",
            "He just finished his workout",
            "The coffee tastes amazing",
            "They are watching a movie tonight",
            "It's raining outside",
            "I need to buy groceries",
            "He is learning to play the guitar",
            "The project deadline is tomorrow",
            "I am baking a cake",
            "She is working from home today",
            "We're going for a hike this weekend",
            "I am cleaning the house",
            "The dog is barking loudly",
            "I am writing an email",
            "She is practicing yoga",
            "The kids are playing in the yard",
            "I need to finish this book",
            "He is preparing dinner",
            "The meeting starts at 3 PM",
            "She is planning a surprise party",
            "I am watering the plants",
            "They are building a new house",
            "I just finished a great movie",
            "She is painting her bedroom",
            "The train is arriving soon",
            "I am learning to code",
            "We are organizing a charity event"
        ])
        return(non_address_texts)













