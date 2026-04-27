from writer import DiaryWriter

class HeartApp:
    """The main door to your little diary."""

    def __init__(self):
        self.diary = DiaryWriter()

    def run(self):
        print("Welcome to Your Little Journal")
        print("Tell me what's on your mind...\n")

        self.diary.write_thoughts()

        print("\nSee you next time! Stay happy!")

if __name__ == "__main__":
    app = HeartApp()
    app.run()