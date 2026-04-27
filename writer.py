class DiaryWriter:
    """A sweet and simple class to save your daily thoughts."""

    def __init__(self, heart_file="mylife.txt"):
        self.heart_file = heart_file

    def write_thoughts(self):
        """Allows you to type your heart out until you're done."""
        try:
            # 'a' lets us keep adding to our story!
            with open(self.heart_file, "a") as file:
                keep_typing = True

                while keep_typing:
                    line = input("Enter line: ")
                    file.write(line + "\n")

                    choice = input("Are there more lines y/n? ").lower()
                    if choice != 'y':
                        keep_typing = False

            print(f"\Your thoughts are tucked away in {self.heart_file}!")

        except Exception as e:
            print(f"Oopsie! Something went wrong: {e}")