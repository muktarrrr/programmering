import time

# Short snippet from "Payphone" by Maroon 5 (fair use)
lyrics = [
    "I'm at a payphone, tryin' to call home",
    "All of my change I spent on you",
    "Where have the times gone?",
    "Baby, it's all wrong",
    "Where are the plans we made for two?"
    "if happpy after didnt exit"
]

# Simulate singing by printing each line with delay
def sing_lyrics(lyrics, delay=1.5):
    print("🎤 Singing 'Payphone' by Maroon 5...\n")
    for line in lyrics:
        print(line)
        time.sleep(delay)
    print("\n🎵 End of song snippet 🎵")

if __name__ == "__main__":
    sing_lyrics(lyrics)
