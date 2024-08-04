# Nai_Synthetic

The synthetic data follows the schema as in the NAI backend branch:

### User
- user_id: Integer, Primary Key
- username: String
- email: String, Unique

### Prompt
- prompt_id: Integer, Primary Key
- user_id: Integer, Foreign Key (References User)
- text: String
- response: String

### Home
- home_id: Integer, Primary Key
- user_id: Integer, Foreign Key (References User)
- post: String
- upload_media: String

### Analytics
- analytics_id: Integer, Primary Key
- social_media: String
- user_id: Integer, Foreign Key (References User)

### Generated Files
The script in the `synth_data.py` generate the following CSV files in the project directory:

- users.csv: Contains user data
- prompts.csv: Contains prompt data
- homes.csv: Contains home data
- analytics.csv: Contains analytics data 