import os
import json

USERS_DIR = "users"

def update_user_configs():
    print("--- User Configuration Tool ---")
    for filename in os.listdir(USERS_DIR):
        if filename.endswith(".json"):
            path = os.path.join(USERS_DIR, filename)
            with open(path, "r") as f:
                config = json.load(f)

            phone = config.get("phone", filename.replace(".json", ""))
            name = config.get("name", "Unknown")

            print(f"User: {name} ({phone})")
            try:
                input("  Press Enter to confirm user or Ctrl+C to cancel.")
                with open(path, "w") as f:
                    json.dump(config, f, indent=2)
                print("  ✅ Configuration updated.\n")
            except Exception as e:
                print(f"  ❌ Error: {e}. Skipping.\n")

if __name__ == "__main__":
    update_user_configs()
