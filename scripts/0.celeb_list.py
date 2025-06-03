male_actors = [
    # Bollywood
    "Shah Rukh Khan", "Salman Khan", "Aamir Khan", "Akshay Kumar", "Hrithik Roshan",
    "Ranbir Kapoor", "Ranveer Singh", "Amitabh Bachchan", "Ajay Devgn", "Saif Ali Khan",
    "Tiger Shroff", "Sidharth Malhotra", "Vicky Kaushal", "Kartik Aaryan", "Rajkummar Rao",
    "Ayushmann Khurrana", "Sunny Deol", "Anil Kapoor", "Nawazuddin Siddiqui", "Emraan Hashmi",

    # Telugu
    "Pawan Kalyan", "Chiranjeevi", "Mahesh Babu", "Allu Arjun", "Prabhas", "Ram Charan",
    "Jr NTR", "Nani", "Ravi Teja", "Venkatesh", "Nagarjuna", "Vijay Deverakonda",
    "Nithiin", "Naga Chaitanya", "Akhil Akkineni", "Ram Pothineni", "Sai Dharam Tej",
     "Sree Vishnu", "Sudheer Babu",

    # Tamil
    "Rajinikanth", "Kamal Haasan", "Vijay", "Ajith Kumar", "Suriya", "Dhanush", "Vikram",
    "Sivakarthikeyan", "Jayam Ravi",

    # Kannada & Malayalam
    "Yash", "Puneeth Rajkumar", "Rakshit Shetty", "Fahadh Faasil", "Dulquer Salmaan",
     "Mammootty", "Tovino Thomas"
]
female_actors = [
    # Bollywood
    "Deepika Padukone", "Alia Bhatt", "Katrina Kaif", "Priyanka Chopra", "Kareena Kapoor",
    "Anushka Sharma", "Kiara Advani", "Kriti Sanon", "Shraddha Kapoor", "Taapsee Pannu",
    "Radhika Apte", "Disha Patani", "Janhvi Kapoor", "Sara Ali Khan", "Madhuri Dixit",
    "Bhumi Pednekar", "Parineeti Chopra", "Yami Gautam", "Huma Qureshi",

    # Telugu
    "Sai Pallavi", "Samantha Ruth Prabhu", "Rashmika Mandanna", "Keerthy Suresh",
    "Pooja Hegde", "Tamannaah Bhatia", "Anushka Shetty", "Kajal Aggarwal", "Nivetha Thomas",
    "Raashi Khanna", "Lavanya Tripathi", "Eesha Rebba", "Hebah Patel", "Mehreen Pirzada",
    "Ritu Varma", "Nabha Natesh", "Krithi Shetty", "Anupama Parameswaran", "Shriya Saran",

    # Tamil/Kannada/Malayalam
    "Nayanthara", "Trisha Krishnan", "Aishwarya Rajesh", "Amala Paul",
    "Malavika Mohanan","Manju Warrier", "Nazriya Nazim", "Aparna Balamurali", "Priya Prakash Varrier"
]
celebs=male_actors+female_actors

print(len(celebs))

duplicates = [name for name in set(celebs) if celebs.count(name) > 1]
print("Duplicates:", duplicates)