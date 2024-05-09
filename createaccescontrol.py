def create_access_control(authorized_user_id):
    def access_control(user_id, action):
        if user_id == authorized_user_id:
            print(f"Executing logic for user ID: {user_id}")
            action()
        else:
            print("Unauthorized")
    return access_control

access_control = create_access_control("user123")

access_control("user123", lambda: print("Authorized user performing action"))

access_control("user456", lambda: print("This should not be executed"))