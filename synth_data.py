import csv
from faker import Faker
import random

# Initialize the Faker instance
fake = Faker()

# Define the number of samples
num_samples = 100

# Initialize lists to hold the generated data
users = []
prompts = []
homes = []
analytics = []

# Function to generate user data
def generate_user(user_id):
    return {
        "user_id": user_id,
        "username": fake.user_name(),
        "email": fake.unique.email()
    }

# Function to generate prompt data
def generate_prompt(prompt_id, user_id):
    return {
        "prompt_id": prompt_id,
        "user_id": user_id,
        "text": fake.sentence(),
        "response": fake.sentence()
    }

# Function to generate home data
def generate_home(home_id, user_id):
    return {
        "home_id": home_id,
        "user_id": user_id,
        "post": fake.text(),
        "upload_media": fake.image_url()
    }

# Function to generate analytics data
def generate_analytics(analytics_id, user_id):
    return {
        "analytics_id": analytics_id,
        "social_media": random.choice(['Facebook', 'Twitter', 'Instagram', 'LinkedIn']),
        "user_id": user_id
    }

# Generate data
for user_id in range(1, num_samples + 1):
    user = generate_user(user_id)
    
    # Generate associated prompts
    num_prompts = random.randint(1, 5)
    user_prompts = []
    for i in range(num_prompts):
        prompt = generate_prompt(len(prompts) + 1, user_id)
        user_prompts.append(prompt)
        prompts.append(prompt)
    user["prompts"] = user_prompts
    
    # Generate associated homes
    num_homes = random.randint(1, 3)
    user_homes = []
    for i in range(num_homes):
        home = generate_home(len(homes) + 1, user_id)
        user_homes.append(home)
        homes.append(home)
    user["homes"] = user_homes
    
    # Generate associated analytics
    num_analytics = random.randint(1, 2)
    user_analytics = []
    for i in range(num_analytics):
        analytic = generate_analytics(len(analytics) + 1, user_id)
        user_analytics.append(analytic)
        analytics.append(analytic)
    user["analytics"] = user_analytics
    
    users.append(user)

# Save users data to CSV
with open('users.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["user_id", "username", "email"])
    writer.writeheader()
    for user in users:
        writer.writerow({"user_id": user["user_id"], "username": user["username"], "email": user["email"]})

# Save prompts data to CSV
with open('prompts.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["prompt_id", "user_id", "text", "response"])
    writer.writeheader()
    for prompt in prompts:
        writer.writerow({"prompt_id": prompt["prompt_id"], "user_id": prompt["user_id"], "text": prompt["text"], "response": prompt["response"]})

# Save homes data to CSV
with open('homes.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["home_id", "user_id", "post", "upload_media"])
    writer.writeheader()
    for home in homes:
        writer.writerow({"home_id": home["home_id"], "user_id": home["user_id"], "post": home["post"], "upload_media": home["upload_media"]})

# Save analytics data to CSV
with open('analytics.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["analytics_id", "social_media", "user_id"])
    writer.writeheader()
    for analytic in analytics:
        writer.writerow({"analytics_id": analytic["analytics_id"], "social_media": analytic["social_media"], "user_id": analytic["user_id"]})

print("Data has been successfully generated and saved to CSV files.")
