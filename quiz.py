# Resistance Type Quiz Program

questions = [
    {
        "question": "1. What’s your immediate thought when you remember the chore?",
        "options": {
            "A": ("Ugh. I hate doing that.", "Emotional"),
            "B": ("I’ll do it later… maybe after something more fun.", "Procrastination"),
            "C": ("I don’t think it’ll take much time, I can do it anytime.", "Cognitive"),
            "D": ("Why does it even need to be done right now?", "Lack of Necessity"),
            "E": ("It’s too much. I don’t even want to think about it.", "Overwhelm")
        }
    },
    {
        "question": "2. How do you feel physically or mentally when you consider doing the task?",
        "options": {
            "A": ("I feel a bit anxious or tense.", "Emotional"),
            "B": ("I feel tired just thinking about it.", "Motivation"),
            "C": ("I feel irritated or rebellious.", "Stubbornness"),
            "D": ("I feel fine – I just end up choosing other things.", "Low Prioritization"),
            "E": ("I feel like I might mess it up or not do it well.", "Cognitive")
        }
    },
    {
        "question": "3. Why haven’t you done it yet?",
        "options": {
            "A": ("Been busy with more important things.", "Low Prioritization"),
            "B": ("Didn’t feel like it.", "Emotional"),
            "C": ("I forgot.", "Cognitive"),
            "D": ("It feels like a never-ending task.", "Overwhelm"),
            "E": ("It will drain me.", "Motivation"),
            "F": ("Someone else should be doing it.", "Stubbornness")
        }
    },
    {
        "question": "4. When you try to do the chore, what typically happens?",
        "options": {
            "A": ("I do something else instead.", "Procrastination"),
            "B": ("I start but get distracted.", "Motivation"),
            "C": ("I don’t even attempt it.", "Overwhelm"),
            "D": ("I begin, but stop midway.", "Motivation"),
            "E": ("I do it only after external pressure.", "Stubbornness")
        }
    },
    {
        "question": "5. How important do you think this chore is?",
        "options": {
            "A": ("Low — doesn’t matter much.", "Lack of Necessity"),
            "B": ("Medium — not urgent.", "Low Prioritization"),
            "C": ("High, but I still can’t do it.", "Emotional"),
            "D": ("High, but I forget or get distracted.", "Cognitive")
        }
    },
    {
        "question": "6. What thought pattern resonates most?",
        "options": {
            "A": ("If I can’t do it perfectly, it’s not worth starting.", "Overwhelm"),
            "B": ("Why do I always have to do this?", "Stubbornness"),
            "C": ("It’s just a small thing, I can do it anytime.", "Cognitive"),
            "D": ("I’m too tired right now.", "Motivation"),
            "E": ("I’ll do it when I’m in the mood.", "Procrastination")
        }
    },
    {
        "question": "7. When you finally do the chore, how do you feel?",
        "options": {
            "A": ("Relieved – it wasn’t as bad as I thought.", "Cognitive"),
            "B": ("Exhausted – I feel drained.", "Motivation"),
            "C": ("Victorious – like I overcame something.", "Overwhelm"),
            "D": ("Resentful – I did it because I had to.", "Stubbornness"),
            "E": ("Indifferent – it didn’t matter much.", "Low Prioritization")
        }
    },
    {
        "question": "8. What’s your internal dialogue before *not* doing the chore?",
        "options": {
            "A": ("I’ll do it later.", "Procrastination"),
            "B": ("Ugh, not this again.", "Emotional"),
            "C": ("No one will notice if it’s not done.", "Lack of Necessity"),
            "D": ("I can’t deal with this right now.", "Overwhelm"),
            "E": ("It’s not urgent.", "Low Prioritization")
        }
    },
    {
        "question": "9. Have you ever resisted even when you had time and energy?",
        "options": {
            "A": ("Yes, I just didn’t want to do *that* task.", "Emotional"),
            "B": ("Yes, I wasn’t clear how to start.", "Cognitive"),
            "C": ("Yes, I didn’t think it mattered.", "Low Prioritization"),
            "D": ("No, I usually do it then.", "Motivation"),
            "E": ("Yes, I hoped someone else would do it.", "Stubbornness")
        }
    },
    {
        "question": "10. What would help you get this chore done?",
        "options": {
            "A": ("A clear plan or checklist.", "Cognitive"),
            "B": ("A burst of energy or a nap first.", "Motivation"),
            "C": ("A sense of urgency or deadline.", "Procrastination"),
            "D": ("Music, rewards, or making it fun.", "Emotional"),
            "E": ("Doing it with someone or delegating.", "Stubbornness"),
            "F": ("Remembering why it matters.", "Lack of Necessity")
        }
    }
]

# Description and Tips
resistance_info = {
    "Emotional": {
        "desc": "Your feelings—like dread, frustration, or dislike—get in the way of doing chores.",
        "tips": [
            "Pair the task with music or a treat.",
            "Acknowledge your emotions, but take action anyway.",
            "Just start for 2 minutes to bypass resistance."
        ]
    },
    "Cognitive": {
        "desc": "Your brain either underestimates, overcomplicates, or forgets the chore.",
        "tips": [
            "Break the task into 3 small steps.",
            "Use visual reminders or checklists.",
            "Set a 5-minute timer to get started."
        ]
    },
    "Motivation": {
        "desc": "You struggle with low energy or drive, even if the chore matters.",
        "tips": [
            "Do chores after something energizing.",
            "Try ‘temptation bundling’—pair it with fun.",
            "Rest first, then start small."
        ]
    },
    "Stubbornness": {
        "desc": "You resist out of defiance, feeling it’s unfair or not your responsibility.",
        "tips": [
            "Reframe the task as a choice, not a demand.",
            "Make it collaborative or competitive.",
            "Ask yourself who benefits—you might."
        ]
    },
    "Procrastination": {
        "desc": "You delay the task, always planning to do it ‘later’.",
        "tips": [
            "Set a mini-deadline or timer.",
            "Stack it after an existing habit.",
            "Start before you feel ready."
        ]
    },
    "Overwhelm": {
        "desc": "The task feels too big or stressful to even begin.",
        "tips": [
            "Shrink the task—what’s the 10% version?",
            "Focus on progress, not perfection.",
            "Start with a ‘prep’ step only."
        ]
    },
    "Low Prioritization": {
        "desc": "Other things always seem more important than this task.",
        "tips": [
            "Link it to a personal goal or benefit.",
            "Time-block it like a real appointment.",
            "Reflect on how it affects your environment or mindset."
        ]
    },
    "Lack of Necessity": {
        "desc": "You don’t believe the chore is urgent or necessary right now.",
        "tips": [
            "Ask: ‘Who benefits if I do this?’",
            "Batch similar tasks to make it worthwhile.",
            "Reframe it as self-care or future-you kindness."
        ]
    }
}

# Count resistance types
score = {}

def ask_question(q):
    print("\n" + q["question"])
    for key, (text, _) in q["options"].items():
        print(f"{key}. {text}")
    choice = input("Your answer: ").upper().strip()
    while choice not in q["options"]:
        choice = input("Please choose a valid option: ").upper().strip()
    resistance_type = q["options"][choice][1]
    score[resistance_type] = score.get(resistance_type, 0) + 1

# Run quiz
print("\n🧠 Welcome to the Chore Resistance Quiz!")
print("Answer the following 10 questions to find out what's really stopping you.\n")

for q in questions:
    ask_question(q)

# Show result
print("\n📊 Analyzing your results...\n")

top_type = max(score, key=score.get)
info = resistance_info[top_type]

print(f"🔥 **Your dominant resistance type is: {top_type}**")
print(f"\n{info['desc']}\n")

print("✅ Try These Tips:")
for tip in info["tips"]:
    print(f" - {tip}")

print("\n🧹 Remember: Small shifts can dissolve big blocks. You’ve got this!")

