import time

# ANSI escape sequences for colors
class Color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class StealthCheck:
    def __init__(self):
        self.valid_accounts = []
        self.invalid_accounts = []

    def display_main_menu(self):
        print(Color.HEADER + "========================")
        print("     StealthCheck")
        print("========================" + Color.ENDC)
        print("[1] Netflix")
        print("[2] Spotify")
        print("[3] Crunchyroll")
        print("[4] Check for Update")
        print("[5] Join our Telegram")
        print("[6] Follow me on GitHub")
        print("[7] Subscribe to our YouTube")
        print("[8] Exit Tool")
        print("\n" + Color.BOLD + "Made by DroidDevHub" + Color.ENDC)

    def choose_service(self):
        while True:
            self.display_main_menu()
            choice = input("\nEnter your choice: ")
            if choice == '1':
                self.netflix_menu()
            elif choice == '2':
                self.spotify_menu()
            elif choice == '3':
                self.crunchyroll_menu()
            elif choice == '4':
                self.check_for_update()
            elif choice == '5':
                self.join_telegram()
            elif choice == '6':
                self.follow_github()
            elif choice == '7':
                self.subscribe_youtube()
            elif choice == '8':
                print("\nExiting the StealthCheck tool...")
                time.sleep(1)
                break
            else:
                print("\nInvalid choice. Please try again.")

    def netflix_menu(self):
        while True:
            print("\n" + Color.OKBLUE + "========================")
            print("     Netflix Options")
            print("========================" + Color.ENDC)
            print("[1] Single Account Check")
            print("[2] Mass Account Check")
            print("[3] Valid Accounts")
            print("[4] Dead Accounts")
            print("[5] Download Valid Accounts")
            print("[6] Return to Main Menu")

            choice = input("\nEnter your choice: ")
            if choice == '1':
                self.single_account_check("Netflix")
            elif choice == '2':
                self.mass_account_check("Netflix")
            elif choice == '3':
                self.display_valid_accounts("Netflix")
            elif choice == '4':
                self.display_dead_accounts("Netflix")
            elif choice == '5':
                self.download_valid_accounts("Netflix")
            elif choice == '6':
                break
            else:
                print("\nInvalid choice. Please try again.")

    def spotify_menu(self):
        while True:
            print("\n" + Color.OKBLUE + "========================")
            print("     Spotify Options")
            print("========================" + Color.ENDC)
            print("[1] Single Account Check")
            print("[2] Mass Account Check")
            print("[3] Valid Accounts")
            print("[4] Dead Accounts")
            print("[5] Download Valid Accounts")
            print("[6] Return to Main Menu")

            choice = input("\nEnter your choice: ")
            if choice == '1':
                self.single_account_check("Spotify")
            elif choice == '2':
                self.mass_account_check("Spotify")
            elif choice == '3':
                self.display_valid_accounts("Spotify")
            elif choice == '4':
                self.display_dead_accounts("Spotify")
            elif choice == '5':
                self.download_valid_accounts("Spotify")
            elif choice == '6':
                break
            else:
                print("\nInvalid choice. Please try again.")

    def crunchyroll_menu(self):
        while True:
            print("\n" + Color.OKBLUE + "========================")
            print("   Crunchyroll Options")
            print("========================" + Color.ENDC)
            print("[1] Single Account Check")
            print("[2] Mass Account Check")
            print("[3] Valid Accounts")
            print("[4] Dead Accounts")
            print("[5] Download Valid Accounts")
            print("[6] Return to Main Menu")

            choice = input("\nEnter your choice: ")
            if choice == '1':
                self.single_account_check("Crunchyroll")
            elif choice == '2':
                self.mass_account_check("Crunchyroll")
            elif choice == '3':
                self.display_valid_accounts("Crunchyroll")
            elif choice == '4':
                self.display_dead_accounts("Crunchyroll")
            elif choice == '5':
                self.download_valid_accounts("Crunchyroll")
            elif choice == '6':
                break
            else:
                print("\nInvalid choice. Please try again.")

    def single_account_check(self, service):
        try:
            email = input(f"Enter {service} email address: ")
            password = input(f"Enter {service} password: ")

            # Simulate account check logic
            time.sleep(1)  # Placeholder for actual logic

            # Simulated validation logic
            if self.is_valid_account(service, email, password):
                print(Color.OKGREEN + "Account is valid." + Color.ENDC)
                self.valid_accounts.append(f"{email}:{password}")
            else:
                print(Color.FAIL + "Account is invalid." + Color.ENDC)
                self.invalid_accounts.append(f"{email}:{password}")

        except KeyboardInterrupt:
            print("\nOperation cancelled.")
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")

        input("\nPress Enter to continue...")

    def mass_account_check(self, service):
        try:
            accounts = self.get_accounts_input()
            total_accounts = len(accounts)
            print(f"\nChecking {total_accounts} accounts for {service}...")

            for index, account in enumerate(accounts, start=1):
                email, password = account.split(":")
                print(f"Checking account {index}/{total_accounts}...")
                time.sleep(1)  # Simulate account check process

                # Simulated validation logic
                if self.is_valid_account(service, email, password):
                    self.valid_accounts.append(f"{email}:{password}")
                else:
                    self.invalid_accounts.append(f"{email}:{password}")

            print("\nAll accounts checked.")
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")

        input("\nPress Enter to continue...")

    def get_accounts_input(self):
        print("\nPaste or enter email:password pairs (one pair per line). Press Enter twice to finish.")
        accounts = []
        while True:
            line = input()
            if line.strip() == "":
                break
            accounts.append(line.strip())
        return accounts

    def display_valid_accounts(self, service):
        print(f"\n" + Color.OKGREEN + "========================")
        print(f"   Valid {service} Accounts")
        print("========================" + Color.ENDC)
        for account in self.valid_accounts:
            print(f"- {account}")
        input("\nPress Enter to return to the service options...")

    def display_dead_accounts(self, service):
        print(f"\n" + Color.FAIL + "========================")
        print(f"   Dead {service} Accounts")
        print("========================" + Color.ENDC)
        for account in self.invalid_accounts:
            print(f"- {account}")
        input("\nPress Enter to return to the service options...")

    def download_valid_accounts(self, service):
        try:
            print(f"\n" + Color.OKBLUE + "========================")
            print(f"   Download Valid {service} Accounts")
            print("========================" + Color.ENDC)
            # Generate and download a file with valid accounts
            filename = f"valid_{service.lower()}_accounts.txt"
            with open(filename, 'w') as file:
                file.write("Valid Accounts:\n")
                for account in self.valid_accounts:
                    file.write(f"{account}\n")
                print(f"Download complete. File saved as '{filename}'")
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")
        input("\nPress Enter to return to the service options...")

    def check_for_update(self):
        try:
            print("\n" + Color.WARNING + "========================")
            print("   Checking for Update")
            print("========================" + Color.ENDC)
            # Simulate update check process
            print("No updates found.")
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")
        input("\nPress Enter to return to the Main Menu...")

    def join_telegram(self):
        try:
            print("\n" + Color.OKBLUE + "========================")
            print("   Join our Telegram")
            print("========================" + Color.ENDC)
            print("Opening Telegram link: https://t.me/DroidDevHub")
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")
        input("\nPress Enter to return to the Main Menu...")

    def follow_github(self):
        try:
            print("\n" + Color.OKBLUE + "========================")
            print("   Follow me on GitHub")
            print("========================" + Color.ENDC)
            print("Opening GitHub link: https://github.com/Techbyets")
        except Exception as e:
            print
