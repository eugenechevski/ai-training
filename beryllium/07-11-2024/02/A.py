import json

def get_top_three_behaviors(user_data):
    top_three_behaviors = []
    for behavior in user_data['predicted_behaviors']:
        if len(top_three_behaviors) < 3:
            top_three_behaviors.append(behavior)
        else:
            for i in range(len(top_three_behaviors)):
                if behavior['probability'] > top_three_behaviors[i]['probability']:
                    top_three_behaviors.insert(i, behavior)
                    break
                elif i == len(top_three_behaviors) - 1:
                    top_three_behaviors.append(behavior)
                    break

    return top_three_behaviors

# Load the JSON data
with open('data.json', 'r') as file:
    data = json.load(file)

# Process each user in the data
for user in data:
    user_id = user['user_id']
    predicted_behaviors = get_top_three_behaviors(user)

    print(f"User ID: {user_id}")
    print("Top three predicted behaviors:")
    for behavior in predicted_behaviors:
        print(f"{behavior['behavior']}: {behavior['probability']}")
    print("\n")