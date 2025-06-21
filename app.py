from flask import Flask, render_template, request
from utils.mood_analyzer import get_mood_category
from utils.recommender import recommend_food

app = Flask(__name__)

mood_emojis = {
    "Happy": "😄",
    "Sad": "😢",
    "Tired": "😴",
    "Sick": "🤒"
}

mood_messages = {
    "Happy": "You're feeling awesome today! Here's some delicious celebration food 🎉",
    "Sad": "Aww, let’s lift your spirits with something tasty 💖",
    "Tired": "Looks like you need comfort food to recharge 😴",
    "Sick": "We’ll keep it light and healthy so you feel better 🤒"
}

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = []
    mood_category = ""
    emoji = ""
    message = ""
    
    if request.method == 'POST':
        user_input = request.form['mood_input']
        preference = request.form['preference']
        
        mood_category = get_mood_category(user_input)
        emoji = mood_emojis.get(mood_category, "")
        message = mood_messages.get(mood_category, "")
        
        recommendations = recommend_food(mood_category, preference)
    
    return render_template(
        'index.html',
        recommendations=recommendations,
        mood_category=mood_category,
        emoji=emoji,
        message=message
    )

if __name__ == '__main__':
    app.run(debug=True)
