class Authentication:
    @staticmethod
    def set_password():
        while True:
            password = input("Set your password: ")
            return password

    @staticmethod
    def authenticate_user(saved_password):
        while True:
            password_attempt = input("Enter your password: ")
            if password_attempt == saved_password:
                print("Authentication successful!")
                break
            else:
                print("Authentication failed. Please try again.")
                
                
    @staticmethod
    def authenticate_fingerprint(fingerprint_data):
        """
        Authenticates user input using fingerprint data.

        Args:
            fingerprint_data: Fingerprint data provided by the user for authentication.

        Returns:
            True if authentication succeeds, False otherwise.
        """
        # Placeholder authentication logic
        # Assume fingerprint scanner is available
        # Compare provided fingerprint data with stored fingerprint data
        # Return True if match is found, False otherwise
        return True  # Placeholder result for demonstration purposes


# Set the password initially
saved_password = Authentication.set_password()

# Authenticate the user
Authentication.authenticate_user(saved_password)
