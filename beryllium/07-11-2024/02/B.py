import json

def get_top_three_behaviors(user_data):
    sorted_behaviors = sorted(user_data['predicted_behaviors'], key=lambda behavior: behavior['probability'], reverse=True)
    top_three_behaviors = []
    for i in range(3):
        behavior = sorted_behaviors[i]
        top_three_behaviors.append((behavior['behavior'], behavior['probability']))
    return top_three_behaviors

with open('data.json') as file:
    data = json.load(file)

for user in data:
    user_id = user['user_id']
    top_three_behaviors = get_top_three_behaviors(user)
    print(f"User ID: {user_id}")
    print(f"Top 3 Predicted Behaviors:")
    for behavior, probability in top_three_behaviors:      
        print(f"{behavior}: {probability:.2f}")
    print("\n")