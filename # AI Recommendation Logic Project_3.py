# AI Recommendation Logic Project
# DecodeLabs Project 3

# User preferences
user_preferences = input(
    "Enter your favorite genres separated by commas: "
).split(",")

# Clean spaces
user_preferences = [genre.strip().title() for genre in user_preferences]

# Dataset
movies = {
    "Interstellar": ["Sci-Fi", "Adventure"],
    "John Wick": ["Action", "Thriller"],
    "Avengers": ["Action", "Sci-Fi", "Adventure"],
    "The Mask": ["Comedy"],
    "Titanic": ["Romance", "Drama"],
    "Batman": ["Action", "Adventure"],
    "Inception": ["Sci-Fi", "Thriller"]
}

# Recommendation logic
recommendations = []

for movie, genres in movies.items():

    score = 0

    for preference in user_preferences:
        if preference in genres:
            score += 1

    recommendations.append((movie, score))

# Sort by highest score
recommendations.sort(key=lambda x: x[1], reverse=True)

# Display results
print("\nRecommended Movies:\n")

for movie, score in recommendations:
    if score > 0:
        print(f"{movie}  | Match Score: {score}")